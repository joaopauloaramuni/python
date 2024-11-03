import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from PIL import ImageTk, Image
from app import gerar_imagem

# Variável global para armazenar a imagem
img = None


# Função para gerar a imagem e exibi-la na interface
def gerar_imagem_interface():
    global img
    prompt = entry_prompt.get()
    if not prompt or prompt == "Ex: Uma paisagem de montanhas ao amanhecer":
        messagebox.showwarning("Aviso", "Digite uma descrição para a imagem.")
        return
    img = gerar_imagem(prompt)
    if img:
        img_resized = img.resize(
            (300, 200)
        )  # Redimensionar a imagem para caber na interface
        img_tk = ImageTk.PhotoImage(img_resized)
        label_imagem.config(image=img_tk)
        label_imagem.image = img_tk  # Mantém referência para evitar garbage collector
        app.geometry("500x600")  # Diminuindo a altura da janela
        messagebox.showinfo("Sucesso", "Imagem gerada com sucesso!")


# Função para salvar a imagem
def salvar_imagem():
    if img:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png", filetypes=[("PNG Files", "*.png")]
        )
        if file_path:
            img.save(file_path)
            messagebox.showinfo("Sucesso", f"Imagem salva como '{file_path}'.")


# Configuração da interface
app = tk.Tk()
app.title("Gerador de Imagens")
app.geometry("500x400")  # Diminuindo a altura da janela
app.configure(bg="#e0f7fa")

# Adicionar um ícone (Certifique-se de ter o arquivo 'icon.ico' no mesmo diretório)
# icon_image_path = "C:/prj/icon.ico" # Para geração do .exe
app.iconbitmap("icon.ico")

# Carregar e exibir a logo (Certifique-se de ter o arquivo 'logo.png' no mesmo diretório)
# logo_image_path = "C:/prj/logo.png" # Para geração do .exe
logo_image = Image.open("logo.png")
logo_image = logo_image.resize((300, 80))  # Ajustar o tamanho da logo
logo_tk = ImageTk.PhotoImage(logo_image)
logo_label = ttk.Label(app, image=logo_tk, background="#e0f7fa")
logo_label.image = logo_tk  # Mantém referência para evitar garbage collector
logo_label.pack(pady=10)  # Ajuste o padding conforme necessário

# Título principal
title_label = ttk.Label(
    app, text="Gerador de Imagens", font=("Helvetica", 16, "bold"), background="#e0f7fa"
)
title_label.pack(pady=10)

# Campo de entrada de texto para o prompt
prompt_frame = ttk.Frame(app, padding="10 10 10 10", style="Card.TFrame")
prompt_frame.pack(pady=10)

# Rótulo para o campo de entrada
prompt_label = ttk.Label(
    prompt_frame,
    text="Descreva sua Imagem:",
    font=("Helvetica", 12, "bold"),
    background="#f0f4f8",
    foreground="#333",
)
prompt_label.grid(row=0, column=0, sticky="w")

# Estilizando o campo de entrada de texto
entry_prompt = ttk.Entry(
    prompt_frame,
    width=30,  # Diminuindo a largura do campo de entrada
    font=("Helvetica", 12),
    style="Modern.TEntry",
)
entry_prompt.grid(row=0, column=1, padx=10)

# Adicionando placeholder no campo de entrada
entry_prompt.insert(0, "Ex: Uma paisagem de montanhas ao amanhecer")  # Placeholder
entry_prompt.bind(
    "<FocusIn>",
    lambda event: (
        entry_prompt.delete(0, tk.END)
        if entry_prompt.get() == "Ex: Uma paisagem de montanhas ao amanhecer"
        else None
    ),
)
entry_prompt.bind(
    "<FocusOut>",
    lambda event: (
        entry_prompt.insert(0, "Ex: Uma paisagem de montanhas ao amanhecer")
        if entry_prompt.get() == ""
        else None
    ),
)

# Estilos customizados
style = ttk.Style()
style.configure(
    "Modern.TEntry",
    fieldbackground="#ffffff",
    bordercolor="#cccccc",
    relief="flat",
    bd=2,
)
style.map("Modern.TEntry", bordercolor=[("active", "#80bfff"), ("focus", "#40a0ff")])

# Frame para os botões "Gerar Imagem" e "Salvar Imagem"
frame_botoes = ttk.Frame(app)
frame_botoes.pack(pady=10)

# Botão para gerar a imagem
btn_gerar = tk.Button(
    frame_botoes,
    text="Gerar Imagem",
    command=gerar_imagem_interface,
    font=("Helvetica", 12, "bold"),
    bg="#ff5722",
    fg="white",
    activebackground="#e64a19",
    activeforeground="white",
)
btn_gerar.grid(row=0, column=0, padx=10, pady=10)

# Botão para salvar a imagem ao lado do botão "Gerar Imagem"
btn_salvar = tk.Button(
    frame_botoes,
    text="Salvar Imagem",
    command=salvar_imagem,
    font=("Helvetica", 12, "bold"),
    bg="#4caf50",
    fg="white",
    activebackground="#388e3c",
    activeforeground="white",
)
btn_salvar.grid(row=0, column=1, padx=10, pady=10)

# Label para exibir a imagem gerada
label_imagem = ttk.Label(app, background="#e0f7fa")
label_imagem.pack(pady=10)

# Rodapé
footer_label = ttk.Label(
    app,
    text="Criado por Aramuni",
    font=("Helvetica", 8, "italic"),
    background="#e0f7fa",
)
footer_label.pack(side="bottom", pady=10)

# Estilos do Frame
style.configure("Card.TFrame", background="#ffffff", borderwidth=1, relief="groove")

# Iniciar a interface
app.mainloop()
