"""Paletas de cores, fontes e estilos ttk da interface."""

from __future__ import annotations

import sys
import tkinter as tk
from dataclasses import dataclass
from tkinter import font as tkfont
from tkinter import ttk


@dataclass(frozen=True)
class Palette:
    name: str
    bg: str          # fundo da janela
    surface: str     # cartões
    surface_alt: str # campos / linhas alternadas
    border: str
    text: str
    muted: str
    accent: str
    accent_hover: str
    accent_text: str
    success: str
    danger: str
    warning: str
    selection: str
    chart: tuple[str, ...]


DARK = Palette(
    name="dark",
    bg="#0d1117",
    surface="#161b22",
    surface_alt="#1c2330",
    border="#30363d",
    text="#e6edf3",
    muted="#8b949e",
    accent="#2f81f7",
    accent_hover="#4c94ff",
    accent_text="#ffffff",
    success="#3fb950",
    danger="#f85149",
    warning="#d29922",
    selection="#1f3a5f",
    chart=("#2f81f7", "#3fb950", "#a371f7", "#d29922", "#f778ba",
           "#39c5cf", "#ff7b72", "#7ee787", "#79c0ff", "#e3b341"),
)

LIGHT = Palette(
    name="light",
    bg="#f3f5f8",
    surface="#ffffff",
    surface_alt="#f6f8fa",
    border="#d0d7de",
    text="#1f2328",
    muted="#636c76",
    accent="#0969da",
    accent_hover="#0a5cc2",
    accent_text="#ffffff",
    success="#1a7f37",
    danger="#cf222e",
    warning="#9a6700",
    selection="#ddf4ff",
    chart=("#0969da", "#1a7f37", "#8250df", "#bf8700", "#bf3989",
           "#1b7c83", "#cf222e", "#2da44e", "#218bff", "#9a6700"),
)


def _pick_family(root: tk.Misc, candidates: list[str]) -> str:
    available = {f.lower() for f in tkfont.families(root)}
    for name in candidates:
        if name.lower() in available:
            return name
    return "TkDefaultFont"


class Fonts:
    """Fontes escolhidas conforme o sistema operacional."""

    def __init__(self, root: tk.Misc):
        if sys.platform == "darwin":
            ui = ["SF Pro Text", "Helvetica Neue", "Helvetica"]
            mono = ["SF Mono", "Menlo", "Monaco"]
        elif sys.platform.startswith("win"):
            ui = ["Segoe UI", "Calibri", "Arial"]
            mono = ["Cascadia Mono", "Consolas", "Courier New"]
        else:
            ui = ["Inter", "Cantarell", "Ubuntu", "DejaVu Sans"]
            mono = ["JetBrains Mono", "DejaVu Sans Mono", "Monospace"]

        family = _pick_family(root, ui)
        mono_family = _pick_family(root, mono)

        self.body = (family, 10)
        self.body_bold = (family, 10, "bold")
        self.small = (family, 9)
        self.title = (family, 17, "bold")
        self.subtitle = (family, 10)
        self.section = (family, 11, "bold")
        self.stat_value = (family, 20, "bold")
        self.stat_label = (family, 9)
        self.mono = (mono_family, 9)


def apply_theme(root: tk.Tk, style: ttk.Style, p: Palette, f: Fonts) -> None:
    """Configura todos os estilos ttk para a paleta informada."""
    style.theme_use("clam")
    root.configure(bg=p.bg)

    style.configure(".", background=p.bg, foreground=p.text, font=f.body,
                    bordercolor=p.border, focuscolor=p.accent,
                    troughcolor=p.surface_alt)

    # --- Frames / Labels -------------------------------------------------
    style.configure("TFrame", background=p.bg)
    style.configure("Card.TFrame", background=p.surface, relief="flat")
    style.configure("Border.TFrame", background=p.border)

    style.configure("TLabel", background=p.bg, foreground=p.text)
    style.configure("Title.TLabel", font=f.title)
    style.configure("Subtitle.TLabel", foreground=p.muted, font=f.subtitle)
    style.configure("Card.TLabel", background=p.surface, foreground=p.text)
    style.configure("CardMuted.TLabel", background=p.surface, foreground=p.muted, font=f.small)
    style.configure("Section.TLabel", background=p.surface, foreground=p.text, font=f.section)
    style.configure("Field.TLabel", background=p.surface, foreground=p.muted, font=f.body_bold)
    style.configure("StatLabel.TLabel", background=p.surface, foreground=p.muted, font=f.stat_label)
    style.configure("StatValue.TLabel", background=p.surface, foreground=p.text, font=f.stat_value)
    style.configure("StatCaption.TLabel", background=p.surface, foreground=p.muted, font=f.small)
    style.configure("StatusBar.TLabel", background=p.surface, foreground=p.muted, font=f.small)
    for lvl, color in (("Success", p.success), ("Danger", p.danger), ("Warning", p.warning)):
        style.configure(f"Stat{lvl}.TLabel", background=p.surface, foreground=color, font=f.small)

    # --- Entradas ----------------------------------------------------------
    field_opts = dict(fieldbackground=p.surface_alt, foreground=p.text,
                      insertcolor=p.text, bordercolor=p.border,
                      lightcolor=p.surface_alt, darkcolor=p.surface_alt,
                      padding=(10, 7), selectbackground=p.accent,
                      selectforeground=p.accent_text)
    style.configure("TEntry", **field_opts)
    style.map("TEntry",
              bordercolor=[("focus", p.accent)],
              lightcolor=[("focus", p.accent)],
              darkcolor=[("focus", p.accent)])

    style.configure("TCombobox", **field_opts, arrowcolor=p.muted, background=p.surface_alt)
    style.map("TCombobox",
              fieldbackground=[("readonly", p.surface_alt)],
              foreground=[("readonly", p.text)],
              selectbackground=[("readonly", p.surface_alt)],
              selectforeground=[("readonly", p.text)],
              bordercolor=[("focus", p.accent)],
              background=[("active", p.surface_alt)],
              arrowcolor=[("active", p.text)])
    root.option_add("*TCombobox*Listbox.background", p.surface)
    root.option_add("*TCombobox*Listbox.foreground", p.text)
    root.option_add("*TCombobox*Listbox.selectBackground", p.accent)
    root.option_add("*TCombobox*Listbox.selectForeground", p.accent_text)
    root.option_add("*TCombobox*Listbox.font", f.body)

    # --- Botões ------------------------------------------------------------
    style.configure("TButton", background=p.surface_alt, foreground=p.text,
                    bordercolor=p.border, lightcolor=p.surface_alt,
                    darkcolor=p.surface_alt, padding=(14, 7), font=f.body_bold,
                    focusthickness=0)
    style.map("TButton",
              background=[("disabled", p.surface), ("pressed", p.border), ("active", p.border)],
              foreground=[("disabled", p.muted)],
              lightcolor=[("active", p.border)], darkcolor=[("active", p.border)])

    style.configure("Accent.TButton", background=p.accent, foreground=p.accent_text,
                    bordercolor=p.accent, lightcolor=p.accent, darkcolor=p.accent)
    style.map("Accent.TButton",
              background=[("disabled", p.border), ("pressed", p.accent_hover), ("active", p.accent_hover)],
              foreground=[("disabled", p.muted)],
              bordercolor=[("disabled", p.border), ("active", p.accent_hover)],
              lightcolor=[("disabled", p.border), ("active", p.accent_hover)],
              darkcolor=[("disabled", p.border), ("active", p.accent_hover)])

    style.configure("Ghost.TButton", background=p.surface, bordercolor=p.surface,
                    lightcolor=p.surface, darkcolor=p.surface, padding=(8, 5))
    style.map("Ghost.TButton",
              background=[("active", p.surface_alt)],
              bordercolor=[("active", p.border)])

    style.configure("TCheckbutton", background=p.surface, foreground=p.text,
                    indicatorbackground=p.surface_alt, indicatorforeground=p.accent_text,
                    bordercolor=p.border, focuscolor=p.surface, upperbordercolor=p.border,
                    lowerbordercolor=p.border)
    style.map("TCheckbutton",
              background=[("active", p.surface)],
              indicatorbackground=[("selected", p.accent), ("active", p.surface_alt)])

    # --- Treeview ------------------------------------------------------------
    style.configure("Treeview", background=p.surface, fieldbackground=p.surface,
                    foreground=p.text, bordercolor=p.surface, lightcolor=p.surface,
                    darkcolor=p.surface, rowheight=30, font=f.body)
    style.map("Treeview",
              background=[("selected", p.selection)],
              foreground=[("selected", p.text)])
    style.configure("Treeview.Heading", background=p.surface, foreground=p.muted,
                    bordercolor=p.border, lightcolor=p.surface, darkcolor=p.surface,
                    relief="flat", font=f.body_bold, padding=(8, 8))
    style.map("Treeview.Heading",
              background=[("active", p.surface_alt)],
              foreground=[("active", p.text)])
    style.layout("Treeview", [("Treeview.treearea", {"sticky": "nswe"})])

    # --- Scrollbar / Progressbar / Notebook ------------------------------------
    style.configure("Vertical.TScrollbar", background=p.surface_alt, troughcolor=p.surface,
                    bordercolor=p.surface, lightcolor=p.surface_alt, darkcolor=p.surface_alt,
                    arrowcolor=p.muted, gripcount=0)
    style.map("Vertical.TScrollbar", background=[("active", p.border)])

    style.configure("Accent.Horizontal.TProgressbar", background=p.accent,
                    troughcolor=p.surface_alt, bordercolor=p.surface,
                    lightcolor=p.accent, darkcolor=p.accent, thickness=6)

    style.configure("TNotebook", background=p.bg, bordercolor=p.bg,
                    lightcolor=p.bg, darkcolor=p.bg, tabmargins=(0, 0, 0, 0))
    style.configure("TNotebook.Tab", background=p.bg, foreground=p.muted,
                    bordercolor=p.bg, lightcolor=p.bg, darkcolor=p.bg,
                    padding=(16, 8), font=f.body_bold, focuscolor=p.bg)
    style.map("TNotebook.Tab",
              background=[("selected", p.surface), ("active", p.surface_alt)],
              foreground=[("selected", p.text), ("active", p.text)],
              lightcolor=[("selected", p.surface)],
              bordercolor=[("selected", p.border)])
