# Projeto RarCracker

O **Projeto RarCracker** é uma aplicação simples de força bruta para tentar descobrir a senha de um arquivo RAR, utilizando uma lista de senhas pré-definidas (word-list). O projeto utiliza um algoritmo de força bruta, que tenta extrair o conteúdo do arquivo RAR com cada senha da lista, até encontrar a senha correta.

## Como funciona

O projeto tenta desbloquear um arquivo RAR protegido por senha utilizando um algoritmo de força bruta. Ele tenta cada senha da lista `rockyou.txt` até encontrar a senha correta que permite extrair os arquivos contidos no RAR. Para tornar o processo mais eficiente, o progresso do cracking da senha é exibido usando a biblioteca `tqdm`.

### Algoritmo de força bruta

**Força bruta** é uma técnica de quebra de senha que tenta todas as combinações possíveis até encontrar a correta. Embora essa abordagem seja garantida para encontrar a senha, ela pode ser muito lenta, dependendo do tamanho da lista de senhas e da complexidade da senha. Neste projeto, utilizamos a lista `rockyou.txt`, uma lista comum de senhas usadas em ataques de força bruta.

No código, o arquivo RAR é iterado e tentamos cada senha da lista até que a senha correta seja encontrada ou todas as senhas tenham sido testadas.

## Dependências

Este projeto depende de algumas bibliotecas que precisam ser instaladas:

### Bibliotecas Python:
- **tqdm**: Esta biblioteca é usada para fornecer uma barra de progresso durante o processo de tentativa das senhas, facilitando o acompanhamento do progresso.
- **rarfile**: A biblioteca `rarfile` permite trabalhar com arquivos RAR em Python, incluindo a extração de arquivos protegidos por senha.

Você pode instalar as dependências usando o comando:

```bash
pip install tqdm rarfile
```

### Ferramenta UnRAR:
Este projeto também utiliza a ferramenta `unrar` no sistema, que é necessária para extrair o conteúdo do arquivo RAR.

Se você estiver usando macOS, pode instalar o `unrar` com o seguinte comando:

```bash
brew install rar
```

Para Linux:

```bash
sudo apt-get install rar
```

ou, se estiver usando o yum:

```bash
sudo yum install rar
```

## Como usar

1. Prepare um arquivo `.rar` protegido por senha (no exemplo, o arquivo é `secret.rar`).
2. Prepare uma **word-list** de senhas. O arquivo `rockyou.txt` é uma lista de senhas comum utilizada para este tipo de ataque e pode ser baixada a partir de:

- [Kaggle - rockyou.txt](https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt)
- [GitHub - rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)

O arquivo `rockyou.txt` possui 133,4 MB de tamanho e contém milhões de senhas comuns.

3. Coloque o arquivo `rockyou.txt` e o arquivo `.rar` na mesma pasta do script Python.
4. Execute o script Python e ele tentará extrair o conteúdo do arquivo `.rar` utilizando as senhas presentes na word-list.

### Exemplo de comando para criar um arquivo `.rar` protegido por senha:

```bash
rar a -phello090 secret.rar secret.txt
```

## Aviso

Este projeto tem fins **didáticos** e não deve ser utilizado de maneira indevida. A utilização de técnicas de força bruta para acessar arquivos sem permissão é ilegal e antiética.

## Licença

Este projeto está licenciado sob a Licença MIT.
