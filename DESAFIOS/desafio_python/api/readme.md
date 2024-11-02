## Desafio 
#### 05) API Imagine que você ficou responsável por desenvolver o backend do sistema de uma biblioteca. Crie uma API RESTful para o cadastro, edição, listagem e exclusão dos livros (título, autor, edição) e o controle de entradas e saídas.  
A proposta foi feita em Python com [Django](https://www.djangoproject.com/) e [Django Rest Framework](https://www.django-rest-framework.org/)   
  
Requisitos:  
 - Python  
 - Postman  
   
 Para garantir uma facilidade, o projeto já acompanha o `db.sqlite3` para ser executado de maneira mais simples e já possui alguns dados pré-cadastrados. 

> Um [ambiente virtual de python](https://docs.python.org/3/library/venv.html) é recomendado, porem não é obrigatório para os passos abaixo.
> <br> Lembre-se de estar na pasta /api/ ao executar os comandos abaixo:

 1. `pip install -r requirements.txt`   para instalar as dependências 
 2. `python manage.py runserver` para executar o servidor na porta :8000

Agora basta importar o Postman [por link](https://www.getpostman.com/collections/ab77ab1737fcf5ec147e) ou por arquivo que esta em `api/Biblioteca.postman_collection.json`


O usuário super criado no banco enviado é: `Login: admin | Senha: admin`
