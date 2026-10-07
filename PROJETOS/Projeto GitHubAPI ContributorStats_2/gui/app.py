"""
Janela principal (Tkinter + ttk).

Esta camada cuida apenas da apresentação. Toda a lógica de acesso à API,
ranking e exportação vem do pacote ``core``.

A análise roda em uma *thread* separada para não travar a janela; a thread
nunca toca nos widgets — ela envia mensagens por uma ``queue.Queue`` que a
thread principal consome com ``after()``.
"""

from __future__ import annotations

import queue
import threading
import tkinter as tk
import webbrowser
from datetime import datetime
from tkinter import filedialog, messagebox, ttk
from typing import Optional

from core import (
    AnalysisResult,
    Contributor,
    ContributorStatsError,
    OperationCancelledError,
    ProgressEvent,
    SortCriterion,
    analyze_repository,
    default_csv_filename,
    export_to_csv,
    rank_contributors,
)
from core.config import DEFAULT_REPO_URL, get_configured_token

from .theme import DARK, LIGHT, Fonts, Palette, apply_theme
from .widgets import BarChart, Card, StatCard


def fmt_int(value: int, signed: bool = False) -> str:
    """Formata inteiros no padrão brasileiro (1.234)."""
    text = f"{value:+,}" if signed else f"{value:,}"
    return text.replace(",", ".")


# Colunas da tabela: id -> (título, largura, alinhamento, função de valor p/ ordenação)
COLUMNS = {
    "rank": ("#", 50, "center", lambda c: c.rank),
    "user": ("Usuário", 170, "w", lambda c: c.username.lower()),
    "commits": ("Commits", 80, "e", lambda c: c.commits),
    "add": ("Inseridas", 90, "e", lambda c: c.additions),
    "del": ("Deletadas", 90, "e", lambda c: c.deletions),
    "net": ("Impacto líquido", 125, "e", lambda c: c.net_impact),
    "last": ("Último commit", 115, "center",
             lambda c: c.last_commit.toordinal() if c.last_commit else 0),
}

CHART_METRICS = {
    "Commits": lambda c: c.commits,
    "Linhas inseridas": lambda c: c.additions,
    "Linhas deletadas": lambda c: c.deletions,
    "Impacto líquido": lambda c: c.net_impact,
}


class ContributorStatsApp(tk.Tk):
    POLL_MS = 80

    def __init__(self):
        super().__init__()
        self.title("GitHub Contributor Stats")
        self.geometry("1280x880")
        self.minsize(1040, 680)

        self.palette: Palette = DARK
        self.fonts = Fonts(self)
        self.style = ttk.Style(self)

        # Estado
        self.result: Optional[AnalysisResult] = None
        self._queue: "queue.Queue[tuple[str, object]]" = queue.Queue()
        self._worker: Optional[threading.Thread] = None
        self._cancel_event = threading.Event()
        self._table_sort: tuple[str, bool] | None = None  # (coluna, decrescente)

        # Variáveis de formulário
        env_token = get_configured_token()
        self.var_url = tk.StringVar(value=DEFAULT_REPO_URL)
        self.var_token = tk.StringVar(value=env_token or "")
        self.var_show_token = tk.BooleanVar(value=False)
        self.var_exact_dates = tk.BooleanVar(value=True)
        self.var_sort = tk.StringVar(value=SortCriterion.COMMITS.label)
        self.var_filter = tk.StringVar()
        self.var_chart_metric = tk.StringVar(value="Commits")
        self.var_status = tk.StringVar(value="Pronto. Informe a URL do repositório e clique em Analisar.")
        self._token_hint = (
            "Token carregado de core/config.py."
            if env_token else
            "Opcional para repositórios públicos · necessário para privados (escopo repo)."
        )

        apply_theme(self, self.style, self.palette, self.fonts)
        self._build_ui()
        self._apply_widget_colors()
        self._bind_shortcuts()
        self.after(self.POLL_MS, self._process_queue)

    # ================================================================== #
    # Construção da interface
    # ================================================================== #
    def _build_ui(self) -> None:
        root = ttk.Frame(self, padding=(24, 20, 24, 16))
        root.pack(fill="both", expand=True)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(3, weight=1)

        self._build_header(root).grid(row=0, column=0, sticky="ew")
        self._build_form(root).grid(row=1, column=0, sticky="ew", pady=(16, 0))
        self._build_stats(root).grid(row=2, column=0, sticky="ew", pady=(16, 0))
        self._build_tabs(root).grid(row=3, column=0, sticky="nsew", pady=(16, 0))
        self._build_statusbar(root).grid(row=4, column=0, sticky="ew", pady=(12, 0))

    def _build_header(self, parent) -> ttk.Frame:
        frame = ttk.Frame(parent)
        self.logo = tk.Canvas(frame, width=44, height=44, highlightthickness=0, bd=0)
        self.logo.pack(side="left", padx=(0, 14))

        texts = ttk.Frame(frame)
        texts.pack(side="left")
        ttk.Label(texts, text="GitHub Contributor Stats", style="Title.TLabel").pack(anchor="w")
        ttk.Label(
            texts,
            text="Ranking de colaboradores por commits e linhas de código, via API do GitHub",
            style="Subtitle.TLabel",
        ).pack(anchor="w")

        self.btn_theme = ttk.Button(frame, text="Tema claro", command=self.toggle_theme)
        self.btn_theme.pack(side="right")
        return frame

    def _build_form(self, parent) -> Card:
        card = Card(parent, padding=(18, 14))
        b = card.body
        b.columnconfigure(0, weight=5)
        b.columnconfigure(1, weight=3)
        b.columnconfigure(2, weight=2)

        # --- Repositório
        ttk.Label(b, text="Repositório", style="Field.TLabel").grid(row=0, column=0, sticky="w")
        self.entry_url = ttk.Entry(b, textvariable=self.var_url)
        self.entry_url.grid(row=1, column=0, sticky="ew", padx=(0, 14), pady=(4, 0))

        # --- Token
        ttk.Label(b, text="Token de acesso (PAT)", style="Field.TLabel").grid(row=0, column=1, sticky="w")
        token_row = ttk.Frame(b, style="Card.TFrame")
        token_row.grid(row=1, column=1, sticky="ew", padx=(0, 14), pady=(4, 0))
        token_row.columnconfigure(0, weight=1)
        self.entry_token = ttk.Entry(token_row, textvariable=self.var_token, show="•")
        self.entry_token.grid(row=0, column=0, sticky="ew")
        self.btn_show = ttk.Button(token_row, text="Mostrar", width=8,
                                   command=self._toggle_token_visibility)
        self.btn_show.grid(row=0, column=1, padx=(6, 0))

        # --- Ordenação
        ttk.Label(b, text="Ordenar ranking por", style="Field.TLabel").grid(row=0, column=2, sticky="w")
        self.combo_sort = ttk.Combobox(
            b, textvariable=self.var_sort, state="readonly",
            values=[c.label for c in SortCriterion],
        )
        self.combo_sort.grid(row=1, column=2, sticky="ew", pady=(4, 0))
        self.combo_sort.bind("<<ComboboxSelected>>", self._on_sort_changed)

        # --- Linha inferior
        bottom = ttk.Frame(b, style="Card.TFrame")
        bottom.grid(row=2, column=0, columnspan=3, sticky="ew", pady=(12, 0))
        bottom.columnconfigure(1, weight=1)

        ttk.Checkbutton(
            bottom, text="Buscar data exata do último commit",
            variable=self.var_exact_dates,
        ).grid(row=0, column=0, sticky="w")
        ttk.Label(bottom, text="   " + self._token_hint, style="CardMuted.TLabel").grid(
            row=0, column=1, sticky="w")

        self.btn_cancel = ttk.Button(bottom, text="Cancelar", command=self.cancel_analysis,
                                     state="disabled")
        self.btn_cancel.grid(row=0, column=2, padx=(8, 0))
        self.btn_analyze = ttk.Button(bottom, text="Analisar repositório", style="Accent.TButton",
                                      command=self.start_analysis)
        self.btn_analyze.grid(row=0, column=3, padx=(8, 0))
        return card

    def _build_stats(self, parent) -> ttk.Frame:
        frame = ttk.Frame(parent)
        p = self.palette
        self.stat_contrib = StatCard(frame, "Colaboradores", p.chart[0])
        self.stat_commits = StatCard(frame, "Commits", p.chart[2])
        self.stat_add = StatCard(frame, "Linhas inseridas", p.success)
        self.stat_del = StatCard(frame, "Linhas deletadas", p.danger)
        self.stat_cards = [self.stat_contrib, self.stat_commits, self.stat_add, self.stat_del]
        for i, card in enumerate(self.stat_cards):
            frame.columnconfigure(i, weight=1, uniform="stats")
            card.grid(row=0, column=i, sticky="ew", padx=(0 if i == 0 else 12, 0))
        return frame

    def _build_tabs(self, parent) -> ttk.Notebook:
        nb = ttk.Notebook(parent)
        self.notebook = nb

        # ---------------- Aba Ranking ----------------
        tab = ttk.Frame(nb, padding=(0, 12, 0, 0))
        tab.columnconfigure(0, weight=7)
        tab.columnconfigure(1, weight=4)
        tab.rowconfigure(0, weight=1)
        nb.add(tab, text="Ranking")

        # Tabela
        table_card = Card(tab, padding=(16, 14))
        table_card.grid(row=0, column=0, sticky="nsew", padx=(0, 12))
        tb = table_card.body
        tb.columnconfigure(0, weight=1)
        tb.rowconfigure(1, weight=1)

        head = ttk.Frame(tb, style="Card.TFrame")
        head.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10))
        head.columnconfigure(0, weight=1)
        title_box = ttk.Frame(head, style="Card.TFrame")
        title_box.grid(row=0, column=0, sticky="w")
        ttk.Label(title_box, text="Ranking de colaboradores", style="Section.TLabel").pack(anchor="w")
        self.lbl_repo = ttk.Label(title_box, text="Nenhum repositório analisado",
                                  style="CardMuted.TLabel")
        self.lbl_repo.pack(anchor="w")

        ttk.Label(head, text="Filtrar", style="CardMuted.TLabel").grid(row=0, column=1, padx=(0, 6))
        self.entry_filter = ttk.Entry(head, textvariable=self.var_filter, width=18)
        self.entry_filter.grid(row=0, column=2)
        self.var_filter.trace_add("write", lambda *_: self._refresh_table())
        self.btn_export = ttk.Button(head, text="Exportar CSV", command=self.export_csv,
                                     state="disabled")
        self.btn_export.grid(row=0, column=3, padx=(8, 0))

        self.tree = ttk.Treeview(tb, columns=list(COLUMNS), show="headings", selectmode="browse")
        for col, (title, width, anchor, _) in COLUMNS.items():
            self.tree.heading(col, text=title, anchor=anchor,
                              command=lambda c=col: self._sort_table_by(c))
            self.tree.column(col, width=width, minwidth=50, anchor=anchor,
                             stretch=(col == "user"))
        self.tree.grid(row=1, column=0, sticky="nsew")
        scroll = ttk.Scrollbar(tb, orient="vertical", command=self.tree.yview)
        scroll.grid(row=1, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.bind("<Double-1>", lambda _e: self._open_selected_profile())
        self.tree.bind("<Button-3>", self._show_context_menu)
        self.tree.bind("<Button-2>", self._show_context_menu)  # macOS

        ttk.Label(tb, text="Dica: clique no cabeçalho para ordenar · duplo clique abre o perfil no GitHub",
                  style="CardMuted.TLabel").grid(row=2, column=0, columnspan=2, sticky="w", pady=(8, 0))

        self.menu = tk.Menu(self, tearoff=0)
        self.menu.add_command(label="Abrir perfil no GitHub", command=self._open_selected_profile)
        self.menu.add_command(label="Copiar nome de usuário", command=self._copy_selected_username)

        # Gráfico
        chart_card = Card(tab, padding=(16, 14))
        chart_card.grid(row=0, column=1, sticky="nsew")
        cb = chart_card.body
        cb.columnconfigure(0, weight=1)
        cb.rowconfigure(1, weight=1)
        chead = ttk.Frame(cb, style="Card.TFrame")
        chead.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        chead.columnconfigure(0, weight=1)
        ctitle = ttk.Frame(chead, style="Card.TFrame")
        ctitle.grid(row=0, column=0, sticky="w")
        ttk.Label(ctitle, text="Top 10", style="Section.TLabel").pack(anchor="w")
        ttk.Label(ctitle, text="Comparativo por métrica",
                  style="CardMuted.TLabel").pack(anchor="w")
        combo_metric = ttk.Combobox(chead, textvariable=self.var_chart_metric, state="readonly",
                                    values=list(CHART_METRICS), width=15)
        combo_metric.grid(row=0, column=1, sticky="e")
        combo_metric.bind("<<ComboboxSelected>>", lambda _e: self._refresh_chart())

        self.chart = BarChart(cb, self.palette, self.fonts, height=300)
        self.chart.grid(row=1, column=0, sticky="nsew")

        # ---------------- Aba Log ----------------
        log_tab = ttk.Frame(nb, padding=(0, 12, 0, 0))
        nb.add(log_tab, text="Log de execução")
        log_card = Card(log_tab, padding=(12, 10))
        log_card.pack(fill="both", expand=True)
        lb = log_card.body
        lb.columnconfigure(0, weight=1)
        lb.rowconfigure(0, weight=1)
        self.log = tk.Text(lb, wrap="word", bd=0, highlightthickness=0, padx=8, pady=6,
                           font=self.fonts.mono, state="disabled", height=10)
        self.log.grid(row=0, column=0, sticky="nsew")
        log_scroll = ttk.Scrollbar(lb, orient="vertical", command=self.log.yview)
        log_scroll.grid(row=0, column=1, sticky="ns")
        self.log.configure(yscrollcommand=log_scroll.set)
        return nb

    def _build_statusbar(self, parent) -> Card:
        card = Card(parent, padding=(14, 8))
        b = card.body
        b.columnconfigure(0, weight=1)
        ttk.Label(b, textvariable=self.var_status, style="StatusBar.TLabel").grid(
            row=0, column=0, sticky="w")
        self.progress = ttk.Progressbar(b, style="Accent.Horizontal.TProgressbar",
                                        mode="determinate", length=240)
        self.progress.grid(row=0, column=1, sticky="e")
        return card

    def _bind_shortcuts(self) -> None:
        self.entry_url.bind("<Return>", lambda _e: self.start_analysis())
        self.entry_token.bind("<Return>", lambda _e: self.start_analysis())
        self.bind_all("<Control-e>", lambda _e: self.export_csv())
        self.bind_all("<Command-e>", lambda _e: self.export_csv())
        self.bind("<Escape>", lambda _e: self.cancel_analysis())

    # ================================================================== #
    # Tema
    # ================================================================== #
    def toggle_theme(self) -> None:
        self.palette = LIGHT if self.palette is DARK else DARK
        apply_theme(self, self.style, self.palette, self.fonts)
        self.btn_theme.configure(text="Tema claro" if self.palette is DARK else "Tema escuro")
        self._apply_widget_colors()
        self._refresh_table()

    def _apply_widget_colors(self) -> None:
        """Recolore os widgets tk (não-ttk), que não usam ttk.Style."""
        p = self.palette
        # Logo: três barras crescentes (um mini gráfico)
        self.logo.configure(bg=p.bg)
        self.logo.delete("all")
        self.logo.create_rectangle(0, 0, 44, 44, fill=p.surface, outline=p.border)
        for i, (h, color) in enumerate(zip((14, 22, 30), (p.chart[0], p.chart[2], p.chart[1]))):
            x = 9 + i * 10
            self.logo.create_rectangle(x, 37 - h, x + 7, 37, fill=color, outline="")

        accents = (p.chart[0], p.chart[2], p.success, p.danger)
        for card, accent in zip(self.stat_cards, accents):
            card.recolor(p, accent)

        self.chart.set_palette(p)
        self.log.configure(bg=p.surface, fg=p.text, insertbackground=p.text,
                           selectbackground=p.selection)
        for level, color in (("info", p.text), ("success", p.success),
                             ("warning", p.warning), ("error", p.danger), ("time", p.muted)):
            self.log.tag_configure(level, foreground=color)
        self.menu.configure(bg=p.surface, fg=p.text, activebackground=p.accent,
                            activeforeground=p.accent_text, bd=0)

        self.tree.tag_configure("odd", background=p.surface)
        self.tree.tag_configure("even", background=p.surface_alt)
        self.tree.tag_configure("top", font=self.fonts.body_bold)

    # ================================================================== #
    # Ações
    # ================================================================== #
    def _toggle_token_visibility(self) -> None:
        show = not self.var_show_token.get()
        self.var_show_token.set(show)
        self.entry_token.configure(show="" if show else "•")
        self.btn_show.configure(text="Ocultar" if show else "Mostrar")

    def _selected_criterion(self) -> SortCriterion:
        for c in SortCriterion:
            if c.label == self.var_sort.get():
                return c
        return SortCriterion.COMMITS

    def start_analysis(self) -> None:
        if self._worker and self._worker.is_alive():
            return

        url = self.var_url.get().strip()
        token = self.var_token.get().strip() or None
        criterion = self._selected_criterion()
        exact = self.var_exact_dates.get()

        self._cancel_event = threading.Event()
        self._set_busy(True)
        self._log(ProgressEvent(f"Iniciando análise de {url}"))
        self.progress.configure(mode="indeterminate")
        self.progress.start(12)

        def worker():
            try:
                result = analyze_repository(
                    url, token, criterion=criterion, fetch_exact_dates=exact,
                    on_progress=lambda ev: self._queue.put(("progress", ev)),
                    cancel_event=self._cancel_event,
                )
                self._queue.put(("done", result))
            except OperationCancelledError:
                self._queue.put(("cancelled", None))
            except ContributorStatsError as exc:
                self._queue.put(("error", exc))
            except Exception as exc:  # erro inesperado: também vai para a GUI
                self._queue.put(("error", exc))

        self._worker = threading.Thread(target=worker, daemon=True)
        self._worker.start()

    def cancel_analysis(self) -> None:
        if self._worker and self._worker.is_alive():
            self._cancel_event.set()
            self.var_status.set("Cancelando…")
            self.btn_cancel.configure(state="disabled")

    def export_csv(self) -> None:
        if not self.result or not self.result.contributors:
            return
        path = filedialog.asksaveasfilename(
            title="Exportar ranking",
            initialfile=default_csv_filename(self.result.repo),
            defaultextension=".csv",
            filetypes=[("CSV (separado por ;)", "*.csv"), ("Todos os arquivos", "*.*")],
        )
        if not path:
            return
        try:
            saved = export_to_csv(self.result.contributors, path)
        except (OSError, ValueError) as exc:
            messagebox.showerror("Erro ao exportar", str(exc), parent=self)
            return
        self._log(ProgressEvent(f"Ranking exportado para {saved}", "success"))
        self.var_status.set(f"CSV salvo em {saved}")

    def _on_sort_changed(self, _event=None) -> None:
        # Reordena localmente — não precisa consultar a API de novo
        if self.result:
            self.result.contributors = rank_contributors(
                self.result.contributors, self._selected_criterion())
            self._table_sort = None
            self._refresh_table()
            self._refresh_chart()

    # ================================================================== #
    # Comunicação com a thread de trabalho
    # ================================================================== #
    def _process_queue(self) -> None:
        try:
            while True:
                kind, payload = self._queue.get_nowait()
                if kind == "progress":
                    self._on_progress(payload)  # type: ignore[arg-type]
                elif kind == "done":
                    self._on_done(payload)  # type: ignore[arg-type]
                elif kind == "cancelled":
                    self._on_finished("Análise cancelada.", "warning")
                elif kind == "error":
                    self._on_error(payload)  # type: ignore[arg-type]
        except queue.Empty:
            pass
        self.after(self.POLL_MS, self._process_queue)

    def _on_progress(self, event: ProgressEvent) -> None:
        self._log(event)
        self.var_status.set(event.message)
        if event.total:
            if str(self.progress.cget("mode")) != "determinate":
                self.progress.stop()
                self.progress.configure(mode="determinate")
            self.progress.configure(maximum=event.total, value=event.current or 0)

    def _on_done(self, result: AnalysisResult) -> None:
        self.result = result
        self._table_sort = None
        self._update_stats()
        self._refresh_table()
        self._refresh_chart()
        self.lbl_repo.configure(
            text=result.full_name)
        self.btn_export.configure(state="normal" if result.contributors else "disabled")
        self._on_finished(
            f"Análise de {result.full_name} concluída às {datetime.now():%H:%M:%S} · "
            f"{len(result.contributors)} colaborador(es).", "success")
        self.notebook.select(0)

    def _on_error(self, exc: Exception) -> None:
        self._on_finished(f"Erro: {exc}", "error")
        messagebox.showerror("Não foi possível analisar o repositório", str(exc), parent=self)

    def _on_finished(self, message: str, level: str) -> None:
        self._log(ProgressEvent(message, level))
        self.var_status.set(message)
        self.progress.stop()
        self.progress.configure(mode="determinate", maximum=1,
                                value=1 if level == "success" else 0)
        self._set_busy(False)

    def _set_busy(self, busy: bool) -> None:
        self.btn_analyze.configure(state="disabled" if busy else "normal")
        self.btn_cancel.configure(state="normal" if busy else "disabled")
        for w in (self.entry_url, self.entry_token):
            w.configure(state="disabled" if busy else "normal")
        self.configure(cursor="watch" if busy else "")

    # ================================================================== #
    # Atualização dos componentes de dados
    # ================================================================== #
    def _update_stats(self) -> None:
        r = self.result
        if not r:
            return
        n = len(r.contributors)
        self.stat_contrib.set(fmt_int(n), "com ao menos um commit")
        avg = r.total_commits / n if n else 0
        self.stat_commits.set(fmt_int(r.total_commits),
                              f"média de {avg:.1f} por colaborador".replace(".", ","))
        self.stat_add.set(fmt_int(r.total_additions), "linhas adicionadas")
        net = r.total_net_impact
        self.stat_del.set(
            fmt_int(r.total_deletions),
            f"impacto líquido {fmt_int(net, signed=True)}",
            "StatSuccess.TLabel" if net >= 0 else "StatDanger.TLabel",
        )

    def _visible_contributors(self) -> list[Contributor]:
        if not self.result:
            return []
        items = list(self.result.contributors)
        term = self.var_filter.get().strip().lower()
        if term:
            items = [c for c in items if term in c.username.lower()]
        if self._table_sort:
            col, desc = self._table_sort
            items.sort(key=COLUMNS[col][3], reverse=desc)
        return items

    def _refresh_table(self) -> None:
        self.tree.delete(*self.tree.get_children())
        for i, c in enumerate(self._visible_contributors()):
            tags = ["even" if i % 2 else "odd"]
            if c.rank <= 3:
                tags.append("top")
            self.tree.insert("", "end", iid=str(c.rank), tags=tags, values=(
                f"{c.rank}º", c.username, fmt_int(c.commits), fmt_int(c.additions),
                fmt_int(c.deletions), fmt_int(c.net_impact, signed=True),
                c.last_commit_display,
            ))
        # Indicador de ordenação nos cabeçalhos
        for col, (title, *_rest) in COLUMNS.items():
            arrow = ""
            if self._table_sort and self._table_sort[0] == col:
                arrow = "  ▼" if self._table_sort[1] else "  ▲"
            self.tree.heading(col, text=title + arrow)

    def _sort_table_by(self, col: str) -> None:
        if self._table_sort and self._table_sort[0] == col:
            self._table_sort = (col, not self._table_sort[1])
        else:
            # Texto começa crescente; números começam decrescente
            self._table_sort = (col, col not in ("user", "rank"))
        self._refresh_table()

    def _refresh_chart(self) -> None:
        if not self.result:
            self.chart.set_data([])
            return
        metric = CHART_METRICS[self.var_chart_metric.get()]
        top = sorted(self.result.contributors, key=metric, reverse=True)[:10]
        self.chart.set_data([(c.username, metric(c)) for c in top])

    # ================================================================== #
    # Utilidades
    # ================================================================== #
    def _log(self, event: ProgressEvent) -> None:
        self.log.configure(state="normal")
        self.log.insert("end", f"{datetime.now():%H:%M:%S}  ", "time")
        self.log.insert("end", event.message + "\n", event.level)
        self.log.see("end")
        self.log.configure(state="disabled")

    def _selected_contributor(self) -> Optional[Contributor]:
        sel = self.tree.selection()
        if not sel or not self.result:
            return None
        return next((c for c in self.result.contributors if str(c.rank) == sel[0]), None)

    def _open_selected_profile(self) -> None:
        c = self._selected_contributor()
        if c and c.profile_url:
            webbrowser.open(c.profile_url)

    def _copy_selected_username(self) -> None:
        c = self._selected_contributor()
        if c:
            self.clipboard_clear()
            self.clipboard_append(c.username)
            self.var_status.set(f"'{c.username}' copiado para a área de transferência.")

    def _show_context_menu(self, event) -> None:
        row = self.tree.identify_row(event.y)
        if row:
            self.tree.selection_set(row)
            self.menu.tk_popup(event.x_root, event.y_root)


def run() -> None:
    app = ContributorStatsApp()
    app.mainloop()
