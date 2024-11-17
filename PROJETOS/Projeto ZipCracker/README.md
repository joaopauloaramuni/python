
# Projeto ZipCracker

O **Projeto ZipCracker** tem como objetivo demonstrar como usar algoritmos de força bruta para tentar descobrir senhas de arquivos ZIP protegidos. O projeto utiliza uma lista de senhas comum, chamada `rockyou.txt`, para testar possíveis combinações até encontrar a senha correta.

## Como Funciona

O projeto tenta desbloquear um arquivo ZIP protegido por senha utilizando um algoritmo de força bruta. Ele tenta cada senha da lista `rockyou.txt` até encontrar a senha correta que permite extrair os arquivos contidos no ZIP. Para tornar o processo mais eficiente, o progresso do cracking da senha é exibido usando a biblioteca `tqdm`.

### Algoritmo de Força Bruta

**Força bruta** é uma técnica de quebra de senha que tenta todas as combinações possíveis até encontrar a correta. Embora essa abordagem seja garantida para encontrar a senha, ela pode ser muito lenta, dependendo do tamanho da lista de senhas e da complexidade da senha. Neste projeto, utilizamos a lista `rockyou.txt`, uma lista comum de senhas usadas em ataques de força bruta.

No código, o arquivo ZIP é iterado e tentamos cada senha da lista até que a senha correta seja encontrada ou todas as senhas tenham sido testadas.

## Dependências

### 1. `tqdm`
- **O que é**: A biblioteca `tqdm` é usada para exibir uma barra de progresso enquanto o código está testando as senhas. Isso facilita o acompanhamento do progresso, especialmente quando se trabalha com listas grandes de senhas.
- **Instalação**:
  ```
  pip install tqdm
  ```

## Como Usar

1. **Baixe o arquivo `rockyou.txt`**:
   - O arquivo `rockyou.txt` tem 133,4 MB e pode ser baixado nos seguintes links:
     - [Kaggle: Common Password List](https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt)
     - [GitHub: rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)

2. **Coloque o arquivo `rockyou.txt` e o arquivo ZIP protegido no diretório do projeto.**

3. **Execute o código** para tentar descobrir a senha do arquivo ZIP.

## Aviso

Este projeto é **para fins didáticos** apenas. O uso deste código para tentar quebrar senhas de arquivos sem permissão é **ilegal** e não é incentivado de forma alguma. O autor não se responsabiliza pelo uso indevido deste código.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
