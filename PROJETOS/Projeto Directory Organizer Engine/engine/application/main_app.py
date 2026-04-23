import logging
import threading
from tkinter import filedialog, messagebox
from engine.ui.app_ui import OrganizerWindow
from engine.service.organizer_service import OrganizerService

class MainApplication:
    def __init__(self):
        self.service = OrganizerService()
        self.window = OrganizerWindow(
            on_select_folder=self.handle_select_folder,
            on_start=self.handle_start_organization
        )
        self.selected_folder = None

    def handle_select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.selected_folder = folder
            self.window.set_selected_path(folder)
            self.window.log_view.log(f"Pasta selecionada: {folder}")
            self.window.set_start_button_state(True)

    def handle_start_organization(self):
        if not self.selected_folder:
            messagebox.showwarning("Aviso", "Por favor, selecione uma pasta primeiro.")
            return

        # Prepare UI for processing
        self.window.set_start_button_state(False)
        self.window.progress_var.set(0)
        self.window.log_view.clear()
        self.window.log_view.log("Iniciando organização...")

        # Run organization in a separate thread to keep UI interactive
        thread = threading.Thread(
            target=self._run_organization,
            args=(self.selected_folder,),
            daemon=True
        )
        thread.start()

    def _run_organization(self, folder_path: str):
        try:
            success = self.service.organize_directory(
                folder_path, 
                progress_callback=self.window.update_progress
            )
            
            if success:
                # Use after() to show messagebox from main thread (Tkinter requirement)
                self.window.after(0, lambda: messagebox.showinfo(
                    "Concluído", 
                    "A organização foi finalizada com sucesso!"
                ))
                logging.info("A organização foi finalizada com sucesso!")
            else:
                self.window.after(0, lambda: messagebox.showerror(
                    "Erro", 
                    "Não foi possível completar a organização. Verifique os logs."
                ))
                logging.error("Não foi possível completar a organização. Verifique os logs.")
                
        except Exception as e:
            self.window.after(0, lambda e=e: self.window.update_progress(0, f"Erro crítico: {str(e)}"))
            self.window.after(0, lambda e=e: messagebox.showerror("Erro Crítico", str(e)))
        finally:
            self.window.after(0, lambda: self.window.set_start_button_state(True))

    def run(self):
        self.window.mainloop()
