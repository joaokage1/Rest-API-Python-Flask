import re
from flask_restful import Resource, reqparse
from models.usuario_model import UsuarioModel


class Usuarios(Resource):

    def get(self):
        return {'usuarios': [usuario.json() for usuario in UsuarioModel.query.all()]}


class Usuario(Resource):
    args = reqparse.RequestParser()
    args.add_argument('nome', type=str, required=True, help="Este campo não pode estar em branco")
    args.add_argument('email', type=str, required=True, help="Este campo não pode estar em branco")
    args.add_argument('senha', type=str, required=True, help="Este campo não pode estar em branco")
    args.add_argument('cpf', type=str, required=True, help="Este campo não pode estar em branco")
    args.add_argument('pis', type=str, required=True, help="Este campo não pode estar em branco")
    args.add_argument('endereco_id')

    update_args = reqparse.RequestParser()
    update_args.add_argument('nome', type=str, required=True, help="Este campo não pode estar em branco")
    update_args.add_argument('senha', type=str, required=True, help="Este campo não pode estar em branco")

    def validate_user_id(id):
        return UsuarioModel.find_usuario_by_id(id)

    def validate_user_email(email):
        return UsuarioModel.find_usuario_by_email(email)

    def validate_user_cpf(cpf):
        return UsuarioModel.find_usuario_by_cpf(cpf)

    def validate_user_pis(pis):
        return UsuarioModel.find_usuario_by_pis(pis)

    def get(self, id):
        usuario = UsuarioModel.find_usuario_by_id(id)
        if usuario:
            return usuario.json()

        return {'message': 'Usuario não encontrado'}, 404

    def post(self, id):

        dados = Usuario.args.parse_args()
        if Usuario.validate_user_id(id):
            return {"message": "Usuario '{}' já existe".format(id)}, 400

        if Usuario.validate_user_email(dados['email']):
            return {"message": "Email '{}' já cadastrado".format(dados['email'])}, 400

        if Usuario.validate_user_cpf(dados['cpf']):
            return {"message": "CPF '{}' já cadastrado".format(dados['cpf'])}, 400

        if Usuario.validate_user_pis(dados['pis']):
            return {"message": "PIS '{}' já cadastrado".format(dados['pis'])}, 400

        usuario = UsuarioModel(id, **dados)
        try:
            usuario.save_usuario()
        except:
            return {'message': 'Houve um erro ao tentar cadastrar usuário'}, 500
        return usuario.json()

    def put(self, id):
        dados = Usuario.update_args.parse_args()

        usuario_encontrado = UsuarioModel.find_usuario_by_id(id)
        if usuario_encontrado:
            usuario_encontrado.update_usuario(**dados)
            try:
                usuario_encontrado.save_usuario()
            except:
                return {'message': 'Houve um erro ao tentar atualizar o usuário'}, 500
            return usuario_encontrado.json(), 200

        return {"message": "Usuario com email '{}' não encontrado".format(dados['email'])}, 200

    def delete(self, id):
        usuario = Usuario.validate_user_id(id)
        if usuario:
            try:
                usuario.delete_usuario()
            except:
                return {'message': 'Houve um erro ao tentar deletar o usuário'}, 500
            return {'message': 'Usuario deletado.'}, 200

        return {'message': 'Usuario não encontrado'}, 404
