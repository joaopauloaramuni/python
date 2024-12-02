# Projeto PdfCompressor

O **PdfCompressor** é um projeto para comprimir arquivos PDF utilizando a ferramenta **Ghostscript**. Ele permite ajustar a qualidade e a resolução das imagens dentro do PDF, proporcionando um equilíbrio entre qualidade visual e tamanho reduzido do arquivo. Este projeto é útil para reduzir o tamanho de arquivos PDF para compartilhamento ou armazenamento.

## Como funciona

O script utiliza o Ghostscript, uma poderosa ferramenta de processamento de PDF e PostScript, para recompactar imagens, ajustar a resolução e otimizar o conteúdo do PDF. Ele suporta diferentes níveis de qualidade e oferece flexibilidade para adequar o resultado às suas necessidades (leitura em tela, impressão ou publicação).

---

## Dependências

Para executar o projeto, é necessário instalar o **Ghostscript**. Siga as instruções abaixo para seu sistema operacional:

### Instalação do Ghostscript

#### **macOS (usando Homebrew):**
```bash
brew install ghostscript
```

#### **Linux (Debian/Ubuntu):**
```bash
sudo apt install ghostscript
```

#### **Windows:**
1. Baixe o instalador [aqui](https://ghostscript.com/).
2. Adicione o caminho do executável (`gswin64c.exe` ou `gswin32c.exe`) às variáveis de ambiente.

---

## O que é Ghostscript?

O **Ghostscript** é uma ferramenta de código aberto para manipulação de arquivos PDF e PostScript. Ele permite:
- Comprimir PDFs.
- Converter PDFs para outros formatos.
- Ajustar a resolução de imagens.
- Trabalhar com arquivos PostScript.

**Documentação oficial e links úteis:**
- [Página principal](https://www.ghostscript.com/)
- [Documentação oficial](https://www.ghostscript.com/documentation/index.html)
- [Ghostscript no ReadTheDocs](https://ghostscript.readthedocs.io/en/latest/)
- [Releases do Ghostscript](https://ghostscript.com/releases/gsdnld.html)

---

## Ambiente Virtual (venv)

### Passo 1: Criar e ativar o ambiente virtual

É recomendado criar um ambiente virtual para isolar as dependências do projeto. Para configurar o ambiente virtual:

1. **Criar o ambiente virtual**:
   ```bash
   python -m venv venv
   ```

2. **Ativar o ambiente virtual**:
   - No Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### Passo 2: Executar o script

Após ativar o ambiente virtual, execute o script principal:
```bash
python main.py
```

## Versão do Python

Este projeto foi desenvolvido na versão **3.13.0** do Python.

---

## Exemplo de Saída

Ao executar o script, você pode esperar uma saída como esta:

```
GPL Ghostscript 10.04.0 (2024-09-18)
Copyright (C) 2024 Artifex Software, Inc.  All rights reserved.
This software is supplied under the GNU AGPLv3 and comes with NO WARRANTY:
see the file COPYING for details.
Processing pages 1 through 242.
Page 1
...
Page 242
PDF comprimido salvo como: output_compressed.pdf
```

No exemplo acima, o arquivo `input.pdf` com tamanho de 19,92 MB foi reduzido para 7,61 MB no arquivo comprimido `output_compressed.pdf`.

---

## Explicação do Código

### 1. **`input_pdf` e `output_pdf`**
- **`input_pdf`**: Especifica o caminho para o arquivo PDF original que será comprimido.
- **`output_pdf`**: Define o caminho e o nome do arquivo comprimido que será gerado pelo script.

### 2. **`quality`**
- Define o nível de compressão e qualidade para o arquivo PDF, utilizando os parâmetros predefinidos do Ghostscript:
  - **`screen`**: Compressão máxima com qualidade baixa. Ideal para leitura em tela, mas imagens podem perder nitidez significativa.
  - **`ebook`**: Boa compressão com qualidade moderada. Um equilíbrio ideal para leitura e compartilhamento.
  - **`printer`**: Qualidade alta com menor compressão. Adequado para impressão doméstica ou comercial.
  - **`prepress`**: Qualidade muito alta com mínima compressão. Recomendado para publicações profissionais e gráficas.

### 3. **`dpi`**
- Especifica a resolução máxima das imagens dentro do PDF:
  - **72 DPI**: Compressão agressiva. As imagens podem parecer pixeladas, mas o tamanho do arquivo será muito reduzido.
  - **100-150 DPI**: Oferece um bom equilíbrio entre qualidade e tamanho do arquivo. Adequado para leitura em tela e impressão básica.
  - **300 DPI**: Alta resolução, ideal para impressão de qualidade. Aumenta significativamente o tamanho do arquivo.

### 4. **Parâmetros de Ghostscript**
- **`-sDEVICE=pdfwrite`**: Especifica que o dispositivo de saída será um arquivo PDF.
- **`-dCompatibilityLevel=1.4`**: Define a compatibilidade do PDF gerado com a versão 1.4 do padrão PDF, garantindo maior compatibilidade com leitores antigos.
- **`-dPDFSETTINGS=/{quality}`**: Aplica o nível de compressão definido por `quality`.
- **`-dColorImageResolution={dpi}`**: Define a resolução máxima das imagens coloridas.
- **`-dGrayImageResolution={dpi}`**: Define a resolução máxima das imagens em escala de cinza.
- **`-dMonoImageResolution={dpi}`**: Define a resolução máxima das imagens monocromáticas.
- **`-dDownsampleColorImages=true`**: Ativa a redução de resolução (downsampling) para imagens coloridas.
- **`-dDownsampleGrayImages=true`**: Ativa a redução de resolução para imagens em escala de cinza.
- **`-dDownsampleMonoImages=true`**: Ativa a redução de resolução para imagens monocromáticas.
- **`-dColorImageDownsampleType=/Bicubic`**: Usa o método de amostragem bicúbica para imagens coloridas, garantindo boa qualidade visual ao reduzir a resolução.
- **`-dGrayImageDownsampleType=/Bicubic`**: Usa o método de amostragem bicúbica para imagens em escala de cinza.
- **`-dMonoImageDownsampleType=/Bicubic`**: Usa o método de amostragem bicúbica para imagens monocromáticas.
- **`-dNOPAUSE`**: Remove pausas interativas no processamento do Ghostscript.
- **`-dBATCH`**: Garante que o processo será executado como um único lote sem interação do usuário.
- **`-sOutputFile={output_pdf}`**: Especifica o caminho e o nome do arquivo PDF gerado.

Com essas configurações, o Ghostscript processa o PDF para reduzir o tamanho ajustando a resolução e recompactando os recursos internos, garantindo flexibilidade para diferentes necessidades de qualidade e tamanho. 

---

## Licença

Este projeto está licenciado sob a Licença MIT.
