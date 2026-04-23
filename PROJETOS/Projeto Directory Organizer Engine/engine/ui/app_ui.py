import logging
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from typing import Callable, Optional
from engine.ui.components import LogView
from engine.config.settings import APP_THEME, APP_TITLE, WINDOW_SIZE
from tkinter import PhotoImage

class OrganizerWindow(ttk.Window):
    def __init__(self, on_select_folder, on_start):
        super().__init__(
            title=APP_TITLE,
            themename=APP_THEME,
            resizable=(False, False)
        )
 
        import sys, os
 
        def resource_path(relative_path):
            try:
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")
            return os.path.join(base_path, relative_path)
 
        icon_path = resource_path("assets/logoEXE.ico")
 
        self.after(0, lambda: self.iconbitmap(icon_path))
        self.after(10, lambda: self.wm_iconbitmap(icon_path))
        self.after(50, lambda: self.wm_iconbitmap(icon_path))
 
        self.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")
        
        self.on_select_folder = on_select_folder
        self.on_start = on_start
        
        self.selected_path_var = ttk.StringVar(value="Nenhuma pasta selecionada")
        self.progress_var = ttk.DoubleVar(value=0)
        self.status_var = ttk.StringVar(value="Aguardando...")
        
        print("Construindo interface gráfica...")
        self._build_ui()
        # Removed place_window_center() as it can cause initialization lag

    def _build_ui(self):
        # Main Container
        container = ttk.Frame(self)
        container.pack(fill=BOTH, expand=YES, padx=20, pady=20)
        
        # Header section
        header_frame = ttk.Frame(container)
        header_frame.pack(fill=X, pady=(0, 20))
        
        ttk.Label(
            header_frame, 
            text=APP_TITLE, 
            font=("Helvetica", 18, "bold"),
            bootstyle=PRIMARY
        ).pack(side=LEFT)
        
        # Selection section
        selection_frame = ttk.LabelFrame(container, text=" Seleção de Pasta ")
        selection_frame.pack(fill=X, pady=(0, 20), ipady=5)  # Use ipady for internal space if needed
        
        path_entry = ttk.Entry(
            selection_frame, 
            textvariable=self.selected_path_var, 
            state="readonly",
            bootstyle=SECONDARY
        )
        path_entry.pack(side=LEFT, fill=X, expand=YES, padx=(0, 10))
        
        select_btn = ttk.Button(
            selection_frame, 
            text="Selecionar Pasta", 
            command=self.on_select_folder,
            bootstyle=INFO
        )
        select_btn.pack(side=LEFT)
        
        # Progress section
        progress_frame = ttk.Frame(container)
        progress_frame.pack(fill=X, pady=(0, 20))
        
        self.progress_bar = ttk.Floodgauge(
            progress_frame,
            variable=self.progress_var,
            text="0%",
            bootstyle=SUCCESS,
            font=("Helvetica", 10, "bold")
        )
        self.progress_bar.pack(fill=X, pady=(0, 10))
        
        self.status_label = ttk.Label(
            progress_frame,
            textvariable=self.status_var,
            font=("Helvetica", 9, "italic")
        )
        self.status_label.pack(side=LEFT)
        
        self.start_btn = ttk.Button(
            progress_frame,
            text="Iniciar Organização",
            command=self.on_start,
            bootstyle=(SUCCESS, OUTLINE),
            width=20
        )
        self.start_btn.pack(side=RIGHT)
        
        # Log section
        self.log_view = LogView(container)
        self.log_view.pack(fill=BOTH, expand=YES)
        
        # Footer
        footer = ttk.Label(
            container, 
            text="© 2026 Engine de Organização de Arquivos - Cross-platform", 
            font=("Helvetica", 8),
            bootstyle=SECONDARY
        )
        footer.pack(pady=(10, 0))

    def update_progress(self, value: float, status_msg: str):
        self.progress_var.set(value)
        self.progress_bar.configure(text=f"{int(value)}%")
        self.status_var.set(status_msg)
        
        # Log the message
        level = "info"
        if "Erro" in status_msg:
            level = "error"
        elif "Sucesso" in status_msg:
            level = "success"
        
        self.log_view.log(status_msg, level)

    def set_selected_path(self, path: str):
        self.selected_path_var.set(path)

    def set_start_button_state(self, enabled: bool):
        state = NORMAL if enabled else DISABLED
        self.start_btn.configure(state=state)
