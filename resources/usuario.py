import re
from flask_restful import Resource, reqparse
from models.usuario_model import UsuarioModel
from models.endereco_model import EnderecoModel

usuarios = [
    {
        'id': 1,
        'nome': 'João Vitor',
        'email': 'jvgsilva180@gmail.com',
        'senha': '123456',
        'cpf': '45215965421',
        'pis': '35246465131',
        'endereco': {"pais": "Brasil"
            , "estado": "Sao Paulo"
            , "municipio": "Sertãozinho"
            , "cep": 14161314, "rua": "Nilo Moi", "numero": 34}
    }
]


class Usuarios(Resource):

    def get(self):
        return {'usuarios': usuarios}


class Usuario(Resource):
    args = reqparse.RequestParser()
    args.add_argument('nome')
    args.add_argument('email')
    args.add_argument('senha')
    args.add_argument('cpf')
    args.add_argument('pis')
    args.add_argument('endereco', type=dict)

    def find_usuario(id):
        for usuario in usuarios:
            if usuario['id'] == id:
                return usuario
        return None

    def get(self, id):
        usuario = Usuario.find_usuario(id)
        if usuario:
            return usuario

        return {'message': 'Usuario não encontrado'}, 404

    def post(self, id):

        dados = Usuario.args.parse_args()
        novo_usuario = UsuarioModel(id, **dados)
        novo_endereco = EnderecoModel(**dados['endereco'])
        novo_usuario.endereco = novo_endereco.json()
        novo_json = novo_usuario.json()

        usuarios.append(novo_json)
        return novo_json, 200

    def put(self, id):
        dados = Usuario.args.parse_args()
        novo_usuario = UsuarioModel(id, **dados)
        novo_endereco = EnderecoModel(**dados['endereco'])
        novo_usuario.endereco = novo_endereco.json()
        novo_json = novo_usuario.json()

        usuario = Usuario.find_usuario(id)
        if usuario:
            usuario.update(novo_json)
            return novo_json, 200

        usuarios.append(novo_json)
        return novo_json, 201

    def delete(self, id):
        global usuarios
        usuarios = [usuario for usuario in usuarios if usuario['id'] != id]
        return {'message': 'Usuario deleteado.'}
