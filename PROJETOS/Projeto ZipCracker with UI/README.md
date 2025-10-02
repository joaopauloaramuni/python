# Projeto ZipCracker with UI

O **Projeto ZipCracker with UI** é uma versão com interface gráfica (Tkinter) do utilitário educacional que demonstra conceitos de força bruta e tentativa de senhas em arquivos ZIP protegidos. Esta versão adiciona uma interface simples e interativa para selecionar arquivos, acompanhar progresso e iniciar as tentativas de forma visual.

## O que há de novo (com UI)
- Interface gráfica construída com **Tkinter** para facilitar o uso.
- Seleção de arquivo ZIP protegido via diálogo de arquivos.
- Escolha de *wordlist* (por exemplo `rockyou.txt`) através da interface.
- Botão **Iniciar** para controlar o início da execução.
- Barra de progresso e logs em tempo real (utilizando `tqdm` ou componente visual equivalente).
- Notificações claras ao encontrar a senha ou ao finalizar a lista de tentativas.
- Aviso sonoro opcional ao encontrar a senha (arquivo `task_complete.mp3).

## Funcionalidades principais
- Teste de senhas a partir de uma *wordlist* fornecida pelo usuário.  
- Seleção do arquivo ZIP e da wordlist via diálogos de arquivo.  
- Barra de progresso e feedback em tempo real (porcentagem e tentativas/segundo).  
- Interface responsiva (threading) — a UI não congela durante o processo.  
- Tratamento de erros e mensagens amigáveis (ZIP inválido, wordlist vazia, etc.).  
- Notificação ao encontrar a senha (exibição na UI e `messagebox`).  
- Som de finalização opcional (reprodução de `task_complete.mp3` com `pygame`).

## Como funciona

O projeto tenta desbloquear um arquivo ZIP protegido por senha utilizando um algoritmo de força bruta. Ele tenta cada senha da lista `rockyou.txt` até encontrar a senha correta que permite extrair os arquivos contidos no ZIP. Para tornar o processo mais eficiente, o progresso do cracking da senha é exibido usando a biblioteca `tqdm`.

### Algoritmo de força bruta

**Força bruta** é uma técnica de quebra de senha que tenta todas as combinações possíveis até encontrar a correta. Embora essa abordagem seja garantida para encontrar a senha, ela pode ser muito lenta, dependendo do tamanho da lista de senhas e da complexidade da senha. Neste projeto, utilizamos a lista `rockyou.txt`, uma lista comum de senhas usadas em ataques de força bruta.

No código, o arquivo ZIP é iterado e tentamos cada senha da lista até que a senha correta seja encontrada ou todas as senhas tenham sido testadas.

## Pré-requisitos

- Python 3.7 ou superior.
- Instalar as dependências necessárias:
  ```bash
  pip install tqdm pygame
  ```
- Baixar uma wordlist como o `rockyou.txt`.
- `tkinter` — geralmente incluído na instalação padrão do Python (GUI).

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

### 1. `tqdm`
- **O que é**: A biblioteca `tqdm` é usada para exibir uma barra de progresso enquanto o código está testando as senhas. Isso facilita o acompanhamento do progresso, especialmente quando se trabalha com listas grandes de senhas.
- **Instalação**:
  ```
  pip install tqdm
  ```

### 2. `pygame`
- **O que é**: `pygame` é uma biblioteca usada para reproduzir o som de notificação (`task_complete.mp3`) quando a senha correta é encontrada.  
- **Instalação**:
  ```
  pip install pygame
  ```
> **Observação:** em sistemas Linux, `pygame` pode depender de bibliotecas do sistema (ex.: `libsdl2`, `libportaudio`, `alsa`). Se houver erro ao inicializar o mixer, instale as dependências do sistema antes de instalar o `pygame`.

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

## Captura de tela

| Tela Principal | Tela de Progresso |
|----------------|-------------------|
| ![Home](https://joaopauloaramuni.github.io/python-imgs/ZipCracker_with_UI/imgs/home.png) | ![Progresso](https://joaopauloaramuni.github.io/python-imgs/ZipCracker_with_UI/imgs/progress.png) |

## Exemplo de saída

[2] Total de senhas a testar: 14,344,392
  50%|███████████████        | 7,172,196/14,344,392 [00:10<00:10, 703,499 words/s]
[+] Senha encontrada: hello090

[!] Senha não encontrada. Tente com outra wordlist.

## Aviso

Este projeto é **para fins didáticos** apenas. O uso deste código para tentar quebrar senhas de arquivos sem permissão é **ilegal** e não é incentivado de forma alguma. O autor não se responsabiliza pelo uso indevido deste código.

## Documentação e Links Úteis

- [MyInstants — efeitos sonoros online](https://www.myinstants.com/pt/index/br/) — para baixar sons como `task_complete.mp3`.
- [Documentação do pygame](https://www.pygame.org/docs/) — informações sobre mixer e reprodução de áudio.
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html) — documentação oficial da biblioteca GUI usada no projeto.
- [tqdm Documentation](https://tqdm.github.io/) — documentação oficial para barras de progresso.

## Licença

Este projeto está licenciado sob a Licença MIT.
