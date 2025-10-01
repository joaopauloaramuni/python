# Projeto ZipCracker

O **Projeto ZipCracker** tem como objetivo demonstrar como usar algoritmos de força bruta para tentar descobrir senhas de arquivos ZIP protegidos. O projeto utiliza uma lista de senhas comum, chamada `rockyou.txt`, para testar possíveis combinações até encontrar a senha correta.

## Como funciona

O projeto tenta desbloquear um arquivo ZIP protegido por senha utilizando um algoritmo de força bruta. Ele tenta cada senha da lista `rockyou.txt` até encontrar a senha correta que permite extrair os arquivos contidos no ZIP. Para tornar o processo mais eficiente, o progresso do cracking da senha é exibido usando a biblioteca `tqdm`.

### Algoritmo de força bruta

**Força bruta** é uma técnica de quebra de senha que tenta todas as combinações possíveis até encontrar a correta. Embora essa abordagem seja garantida para encontrar a senha, ela pode ser muito lenta, dependendo do tamanho da lista de senhas e da complexidade da senha. Neste projeto, utilizamos a lista `rockyou.txt`, uma lista comum de senhas usadas em ataques de força bruta.

No código, o arquivo ZIP é iterado e tentamos cada senha da lista até que a senha correta seja encontrada ou todas as senhas tenham sido testadas.

## Pré-requisitos

- Python 3.7 ou superior.
- Instalar as dependências necessárias:
  ```bash
  pip install tqdm
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
pip install tqdm
```

## Dependências

### `tqdm`
- **O que é**: A biblioteca `tqdm` é usada para exibir uma barra de progresso enquanto o código está testando as senhas. Isso facilita o acompanhamento do progresso, especialmente quando se trabalha com listas grandes de senhas.
- **Instalação**:
  ```
  pip install tqdm
  ```

## Wordlist

1. **Baixe o arquivo `rockyou.txt`**:
   - O arquivo `rockyou.txt` tem 133,4 MB e pode ser baixado nos seguintes links:
     - [Kaggle: Common Password List](https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt)
     - [GitHub: rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)

2. **Coloque o arquivo `rockyou.txt` e o arquivo ZIP protegido no diretório do projeto.**

## Execução

1. Coloque o arquivo ZIP protegido na mesma pasta do script.
2. Coloque uma wordlist (rockyou.txt) no formato .txt contendo as possíveis senhas na mesma pasta do script.
3. Execute o script principal:
   ```bash
   python main.py
   ```

5. Caso a senha seja encontrada, ela será exibida no console.

## Exemplo de saída

[2] Total de senhas a testar: 14,344,392
  50%|███████████████        | 7,172,196/14,344,392 [00:10<00:10, 703,499 words/s]
[+] Senha encontrada: hello090

[!] Senha não encontrada. Tente com outra wordlist.

## Aviso

Este projeto é **para fins didáticos** apenas. O uso deste código para tentar quebrar senhas de arquivos sem permissão é **ilegal** e não é incentivado de forma alguma. O autor não se responsabiliza pelo uso indevido deste código.

## Licença

Este projeto está licenciado sob a Licença MIT.
