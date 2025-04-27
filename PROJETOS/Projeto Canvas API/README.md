# Projeto Canvas API - Integração e Listagem de Tarefas

## Descrição
Este projeto utiliza a API do Canvas para recuperar informações sobre os cursos e as tarefas associadas ao usuário autenticado. O script exibe o nome do curso, o ID, e a lista de tarefas com suas respectivas datas de entrega formatadas no fuso horário de São Paulo (UTC-3).

O código foi desenvolvido para facilitar o acesso a informações importantes sobre as tarefas, como a data de entrega, diretamente da plataforma Canvas, e apresentá-las de forma amigável.

## Exemplo de Saída
O script irá gerar uma saída no formato abaixo para cada curso e suas tarefas:

```
******************************************************************************************************************************************************
***** Curso: Projeto de Software - Engenharia de Software - Campus Coração Eucarístico - PMG - Noite - 2024/2 | ID do curso: 205259 *****
Tarefa: Trabalho 1 - SGO - Valor: 10 pontos | ID da Tarefa: 1011990 | Data de Entrega: 18/09/2024 23:59:00
Tarefa: Resenha do Artigo Big Ball of Mud | ID da Tarefa: 1015952 | Data de Entrega: 09/09/2024 23:59:00
Tarefa: Resenha do Artigo Thoughtworks Technology Radar | ID da Tarefa: 1018490 | Data de Entrega: 16/09/2024 23:59:00
Tarefa: Resenha do Artigo Microsservices  | ID da Tarefa: 1020616 | Data de Entrega: 06/10/2024 23:59:00
Tarefa: Trabalho Final - 20 pts | ID da Tarefa: 1023456 | Data de Entrega: 01/12/2024 23:59:00
Tarefa: Atividade Code Review | ID da Tarefa: 1023506 | Data de Entrega: 27/10/2024 23:59:00
Tarefa: Resenha dos Capítulos 6 e 7 do livro Engenharia de Software Moderna | ID da Tarefa: 1023515 | Data de Entrega: 18/10/2024 23:59:00
Tarefa: AV1 - 25 pontos | ID da Tarefa: 1029012 | Data de Entrega: 24/09/2024 23:59:00
Tarefa: AV2 - 25 pontos | ID da Tarefa: 1058667 | Data de Entrega: 03/12/2024 23:59:00
Tarefa: ADA | ID da Tarefa: 1059544 | Data de Entrega: 04/12/2024 23:59:00
******************************************************************************************************************************************************
```

## Como Gerar o Token de Acesso no Canvas

1. **Acesse o Canvas**:
   - Abra o navegador e vá para a URL do Canvas da sua instituição: [https://pucminas.instructure.com](https://pucminas.instructure.com).

2. **Faça o Login**:
   - Entre com seu nome de usuário e senha no Canvas, usando suas credenciais de acesso.

3. **Acesse as Configurações do Perfil**:
   - No canto superior esquerdo, clique no seu **avatar** ou nome de usuário.
   - No menu suspenso, clique em **Configurações**.

4. **Gerar o Token de Acesso**:
   - Na tela de configurações do seu perfil, localize a opção **"Tokens de Acesso"**.
   - Clique em **"Configurações"** no menu lateral e, depois, clique em **"Novo token de acesso"**.

5. **Preencha as Informações do Token**:
   - No campo **"Descrição"**, coloque um nome para o token, como **"API do Projeto"**.
   - Escolha a **data de expiração** do token, se desejar (pode ser indefinido).
   - Clique em **"Gerar Token"**.

6. **Copie o Token Gerado**:
   - O token será exibido uma única vez. **Copie o token gerado** e guarde em um lugar seguro.
   - Exemplo de token (não compartilhe com ninguém): `11748~U646vcwetXcJRXwhPMvZwNym9PKYLUhCZuRWmPBD4Yv2t4YnnkH2FG**********`.

7. **Substitua no Código**:
   - No seu código Python, substitua o valor da variável `API_KEY` pelo token gerado.

   ```python
   API_KEY = "seu_token_gerado_aqui"
   ```

## Dependências

- [CanvasAPI](https://pypi.org/project/canvasapi/): Biblioteca Python para acessar a API do Canvas LMS da Instructure. Esta biblioteca facilita a interação com o sistema Canvas, permitindo que desenvolvedores gerenciem programaticamente cursos, usuários, notas, tarefas e muito mais. O CanvasAPI foi criado e é mantido pela Universidade da Flórida Central (University of Central Florida) como um projeto de código aberto, oferecendo uma maneira eficiente e simples de integrar e automatizar o uso do Canvas LMS.

  - [GitHub CanvasAPI](https://github.com/ucfopen/canvasapi)
  - A biblioteca permite a automação de processos como:
    - Criação e gerenciamento de cursos
    - Acesso a dados de usuários e turmas
    - Gerenciamento de tarefas e notas
    - Interação com o gradebook (boletim de notas)
    - E muito mais, de forma programática.

  O projeto é de código aberto, o que significa que qualquer desenvolvedor pode contribuir e usar a biblioteca para integrar o Canvas LMS com outros sistemas e fluxos de trabalho.

- [pytz](https://pypi.org/project/pytz/): Biblioteca Python para trabalhar com fusos horários. Usada para garantir que as datas e horas sejam corretamente convertidas para o fuso horário local desejado.

## Instalação das Dependências

Para executar este projeto, é necessário instalar as dependências. Siga os passos abaixo:

1. Crie um ambiente virtual:
   ```
   python -m venv .venv
   ```

2. Ative o ambiente virtual:
   - **Windows**:
     ```
     .venv\Scripts\activate
     ```
   - **Linux/MacOS**:
     ```
     source .venv/bin/activate
     ```

3. Instale as dependências:
   ```
   pip install canvasapi pytz
   ```

## Documentação e Links Úteis

- [CanvasAPI no GitHub](https://github.com/ucfopen/canvasapi)
- [CanvasAPI no PyPI](https://pypi.org/project/canvasapi/)
- [pytz no PyPI](https://pypi.org/project/pytz/)
- [Documentação do CanvasAPI](https://canvasapi.readthedocs.io/en/stable/)
- [Exemplos do CanvasAPI - Cursos](https://canvasapi.readthedocs.io/en/stable/examples.html#courses)
- [Exemplos do CanvasAPI - Tarefas](https://canvasapi.readthedocs.io/en/stable/examples.html#assignments)
- [Documentação da API do Canvas](https://canvas.instructure.com/doc/api/index.html)

## Licença

Este projeto está licenciado sob a Licença MIT.
