import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
from tkinter import font
from pathlib import Path
import threading
from zipfile import ZipFile, BadZipFile
from tqdm import tqdm

class ZipCrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ZIP Password Cracker")
        self.root.geometry("550x300")
        self.root.resizable(False, False)

        self.word_list_path = None
        self.zip_file_path = None
        self.stop_flag = False

        # Frame principal
        frame = tk.Frame(root, padx=20, pady=20)
        frame.pack(fill='both', expand=True)

        # Font mono para exibir senhas/paths
        mono_font = font.Font(family="Courier", size=12)

        # Botões de seleção e iniciar
        self.btn_wordlist = tk.Button(frame, text="Selecionar Wordlist", font=mono_font, command=self.select_wordlist)
        self.btn_zip = tk.Button(frame, text="Selecionar ZIP", font=mono_font, command=self.select_zip)
        self.start_button = tk.Button(frame, text="Iniciar", font=mono_font, command=self.start_cracking_thread, state='disabled')

        # Barra de progresso e label de resultado
        self.progress = Progressbar(frame, mode='determinate')
        self.result_label = tk.Label(frame, text="", font=mono_font, width=60, anchor='w', justify="left", wraplength=500)

        # Posicionando widgets
        self.btn_wordlist.pack(fill='x', pady=5)
        self.btn_zip.pack(fill='x', pady=5)
        self.start_button.pack(fill='x', pady=5)
        self.progress.pack(fill='x', pady=10)
        self.result_label.pack(fill='x', pady=10)

    def select_wordlist(self):
        path = filedialog.askopenfilename(title="Selecionar Wordlist")
        if path:
            self.word_list_path = Path(path)
            self.result_label.config(text=f"Wordlist selecionada: {self.word_list_path.name}")
        self.check_start_ready()

    def select_zip(self):
        path = filedialog.askopenfilename(title="Selecionar ZIP", filetypes=[("ZIP files", "*.zip")])
        if path:
            self.zip_file_path = Path(path)
            self.result_label.config(text=f"ZIP selecionado: {self.zip_file_path.name}")
        self.check_start_ready()

    def check_start_ready(self):
        if self.word_list_path and self.zip_file_path:
            self.start_button.config(state='normal')
        else:
            self.start_button.config(state='disabled')

    def start_cracking_thread(self):
        # desativa botão e inicia thread
        self.start_button.config(state='disabled')
        self.stop_flag = False
        threading.Thread(target=self.crack_zip_password, daemon=True).start()

    def crack_zip_password(self):
        # valida existência
        if not (self.word_list_path and self.zip_file_path):
            messagebox.showerror("Erro", "Selecione a wordlist e o arquivo ZIP antes de iniciar.")
            self.start_button.config(state='normal')
            return

        try:
            zip_file = ZipFile(self.zip_file_path)
        except BadZipFile:
            messagebox.showerror("Erro", "O arquivo selecionado não é um ZIP válido.")
            self.start_button.config(state='normal')
            return
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao abrir ZIP: {e}")
            self.start_button.config(state='normal')
            return

        # contar palavras (modo binário)
        try:
            with open(self.word_list_path, 'rb') as f:
                n_words = sum(1 for _ in f)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao ler wordlist: {e}")
            self.start_button.config(state='normal')
            return

        # imprime total como no padrão
        print('[2] Total de senhas a testar:', f'{n_words:,}')

        # define máximo da progressbar (padrão seguido)
        self.progress['maximum'] = n_words
        self.progress['value'] = 0

        if n_words == 0:
            messagebox.showwarning("Aviso", "Wordlist vazia.")
            self.start_button.config(state='normal')
            return

        found = False
        try:
            with open(self.word_list_path, 'rb') as wordlist:
                for i, word in enumerate(tqdm(wordlist, total=n_words, unit='word')):
                    if self.stop_flag:
                        break

                    password = word.strip().decode(errors="ignore")  # segue o padrão: decode com errors="ignore"

                    display_password = password[:18].ljust(18)

                    # atualizar progresso GUI (valor do Progressbar)
                    self.progress['value'] = i + 1

                    # calcular porcentagem
                    percent = (i + 1) / n_words * 100

                    # atualizar label com largura fixa para a senha testada
                    self.result_label.config(
                        text=f"Testando senha: {display_password} | {i+1:,}/{n_words:,} ({percent:.2f}%)"
                    )
                    self.root.update_idletasks()

                    try:
                        # zipfile expects a bytes password
                        zip_file.extractall(pwd=word.strip())
                    except RuntimeError:
                        # senha incorreta (algumas versões do Python levantam RuntimeError)
                        pass
                    except Exception:
                        # erro genérico -> tratamos como falha na senha e continuamos
                        pass
                    else:
                        # sucesso!
                        found = True
                        self.result_label.config(text=f"✅ Senha encontrada: {password}")
                        print(f"\n[+] Senha encontrada: {password}")
                        messagebox.showinfo("Senha encontrada", f"Senha: {password}")
                        return

        finally:
            # sempre reabilitar o botão quando terminar/parar
            self.start_button.config(state='normal')

        if not found and not self.stop_flag:
            self.result_label.config(text="❌ Senha não encontrada. Tente outra wordlist.")
            print("\n[!] Senha não encontrada. Tente com outra wordlist.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ZipCrackerApp(root)
    root.mainloop()

# pip install tqdm
