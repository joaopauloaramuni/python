import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
from tkinter import font
from pathlib import Path
import threading
import pikepdf
from tqdm import tqdm

class PDFCrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Password Cracker")
        self.root.geometry("550x300")
        self.root.resizable(False, False)

        self.word_list_path = None
        self.pdf_file_path = None

        # Frame principal
        frame = tk.Frame(root, padx=20, pady=20)
        frame.pack(fill='both', expand=True)

        # Botões de seleção
        mono_font = font.Font(family="Courier", size=12)
        self.btn_wordlist = tk.Button(frame, text="Selecionar Wordlist", font=mono_font, command=self.select_wordlist)
        self.btn_pdf = tk.Button(frame, text="Selecionar PDF", font=mono_font, command=self.select_pdf)
        self.start_button = tk.Button(frame, text="Iniciar", font=mono_font, command=self.start_cracking_thread, state='disabled')
        self.progress = Progressbar(frame, mode='determinate')
        self.result_label = tk.Label(frame, text="", font=mono_font, width=60, anchor='w', justify="left", wraplength=500)

        # Posicionando widgets
        self.btn_wordlist.pack(fill='x', pady=5)
        self.btn_pdf.pack(fill='x', pady=5)
        self.start_button.pack(fill='x', pady=5)
        self.progress.pack(fill='x', pady=10)
        self.result_label.pack(fill='x', pady=10)

    def select_wordlist(self):
        path = filedialog.askopenfilename(title="Selecionar Wordlist")
        if path:
            self.word_list_path = Path(path)
            self.result_label.config(text=f"Wordlist selecionada: {self.word_list_path.name}")
        self.check_start_ready()

    def select_pdf(self):
        path = filedialog.askopenfilename(title="Selecionar PDF", filetypes=[("PDF files", "*.pdf")])
        if path:
            self.pdf_file_path = Path(path)
            self.result_label.config(text=f"PDF selecionado: {self.pdf_file_path.name}")
        self.check_start_ready()

    def check_start_ready(self):
        if self.word_list_path and self.pdf_file_path:
            self.start_button.config(state='normal')
        else:
            self.start_button.config(state='disabled')

    def start_cracking_thread(self):
        self.start_button.config(state='disabled')
        threading.Thread(target=self.crack_pdf_password, daemon=True).start()

    def crack_pdf_password(self):
        with open(self.word_list_path, 'rb') as f:
            n_words = sum(1 for _ in f)
        print('[2] Total de senhas a testar:', f'{n_words:,}')

        self.progress['maximum'] = n_words

        with open(self.word_list_path, 'rb') as wordlist:
            for i, word in enumerate(tqdm(wordlist, total=n_words, unit='word')):
                password = word.strip().decode(errors="ignore")
                try:
                    with pikepdf.open(self.pdf_file_path, password=password):
                        self.result_label.config(text=f"✅ Senha encontrada: {password}")
                        print(f"\n[+] Senha encontrada: {password}")
                        return
                except pikepdf.PasswordError:
                    self.progress['value'] = i + 1
                    percent = (i + 1) / n_words * 100
                    display_password = password[:18].ljust(18)
                    self.result_label.config(
                        text=f"Testando senha: {display_password} | {i+1:,}/{n_words:,} ({percent:.2f}%)"
                    )
                    self.root.update_idletasks()

        self.result_label.config(text="❌ Senha não encontrada. Tente outra wordlist.")
        print("\n[!] Senha não encontrada. Tente com outra wordlist.")
        self.start_button.config(state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFCrackerApp(root)
    root.mainloop()
