import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
import threading
import sys
import os
import pdf_translator


# ─────────────────────────────────────────────
# REDIRECIONAR PRINT
# ─────────────────────────────────────────────
class RedirectOutput:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert("end", message)
        self.text_widget.see("end")

    def flush(self):
        pass


# ─────────────────────────────────────────────
# AÇÕES
# ─────────────────────────────────────────────
def escolher_pdf(entry):
    caminho = filedialog.askopenfilename(
        title="Selecionar PDF",
        filetypes=[("PDF", "*.pdf")]
    )
    if caminho:
        entry.delete(0, "end")
        entry.insert(0, caminho)


def executar_traducao(entry, btn, progress, status):
    caminho_pdf = entry.get()

    if not caminho_pdf or not os.path.exists(caminho_pdf):
        messagebox.showerror("Erro", "Selecione um PDF válido.")
        return

    caminho_saida = os.path.splitext(caminho_pdf)[0] + "_traduzido.txt"

    def tarefa():
        try:
            btn.config(state=DISABLED)
            progress.start()
            status.config(text="🔄 Processando...")

            print("📄 Lendo PDF...")
            paginas = pdf_translator.ler_pdf(caminho_pdf)

            resultado = []

            for pg in paginas:
                print(f"\n── Página {pg['pagina']} ──")

                texto_limpo = pdf_translator.limpar_texto(pg["texto"])

                if not texto_limpo:
                    print("(sem texto)")
                    resultado.append({**pg, "texto_traduzido": "[sem texto]"})
                    continue

                blocos = pdf_translator.dividir_em_blocos(texto_limpo)
                traducoes = pdf_translator.traduzir_blocos(blocos)

                resultado.append({
                    **pg,
                    "texto_traduzido": "\n\n".join(traducoes)
                })

            print("\n💾 Salvando...")
            pdf_translator.salvar_resultado(resultado, caminho_saida)

            print("\n✅ Finalizado!")
            status.config(text="✅ Concluído")

            messagebox.showinfo("Sucesso", "Tradução concluída!")

        except Exception as e:
            messagebox.showerror("Erro", str(e))
            status.config(text="❌ Erro")

        finally:
            progress.stop()
            btn.config(state=NORMAL)

    threading.Thread(target=tarefa).start()


# ─────────────────────────────────────────────
# GUI
# ─────────────────────────────────────────────
def criar_interface():
    app = ttk.Window(themename="superhero")  # 🔥 tema bonito
    app.title("Tradutor de PDF")
    app.geometry("800x600")

    container = ttk.Frame(app, padding=20)
    container.pack(fill=BOTH, expand=True)

    # ── HEADER ───────────────────────────────
    ttk.Label(
        container,
        text="📄 Tradutor de PDF",
        font=("Segoe UI", 20, "bold")
    ).pack(anchor="center", pady=(0, 10))

    ttk.Label(
        container,
        text="Traduza PDFs automaticamente para texto",
        font=("Segoe UI", 10)
    ).pack(anchor="center", pady=(0, 20))

    # ── CARD ────────────────────────────────
    card = ttk.Frame(container, padding=15, bootstyle="secondary")
    card.pack(fill=X, pady=10)

    ttk.Label(card, text="Arquivo PDF:", font=("Segoe UI", 10, "bold")).pack(anchor="w")

    row = ttk.Frame(card)
    row.pack(fill=X, pady=5)

    entry = ttk.Entry(row)
    entry.pack(side=LEFT, fill=X, expand=True, padx=(0, 5))

    ttk.Button(
        row,
        text="📂",
        width=3,
        bootstyle=PRIMARY,
        command=lambda: escolher_pdf(entry)
    ).pack(side=LEFT)

    # ── BOTÃO ───────────────────────────────
    btn = ttk.Button(
        container,
        text="🚀 Iniciar Tradução",
        bootstyle="success-outline",
        width=25
    )
    btn.pack(pady=10)

    # ── PROGRESSO ───────────────────────────
    progress = ttk.Progressbar(container, mode="indeterminate")
    progress.pack(fill=X, pady=5)

    status = ttk.Label(container, text="⏳ Aguardando...", font=("Segoe UI", 9))
    status.pack(anchor="center", pady=(0, 10))

    # ── LOG ─────────────────────────────────
    log_frame = ttk.Frame(container)
    log_frame.pack(fill=BOTH, expand=True)

    text = ttk.Text(
        log_frame,
        wrap="word",
        font=("Consolas", 10),
        height=15
    )
    text.pack(fill=BOTH, expand=True)

    # redireciona print
    sys.stdout = RedirectOutput(text)
    sys.stderr = RedirectOutput(text)

    # conecta botão
    btn.config(command=lambda: executar_traducao(entry, btn, progress, status))

    return app


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
if __name__ == "__main__":
    app = criar_interface()
    app.mainloop()
