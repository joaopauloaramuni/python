"""Componentes visuais reutilizáveis da interface."""

from __future__ import annotations

import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
from typing import Sequence

from .theme import Fonts, Palette


class Card(ttk.Frame):
    """Cartão com borda de 1px. Use ``.body`` para inserir conteúdo."""

    def __init__(self, master, padding=16, **kwargs):
        super().__init__(master, style="Border.TFrame", padding=1, **kwargs)
        self.body = ttk.Frame(self, style="Card.TFrame", padding=padding)
        self.body.pack(fill="both", expand=True)


class StatCard(Card):
    """Cartão de indicador (KPI): rótulo, valor grande e legenda."""

    def __init__(self, master, label: str, accent: str, **kwargs):
        super().__init__(master, padding=(16, 12), **kwargs)
        top = ttk.Frame(self.body, style="Card.TFrame")
        top.pack(fill="x")
        self._dot = tk.Canvas(top, width=10, height=10, highlightthickness=0, bd=0)
        self._dot.pack(side="left", padx=(0, 8))
        self._accent = accent
        ttk.Label(top, text=label.upper(), style="StatLabel.TLabel").pack(side="left")

        self.value = ttk.Label(self.body, text="—", style="StatValue.TLabel")
        self.value.pack(anchor="w", pady=(6, 0))
        self.caption = ttk.Label(self.body, text=" ", style="StatCaption.TLabel")
        self.caption.pack(anchor="w")

    def recolor(self, p: Palette, accent: str | None = None) -> None:
        if accent:
            self._accent = accent
        self._dot.configure(bg=p.surface)
        self._dot.delete("all")
        self._dot.create_oval(1, 1, 9, 9, fill=self._accent, outline="")

    def set(self, value: str, caption: str = " ", caption_style: str = "StatCaption.TLabel"):
        self.value.configure(text=value)
        self.caption.configure(text=caption, style=caption_style)


class BarChart(tk.Canvas):
    """Gráfico de barras horizontais desenhado em ``tk.Canvas`` (sem dependências)."""

    def __init__(self, master, palette: Palette, fonts: Fonts, **kwargs):
        super().__init__(master, highlightthickness=0, bd=0, **kwargs)
        self.palette = palette
        self.fonts = fonts
        self._items: list[tuple[str, float]] = []
        self._value_fmt = "{:,.0f}"
        self._empty_text = "Os dados aparecerão aqui após a análise."
        self.bind("<Configure>", lambda _e: self.redraw())

    def set_palette(self, palette: Palette) -> None:
        self.palette = palette
        self.redraw()

    def set_data(self, items: Sequence[tuple[str, float]], value_fmt: str = "{:,.0f}") -> None:
        self._items = list(items)
        self._value_fmt = value_fmt
        self.redraw()

    def redraw(self) -> None:
        p, f = self.palette, self.fonts
        self.configure(bg=p.surface)
        self.delete("all")
        width, height = self.winfo_width(), self.winfo_height()
        if width < 50 or height < 50:
            return

        if not self._items:
            self.create_text(width / 2, height / 2, text=self._empty_text,
                             fill=p.muted, font=f.body, width=width - 40)
            return

        label_font = tkfont.Font(font=f.body)
        value_font = tkfont.Font(font=f.body_bold)
        pad_x, top = 4, 6
        label_w = min(
            max(label_font.measure(self._short(n)) for n, _ in self._items) + 12,
            int(width * 0.42),
        )
        value_w = max(value_font.measure(self._fmt(v)) for _, v in self._items) + 10
        bar_area = max(width - pad_x * 2 - label_w - value_w, 20)

        n = len(self._items)
        row_h = min(34, max(22, (height - top * 2) / n))
        bar_h = max(10, row_h * 0.5)
        max_val = max((abs(v) for _, v in self._items), default=1) or 1

        for i, (name, val) in enumerate(self._items):
            y = top + i * row_h + row_h / 2
            color = p.chart[i % len(p.chart)]
            self.create_text(pad_x, y, text=self._short(name), anchor="w",
                             fill=p.text, font=f.body)
            x0 = pad_x + label_w
            # trilho
            self._round_rect(x0, y - bar_h / 2, x0 + bar_area, y + bar_h / 2,
                             r=bar_h / 2, fill=p.surface_alt)
            # barra
            length = max(bar_h, bar_area * abs(val) / max_val)
            bar_color = color if val >= 0 else p.danger
            self._round_rect(x0, y - bar_h / 2, x0 + length, y + bar_h / 2,
                             r=bar_h / 2, fill=bar_color)
            self.create_text(x0 + bar_area + 8, y, text=self._fmt(val),
                             anchor="w", fill=p.text, font=f.body_bold)

    # -- utilidades -----------------------------------------------------------
    def _fmt(self, v: float) -> str:
        return self._value_fmt.format(v).replace(",", ".")

    @staticmethod
    def _short(name: str, limit: int = 18) -> str:
        return name if len(name) <= limit else name[: limit - 1] + "…"

    def _round_rect(self, x0, y0, x1, y1, r, **kw):
        r = min(r, (x1 - x0) / 2, (y1 - y0) / 2)
        pts = [x0 + r, y0, x1 - r, y0, x1, y0, x1, y0 + r, x1, y1 - r, x1, y1,
               x1 - r, y1, x0 + r, y1, x0, y1, x0, y1 - r, x0, y0 + r, x0, y0]
        return self.create_polygon(pts, smooth=True, outline="", **kw)
