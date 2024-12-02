import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class PdfCompressorUI:
    def __init__(self, compress_pdf_with_ghostscript):
        self.compress_pdf_with_ghostscript = compress_pdf_with_ghostscript
        self.input_pdf = None
        self.janela = tk.Tk()
        self.janela.title("PdfCompressor with UI")
        self.janela.geometry("450x580")

        # Interface Elements
        tk.Label(self.janela, text="PdfCompressor with UI", font=("Helvetica", 16, "bold")).pack(pady=(20, 10))

        # Botão para selecionar arquivo PDF
        tk.Button(self.janela, text="Selecionar PDF", command=self.selecionar_pdf, width=15, padx=20, pady=10, bg="#4CAF50", fg="#FFFFFF").pack(pady=10)

        self.lbl_caminho = tk.Label(self.janela, text="Nenhum PDF selecionado", wraplength=400, fg="#555555", height=2, anchor="w", justify="left", font=("Helvetica", 12))
        self.lbl_caminho.pack(pady=5)

        # Configuração de DPI
        tk.Label(self.janela, text="Definir DPI:", font=("Helvetica", 12)).pack(pady=10)
        self.dpi_slider = tk.Scale(self.janela, from_=36, to=300, orient="horizontal", length=400)
        self.dpi_slider.set(120)
        self.dpi_slider.pack(pady=(5, 20))
        
        # Parâmetros adicionais
        self.downsample_color = tk.BooleanVar(value=True)
        self.downsample_gray = tk.BooleanVar(value=True)
        self.downsample_mono = tk.BooleanVar(value=True)

        tk.Checkbutton(self.janela, text="Reduzir resolução de imagens coloridas", variable=self.downsample_color).pack(anchor="w", padx=20)
        tk.Checkbutton(self.janela, text="Reduzir resolução de imagens em escala de cinza", variable=self.downsample_gray).pack(anchor="w", padx=20)
        tk.Checkbutton(self.janela, text="Reduzir resolução de imagens monocromáticas", variable=self.downsample_mono).pack(anchor="w", padx=20)

        # Configuração de qualidade
        tk.Label(self.janela, text="Qualidade:", font=("Helvetica", 12)).pack(pady=(20, 10))
        self.quality_combo = ttk.Combobox(self.janela, values=["screen", "ebook", "printer", "prepress"], state="readonly")
        self.quality_combo.set("ebook")
        self.quality_combo.pack(pady=(5, 20))

        # Botão para comprimir PDF
        tk.Button(self.janela, text="Comprimir PDF", command=self.comprimir_pdf, width=15, padx=20, pady=10, bg="#4CAF50", fg="#FFFFFF").pack(pady=10)

        # Adicionar um Label para exibir o resultado
        self.lbl_resultado = tk.Label(self.janela, text="Aguardando inserir PDF", wraplength=400, fg="#555555", height=2, anchor="w", justify="left", font=("Helvetica", 12))
        self.lbl_resultado.pack(pady=5)
        
    def selecionar_pdf(self):
        self.input_pdf = filedialog.askopenfilename(title="Selecione um PDF", filetypes=[("PDF Files", "*.pdf")])
        if self.input_pdf:
            self.lbl_caminho.config(text=self.input_pdf)
            self.lbl_resultado.config(text="PDF selecionado! Pressione 'Comprimir PDF' para continuar.", fg="#555555")

    def comprimir_pdf(self):
        if not self.input_pdf:
            self.lbl_resultado.config(text="Nenhum PDF selecionado! Por favor, insira um arquivo.", fg="red")
            messagebox.showwarning("Aviso", "Selecione um PDF primeiro!")
            return
        else:
            messagebox.showinfo("Informação", "A compressão pode levar alguns minutos a depender do tamanho do pdf. Clique em OK para iniciar a compressão.")

        dpi = self.dpi_slider.get()
        quality = self.quality_combo.get()
        output_pdf = self.input_pdf.replace(".pdf", "_compressed.pdf")
        # output_pdf = "output_compressed.pdf" 
        
        downsample_params = []
        if self.downsample_color.get():
            downsample_params.append("-dDownsampleColorImages=true")
        if self.downsample_gray.get():
            downsample_params.append("-dDownsampleGrayImages=true")
        if self.downsample_mono.get():
            downsample_params.append("-dDownsampleMonoImages=true")

        resultado = self.compress_pdf_with_ghostscript(self.input_pdf, output_pdf, quality, dpi, downsample_params)

        if "Erro" in resultado:
            self.lbl_resultado.config(text=resultado, fg="red")
            messagebox.showerror("Erro", resultado)
            print(f"Erro: {resultado}")  # Exibe a mensagem de erro no console
        else:
            self.lbl_resultado.config(text=resultado, fg="green")
            messagebox.showinfo("Sucesso", resultado)
            print(f"Sucesso: {resultado}")  # Exibe a mensagem de sucesso no console

    def iniciar(self):
        self.janela.mainloop()
