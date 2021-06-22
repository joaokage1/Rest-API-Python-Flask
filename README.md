# Desafio Back-End

API Rest para o desafio de cadastro de usuário WEB. Foi desenvolvido em Python, com o microframework Flask e autenticação JWT.

<p align="center">
  <img src="https://cdn.worldvectorlogo.com/logos/python-5.svg" alt="python-logo" width="120px" height="120px"/>
  <img src="https://cdn.icon-icons.com/icons2/2389/PNG/512/flask_logo_icon_145276.png" alt="flask-logo" width="120px" height="120px"/>
</p>

### Configuração Back-End

Não há necessidade de criar o banco de dados, pois para execução local foi utilizado o sqlite.
No diretório do projeto abra o prompt e execute o seguinte comando para instalação das bibliotecas
`$ pip install -r requirements.txt`

Em seguida este
`$ export FLASK_APP=app.py  `

Para iniciar o projeto

`$ flask run`

## EndPoints
## CRUD Usuario
Método `GET`
Url : http://127.0.0.1:5000/usuarios/<int:id>

Retorna o registro cadastrado no banco de determinado usuário

Método `POST`
Url :http://127.0.0.1:5000/cadastro

Insere um determinado usuário, com as seguintes informações no request:

>{
    "nome": "Nome do usuário",
    "email": "Email do usuário",
    "senha": "senha",
    "cpf": "CPF",
    "pis": "PIS",
    "endereco_id": chave estrangeira para tabela de endereços.
}

Url :http://127.0.0.1:5000/login

Faz login com usuario cadastrado, usando o seguinte request:

>{
    "email": "Email do usuário",
    "senha": "senha"
}

Url :http://127.0.0.1:5000/logout

Faz logout do usuario logado:

Método DELETE
Url :http://127.0.0.1:5000/usuarios/<int:id>

Deleta o registro que possua o id e desloga da aplicação.

## CRUD Endereço
Método `POST`
Url :http://127.0.0.1:5000/endereco

Faz o cadastro de um endereço no banco, usando o seguinte request:

>{
    "pais":"país do usuário",
    "estado":"estado do usuário",
    "municipio":"cidade",
    "cep":CEP,
    "rua":"Rua",
    "numero":Numero da residencia,
    "complemento":"Complemento * opcional"
}

Método `PUT`
Url :http://127.0.0.1:5000/endereco/<int:id>

Atualiza um endereço com o seguint request:
>{
    "pais":"país do usuário",
    "estado":"estado do usuário",
    "municipio":"cidade",
    "cep":CEP,
    "rua":"Rua",
    "numero":Numero da residencia,
    "complemento":"Complemento * opcional"
}

Nota: O método de delete é feito automáticamente aós deletar um usuário.

## Caso queira, todos os endpoints também estão disponíveis em:
- http://joaostz.pythonanywhere.com/

Para o deploy, foi utilizado o banco de dados mySql.

## O Front-end da aplicação está disponível em:
- https://github.com/joaokage1/pt-desafio

