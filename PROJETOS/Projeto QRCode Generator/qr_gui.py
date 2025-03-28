import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk
from qr_logic import QRCodeLogic

class QRCodeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de QR Code Personalizado")
        self.root.geometry("600x700")
        
        # Instância da lógica
        self.qr_logic = QRCodeLogic()

        # Variáveis para personalização
        self.qr_data = tk.StringVar()
        self.fill_color = tk.StringVar(value="black")
        self.back_color = tk.StringVar(value="white")
        self.qr_size = tk.IntVar(value=10)
        self.image_path = None

        # Interface
        self.create_widgets()

    def create_widgets(self):
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)

        # Entrada de dados
        tk.Label(main_frame, text="Digite o texto/URL para o QR Code:").pack()
        tk.Entry(main_frame, textvariable=self.qr_data, width=50).pack(pady=5)

        # Seleção de cores
        color_frame = tk.Frame(main_frame)
        color_frame.pack(pady=10)
        
        tk.Label(color_frame, text="Cor do QR:").grid(row=0, column=0, padx=5)
        tk.Entry(color_frame, textvariable=self.fill_color, width=10).grid(row=0, column=1)
        
        tk.Label(color_frame, text="Cor de fundo:").grid(row=0, column=2, padx=5)
        tk.Entry(color_frame, textvariable=self.back_color, width=10).grid(row=0, column=3)

        # Tamanho
        tk.Label(main_frame, text="Tamanho (1-40):").pack()
        tk.Scale(main_frame, from_=1, to=40, orient="horizontal", 
                variable=self.qr_size).pack()

        # Botão para adicionar imagem
        tk.Button(main_frame, text="Adicionar Imagem (opcional)", 
                 command=self.load_image).pack(pady=5)

        # Botões de ação
        tk.Button(main_frame, text="Gerar QR Code", 
                 command=self.generate_qr).pack(pady=10)
        tk.Button(main_frame, text="Salvar QR Code", 
                 command=self.save_qr).pack()

        # Área de visualização
        self.preview_label = tk.Label(main_frame)
        self.preview_label.pack(pady=10)

    def load_image(self):
        self.image_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
        )
        if self.image_path:
            messagebox.showinfo("Sucesso", "Imagem carregada com sucesso!")

    def generate_qr(self):
        try:
            qr_img = self.qr_logic.generate_qr(
                data=self.qr_data.get(),
                fill_color=self.fill_color.get(),
                back_color=self.back_color.get(),
                box_size=self.qr_size.get(),
                image_path=self.image_path
            )
            self.show_preview(qr_img)
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def show_preview(self, img):
        photo = ImageTk.PhotoImage(img)
        self.preview_label.configure(image=photo)
        self.preview_label.image = photo  # Manter referência

    def save_qr(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        if file_path:
            if self.qr_logic.save_qr(file_path):
                messagebox.showinfo("Sucesso", "QR Code salvo com sucesso!")
            else:
                messagebox.showwarning("Aviso", "Gere um QR Code primeiro!")
