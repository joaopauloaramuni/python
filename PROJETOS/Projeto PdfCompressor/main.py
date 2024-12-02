import subprocess

def compress_pdf_with_ghostscript(input_pdf, output_pdf, quality="ebook", dpi=120):
    """
    Comprime um PDF usando Ghostscript, preservando qualidade das imagens.

    :param input_pdf: Caminho para o PDF original.
    :param output_pdf: Caminho para salvar o PDF comprimido.
    :param quality: Nível de qualidade ('screen', 'ebook', 'printer', 'prepress').
    :param dpi: Resolução máxima (DPI) para imagens no PDF.
    """
    try:
        # Comando do Ghostscript para compressão com foco em qualidade
        command = [
            "gs",  # No Windows, substitua por "gswin64c" ou "gswin32c"
            "-sDEVICE=pdfwrite",  # Define o dispositivo de saída como PDF
            "-dCompatibilityLevel=1.4",  # Define a compatibilidade com PDF 1.4
            f"-dPDFSETTINGS=/{quality}",  # Configura o nível de compressão
            "-dNOPAUSE",  # Evita pausas interativas
            "-dBATCH",  # Processa o arquivo sem interações
            f"-sOutputFile={output_pdf}",  # Define o arquivo de saída
            f"-dColorImageResolution={dpi}",  # Define resolução para imagens coloridas
            f"-dGrayImageResolution={dpi}",   # Define resolução para imagens em escala de cinza
            f"-dMonoImageResolution={dpi}",   # Define resolução para imagens monocromáticas
            "-dDownsampleColorImages=true",  # Ativa redução de resolução para imagens coloridas
            "-dDownsampleGrayImages=true",   # Ativa redução de resolução para imagens em escala de cinza
            "-dDownsampleMonoImages=true",   # Ativa redução de resolução para imagens monocromáticas
            "-dColorImageDownsampleType=/Bicubic",  # Método de amostragem de alta qualidade para imagens coloridas
            "-dGrayImageDownsampleType=/Bicubic",   # Método de amostragem para imagens em escala de cinza
            "-dMonoImageDownsampleType=/Bicubic",   # Método de amostragem para imagens monocromáticas
            input_pdf  # Arquivo PDF de entrada
        ]
        
        # Executa o comando do Ghostscript
        subprocess.run(command, check=True)
        print(f"PDF comprimido salvo como: {output_pdf}")
    except Exception as e:
        # Trata erros de execução
        print(f"Erro ao comprimir o PDF com Ghostscript: {e}")


def main():
    """
    Função principal que configura os caminhos de entrada/saída
    e chama a função de compressão.
    """
    # Caminho do arquivo PDF de entrada
    input_pdf = "input.pdf"  # Substitua pelo caminho do arquivo original

    # Caminho do arquivo PDF de saída
    output_pdf = "output_compressed.pdf"  # Substitua pelo caminho do arquivo comprimido

    # Configurações de compressão

    # Define o nível de qualidade para compressão do PDF
    # 'screen': Qualidade baixa, compressão máxima, ideal para leitura em tela com tamanho reduzido. 
    #           Imagens podem perder nitidez significativa (ruim para impressão).
    # 'ebook': Qualidade moderada, boa para leitura em tela e compartilhamento. Equilíbrio entre qualidade e tamanho.
    # 'printer': Qualidade alta, bom para impressão padrão, mas o tamanho do arquivo aumenta.
    # 'prepress': Qualidade muito alta, quase sem compressão. Recomendado para publicações profissionais. 
    #             Gera arquivos maiores com ótima fidelidade.
    quality = "ebook"

    # Define o DPI (resolução) para imagens dentro do PDF
    # DPI muito baixo (ex: 72): Compressão agressiva, imagens podem ficar pixeladas.
    # DPI médio (ex: 100-150): Boa qualidade para leitura em tela e impressão básica (equilíbrio recomendado).
    # DPI alto (ex: 300): Alta qualidade, imagens muito nítidas, ideal para impressão (maior tamanho do arquivo).
    dpi = 120  # Resolução ajustada para equilíbrio entre qualidade e tamanho

    # Chama a função de compressão
    compress_pdf_with_ghostscript(input_pdf, output_pdf, quality=quality, dpi=dpi)


# Executa a função principal se o script for chamado diretamente
if __name__ == "__main__":
    main()

# brew install ghostscript