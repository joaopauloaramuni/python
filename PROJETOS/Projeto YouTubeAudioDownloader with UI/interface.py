import tkinter as tk


def create_interface(start_download):
    """
    Cria a interface gráfica.

    :param start_download: Função para iniciar o download.
    """
    def reset_ui():
        """Reseta a interface após o download."""
        url_entry.delete(0, tk.END)
        download_button.config(state=tk.NORMAL)
        # update_status("Aguardando URL...", "green")  # Define o status inicial após o reset

    def handle_download():
        """Valida a entrada e inicia o download."""
        url = url_entry.get().strip()
        if not url:
            update_status("Por favor, insira uma URL válida!", "red")
            tk.messagebox.showerror("Erro", "Por favor, insira uma URL válida!")
            return

        download_button.config(state=tk.DISABLED)
        update_status("Baixando...", "green")
        start_download(url, update_status, reset_ui)

    def update_status(message, color):
        """Atualiza o rótulo de status com mensagem e cor."""
        status_label.config(text=message, fg=color)

    # Configuração da janela principal
    root = tk.Tk()
    root.title("YouTube Audio Downloader")

    # Define as dimensões da janela (levemente mais largas que o campo de texto)
    window_width = 600
    window_height = 180
    root.geometry(f"{window_width}x{window_height}")
    root.resizable(False, False)

    # Centralizar os elementos na janela
    container = tk.Frame(root, width=window_width, height=window_height)
    container.pack_propagate(False)
    container.pack()

    # Campo de entrada para a URL
    tk.Label(container, text="URL do vídeo:").pack(pady=5)
    url_entry = tk.Entry(container, width=48)
    url_entry.pack(pady=5)

    # Botão para iniciar o download
    download_button = tk.Button(container, text="Download", command=handle_download)
    download_button.pack(pady=10)

    # Rótulo para exibir o status inicial
    status_label = tk.Label(container, text="Aguardando URL...", fg="green")
    status_label.pack(pady=5)

    # Iniciar a interface
    root.mainloop()
