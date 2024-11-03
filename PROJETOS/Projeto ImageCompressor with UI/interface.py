import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import font


class CompressorInterface:
    def __init__(self, funcao_comprimir):
        self.funcao_comprimir = funcao_comprimir
        self.caminho_arquivo = None

        # Criação da janela principal com título e dimensões
        self.janela = tk.Tk()
        self.janela.title("Compressor de Imagens")
        self.janela.geometry("550x400")
        self.janela.config(bg="#f0f4f8")

        # Estilos de fonte e cores
        fonte_titulo = font.Font(family="Helvetica", size=16, weight="bold")
        fonte_texto = font.Font(family="Helvetica", size=12)
        cor_botao = "#4CAF50"
        cor_texto_botao = "#FFFFFF"

        # Título da interface
        self.lbl_titulo = tk.Label(
            self.janela,
            text="Compressor de Imagens",
            font=fonte_titulo,
            bg="#f0f4f8",
            fg="#333333",
        )
        self.lbl_titulo.pack(pady=(10, 20))

        # Botão para selecionar a imagem
        self.btn_selecionar = tk.Button(
            self.janela,
            text="Selecionar Imagem",
            command=self.selecionar_arquivo,
            bg=cor_botao,
            fg=cor_texto_botao,
            font=fonte_texto,
            relief="flat",
            padx=20,
            pady=10,
        )
        self.btn_selecionar.pack(pady=5)

        # Rótulo para exibir o caminho do arquivo selecionado
        self.lbl_caminho = tk.Label(
            self.janela,
            text="Nenhuma imagem selecionada",
            wraplength=400,
            bg="#e0e6ed",
            fg="#555555",
            font=fonte_texto,
            padx=10,
            pady=10,
            relief="groove",
        )
        self.lbl_caminho.pack(pady=10)

        # Rótulo e barra deslizante para ajustar a qualidade da imagem
        self.lbl_qualidade = tk.Label(
            self.janela,
            text="Qualidade da Imagem:",
            bg="#f0f4f8",
            fg="#333333",
            font=fonte_texto,
        )
        self.lbl_qualidade.pack(pady=(10, 0))

        self.escala_qualidade = tk.Scale(
            self.janela,
            from_=1,
            to=100,
            orient="horizontal",
            font=fonte_texto,
            length=300,
            troughcolor="#4CAF50",
            activebackground="#81C784",
            bg="#f0f4f8",
            fg="#333333",
        )
        self.escala_qualidade.set(75)  # Define valor inicial como 75
        self.escala_qualidade.pack(pady=5)

        # Botão para comprimir a imagem
        self.btn_comprimir = tk.Button(
            self.janela,
            text="Comprimir Imagem",
            command=self.comprimir_imagem,
            bg=cor_botao,
            fg=cor_texto_botao,
            font=fonte_texto,
            relief="flat",
            padx=20,
            pady=10,
        )
        self.btn_comprimir.pack(pady=(20, 10))

    def selecionar_arquivo(self):
        # Abre uma janela para selecionar o arquivo e exibe o caminho selecionado
        self.caminho_arquivo = filedialog.askopenfilename(
            title="Selecione uma imagem", filetypes=[("Imagens", "*.jpg *.jpeg *.png")]
        )
        if self.caminho_arquivo:
            self.lbl_caminho.config(text=self.caminho_arquivo)

    def comprimir_imagem(self):
        # Obtém o valor da qualidade da barra deslizante
        qualidade = self.escala_qualidade.get()

        if self.caminho_arquivo:
            resultado = self.funcao_comprimir(self.caminho_arquivo, qualidade)
            if "Erro" in resultado:
                messagebox.showerror("Erro", resultado)
            else:
                resultado_corrigido = resultado.replace("\\", "/")
                messagebox.showinfo(
                    "Sucesso", f"Imagem comprimida salva em:\n{resultado_corrigido}"
                )
        else:
            messagebox.showwarning("Aviso", "Selecione uma imagem primeiro.")

    def iniciar(self):
        self.janela.mainloop()
