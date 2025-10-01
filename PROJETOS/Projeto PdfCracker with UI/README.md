# Projeto PdfCracker with UI

PdfCracker é uma ferramenta simples para tentativa de quebra de senha de arquivos PDF protegidos utilizando uma wordlist. Este projeto foi desenvolvido com Python, empregando as bibliotecas `pikepdf`, `tqdm` e `tkinter`.

## Funcionalidades

- Testa cada senha de uma wordlist para abrir um arquivo PDF protegido.
- Interface gráfica amigável utilizando **Tkinter**.
- Exibe progresso em tempo real com barra de progresso.
- Relata a senha encontrada ou notifica que nenhuma senha foi eficaz.
- Mostra a senha sendo testada em tempo real.

## Pré-requisitos

- Python 3.7 ou superior.
- Instalar as dependências necessárias:
  ```bash
  pip install tqdm pikepdf
  ```
- Baixar uma wordlist como o `rockyou.txt`.

## Ambiente virtual

1. **Crie o ambiente virtual:**
```bash
python -m venv .venv
```

2. **Ative o ambiente virtual:**

- **Windows:**
```bash
.venv\Scripts\activate
```

- **Linux/macOS:**
```bash
source .venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install tqdm pikepdf
```

## Dependências

### 1. `tqdm`
- **O que é**: A biblioteca `tqdm` é usada para exibir uma barra de progresso enquanto o código está testando as senhas. Isso facilita o acompanhamento do progresso, especialmente quando se trabalha com listas grandes de senhas.
- **Instalação**:
  ```
  pip install tqdm
  ```
### 2. `pikepdf`
- **O que é**: A biblioteca `pikepdf` permite ler, manipular e escrever arquivos PDF em Python. No contexto de testes de senha, ela é usada para abrir PDFs protegidos e tentar desbloqueá-los programaticamente.
- **Instalação**:
  ```
  pip install pikepdf
  ```

## Estrutura do Projeto

- protected.pdf   # Arquivo PDF protegido que será testado.
- rockyou.txt     # Wordlist com as possíveis senhas.
- main.py         # Script principal com interface gráfica (Tkinter).
- oldmain.py      # Versão anterior com PyPDF2 para fins de comparação.

## Wordlist

1. **Baixe o arquivo `rockyou.txt`**:
   - O arquivo `rockyou.txt` tem 133,4 MB e pode ser baixado nos seguintes links:
     - [Kaggle: Common Password List](https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt)
     - [GitHub: rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)

2. **Coloque o arquivo `rockyou.txt` e o arquivo PDF protegido no diretório do projeto.**

## Execução

1. Execute o script principal com interface gráfica:
   ```bash
   python main.py
   ```
2. Use os botões para selecionar o PDF protegido e a wordlist.
3. Clique em Iniciar para começar a tentativa de quebra de senha.
4. A barra de progresso mostrará o andamento e a senha sendo testada.
5. Caso a senha seja encontrada, ela será exibida na interface e no console.

## Notas técnicas

- O **pikepdf** é utilizado por ser mais performático e rápido que o **PyPDF2** em operações de leitura e tentativa de senha em PDFs.
- O **tqdm** adiciona uma barra de progresso para visualizar a taxa de testes de senhas.
- A interface **Tkinter** torna o processo mais amigável e interativo, exibindo o progresso da tentativa de senha e o resultado final.

## Captura de tela

| Tela Principal | Tela de Progresso |
|----------------|-------------------|
| ![Home](https://joaopauloaramuni.github.io/python-imgs/PdfCracker_with_UI/imgs/home.png) | ![Progresso](https://joaopauloaramuni.github.io/python-imgs/PdfCracker_with_UI/imgs/progress.png) |

## Exemplo de saída

[2] Total de senhas a testar: 14,344,392
  50%|███████████████        | 7,172,196/14,344,392 [00:10<00:10, 703,499 words/s]
[+] Senha encontrada: hello090

[!] Senha não encontrada. Tente com outra wordlist.

## Comparação com PyPDF2

Durante os testes, o **pikepdf** se mostrou significativamente mais rápido do que o **PyPDF2**. Por esse motivo, a implementação padrão utiliza o **pikepdf**, enquanto a versão anterior com **PyPDF2** está disponível no arquivo `oldmain.py`.

## Licença

Este projeto está licenciado sob a Licença MIT.
