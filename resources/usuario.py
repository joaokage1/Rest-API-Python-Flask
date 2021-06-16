import re
from flask_restful import Resource, reqparse
from models.usuario_model import UsuarioModel

usuarios = [
    {
        'id': 1,
        'nome':'João Vitor',
        'email': 'jvgsilva180@gmail.com',
        'senha': '123456',
    },
    {
        'id': 2,
        'nome':'Jaqueline',
        'email': 'jaqueline@gmail.com',
        'senha': '123456',
    },
    {
        'id': 3,
        'nome':'Tião',
        'email': 'tiao@gmail.com',
        'senha': '123456',
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
    
    def find_usuario(id):
        for usuario in usuarios:
            if usuario['id'] == id:
                return usuario
        return None
    
    def get(self, id):
        usuario = Usuario.find_usuario(id)
        if usuario :
            return usuario
        
        return {'message': 'Usuario não encontrado'}, 404
    
    def post(self, id):
        
        dados = Usuario.args.parse_args()
        novo_usuario = UsuarioModel(id, **dados)
        novo_json = novo_usuario.json()
        
        usuarios.append(novo_json)
        return novo_json, 200
    
    def put(self, id):
        dados = Usuario.args.parse_args()
        novo_usuario = UsuarioModel(id, **dados)
        novo_json = novo_usuario.json()
        
        usuario = Usuario.find_usuario(id)
        if usuario :
            usuario.update(novo_json)
            return novo_json, 200
        
        usuarios.append(novo_json)
        return novo_json, 201
    
    def delete(self, id):
        global usuarios
        usuarios = [usuario for usuario in usuarios if usuario['id'] != id]
        return {'message': 'Usuario deleteado.'}