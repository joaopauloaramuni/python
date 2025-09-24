# Projeto PdfCracker

PdfCracker é uma ferramenta simples para tentativa de quebra de senha de arquivos PDF protegidos utilizando uma wordlist. Este projeto foi desenvolvido com Python, empregando as bibliotecas `pikepdf` e `tqdm`.

## Funcionalidades

- Testa cada senha de uma wordlist para abrir um arquivo PDF protegido.
- Exibe progresso em tempo real utilizando a barra de progresso do `tqdm`.
- Relata a senha encontrada ou notifica que nenhuma senha foi eficaz.

## Pré-requisitos

- Python 3.7 ou superior.
- Instalar as dependências necessárias:
  ```bash
  pip install tqdm pikepdf
  ```

## Estrutura do Projeto

protected.pdf   # Arquivo PDF protegido que será testado.
rockyou.txt     # Wordlist com as possíveis senhas.
main.py         # Script principal para tentativa de quebra de senha.
oldmain.py      # Versão anterior com PyPDF2 para fins de comparação.

## Execução

1. Coloque o arquivo PDF protegido na mesma pasta do script.
2. Forneça uma wordlist no formato .txt contendo as possíveis senhas.
3. Execute o script principal:
   ```bash
   python main.py
   ```

5. Caso a senha seja encontrada, ela será exibida no console.

## Notas técnicas

- O **pikepdf** é utilizado por ser mais performático e rápido que o **PyPDF2** em operações de leitura e tentativa de senha em PDFs.
- O **tqdm** adiciona uma barra de progresso para visualizar a taxa de testes de senhas.

## Exemplo de saída

[2] Total de senhas a testar: 14,344,392
  50%|███████████████        | 7,172,196/14,344,392 [00:10<00:10, 703,499 words/s]
[+] Senha encontrada: hello090

[!] Senha não encontrada. Tente com outra wordlist.

## Comparação com PyPDF2

Durante os testes, o **pikepdf** se mostrou significativamente mais rápido do que o **PyPDF2**. Por esse motivo, a implementação padrão utiliza o **pikepdf**, enquanto a versão anterior com **PyPDF2** está disponível no arquivo `oldmain.py`.

## Licença

Este projeto está licenciado sob a Licença MIT.

