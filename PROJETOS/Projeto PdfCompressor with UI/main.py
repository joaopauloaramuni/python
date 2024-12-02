import subprocess
from interface import PdfCompressorUI

def compress_pdf_with_ghostscript(input_pdf, output_pdf, quality, dpi, downsample_params):
    """
    Função para comprimir PDF utilizando Ghostscript.
    """
    try:
        command = [
            "gs",
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            f"-dPDFSETTINGS=/{quality}",
            "-dNOPAUSE",
            "-dBATCH",
            f"-sOutputFile={output_pdf}",
            f"-dColorImageResolution={dpi}",
            f"-dGrayImageResolution={dpi}",
            f"-dMonoImageResolution={dpi}",
        ] + downsample_params + [input_pdf]

        subprocess.run(command, check=True)
        return f"PDF comprimido salvo em: {output_pdf}"
    except Exception as e:
        return f"Erro ao comprimir o PDF: {e}"

if __name__ == "__main__":
    app = PdfCompressorUI(compress_pdf_with_ghostscript)
    app.iniciar()
