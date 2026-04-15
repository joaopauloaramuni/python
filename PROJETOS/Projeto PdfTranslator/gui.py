import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import threading
import sys
import os
import pdf_translator


# ─────────────────────────────────────────────
# REDIRECIONAR PRINT PARA TEXTAREA
# ─────────────────────────────────────────────

class RedirectOutput:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)
        self.text_widget.update_idletasks()

    def flush(self):
        pass


# ─────────────────────────────────────────────
# AÇÕES
# ─────────────────────────────────────────────

def escolher_pdf(entry_path):
    caminho = filedialog.askopenfilename(
        title="Selecionar PDF",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )
    if caminho:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, caminho)


def executar_traducao(entry_path, text_output, btn_traduzir):
    caminho_pdf = entry_path.get()

    if not caminho_pdf or not os.path.exists(caminho_pdf):
        messagebox.showerror("Erro", "Selecione um PDF válido.")
        return

    # define saída no mesmo diretório
    caminho_saida = os.path.splitext(caminho_pdf)[0] + "_traduzido.txt"

    def tarefa():
        try:
            btn_traduzir.config(state=tk.DISABLED)

            print("📄 Lendo PDF...")
            paginas = pdf_translator.ler_pdf(caminho_pdf)
            print(f"{len(paginas)} página(s) encontrada(s).")

            resultado = []

            for pg in paginas:
                print(f"\n── Página {pg['pagina']} ──────────────────────────────")

                texto_limpo = pdf_translator.limpar_texto(pg["texto"])

                if not texto_limpo:
                    print("(página sem texto — pulando)")
                    resultado.append({**pg, "texto_traduzido": "[imagem / sem texto]"})
                    continue

                blocos = pdf_translator.dividir_em_blocos(texto_limpo)
                print(f"{len(blocos)} bloco(s) para traduzir.")

                traducoes = pdf_translator.traduzir_blocos(blocos)
                texto_traduzido = "\n\n".join(traducoes)

                resultado.append({**pg, "texto_traduzido": texto_traduzido})

            print("\n💾 Salvando resultado...")
            pdf_translator.salvar_resultado(resultado, caminho_saida)

            print(f"\n✅ Concluído! Arquivo salvo em:\n{caminho_saida}")

            messagebox.showinfo("Sucesso", "Tradução concluída!")

        except Exception as e:
            messagebox.showerror("Erro", str(e))
        finally:
            btn_traduzir.config(state=tk.NORMAL)

    threading.Thread(target=tarefa).start()


# ─────────────────────────────────────────────
# GUI
# ─────────────────────────────────────────────

def criar_interface():
    root = tk.Tk()
    root.title("Tradutor de PDF")
    root.geometry("700x500")

    # ── Frame topo ────────────────────────────
    frame_top = tk.Frame(root)
    frame_top.pack(fill=tk.X, padx=10, pady=10)

    entry_path = tk.Entry(frame_top)
    entry_path.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

    btn_arquivo = tk.Button(
        frame_top,
        text="Selecionar PDF",
        command=lambda: escolher_pdf(entry_path)
    )
    btn_arquivo.pack(side=tk.LEFT)

    # ── Botão traduzir ────────────────────────
    btn_traduzir = tk.Button(
        root,
        text="Traduzir e Gerar TXT",
        height=2
    )
    btn_traduzir.pack(fill=tk.X, padx=10, pady=5)

    # ── Área de saída ─────────────────────────
    text_output = scrolledtext.ScrolledText(root, wrap=tk.WORD)
    text_output.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # redireciona print()
    sys.stdout = RedirectOutput(text_output)
    sys.stderr = RedirectOutput(text_output)

    # conecta botão
    btn_traduzir.config(
        command=lambda: executar_traducao(entry_path, text_output, btn_traduzir)
    )

    return root


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    app = criar_interface()
    app.mainloop()


if __name__ == "__main__":
    main()