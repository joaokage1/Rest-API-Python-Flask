import hmac

from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from flask_restful import Resource, reqparse

from blacklist import BLACKLIST
from models.usuario_model import UsuarioModel

atributos = reqparse.RequestParser()
atributos.add_argument('nome', type=str, required=True, help="Este campo não pode estar em branco")
atributos.add_argument('email', type=str, required=True, help="Este campo não pode estar em branco")
atributos.add_argument('senha', type=str, required=True, help="Este campo não pode estar em branco")
atributos.add_argument('cpf', type=str, required=True, help="Este campo não pode estar em branco")
atributos.add_argument('pis', type=str, required=True, help="Este campo não pode estar em branco")
atributos.add_argument('endereco_id', type=int, required=True, help="Este campo não pode estar em branco")


class Usuario(Resource):
    # usuarios/{id}

    def validate_user_id(id):
        return UsuarioModel.find_usuario_by_id(id)

    def validate_user_email(email):
        return UsuarioModel.find_usuario_by_email(email)

    def validate_user_cpf(cpf):
        return UsuarioModel.find_usuario_by_cpf(cpf)

    def validate_user_pis(pis):
        return UsuarioModel.find_usuario_by_pis(pis)

    @jwt_required()
    def get(self, id):
        usuario = UsuarioModel.find_usuario_by_id(id)
        if usuario:
            return usuario.json()

        return {'message': 'Usuario não encontrado'}, 404

    @jwt_required()
    def delete(self, id):
        usuario = Usuario.validate_user_id(id)
        if usuario:
            try:
                usuario.delete_usuario()
                jwt_id = get_jwt()['jti']
                BLACKLIST.add(jwt_id)
            except:
                return {'message': 'Houve um erro ao tentar deletar o usuário'}, 500
            return {'message': 'Usuario deletado.'}, 200

        return {'message': 'Usuario não encontrado'}, 404


class UsuarioCadastro(Resource):

    # /cadastro
    def post(self):
        dados = atributos.parse_args()
        if Usuario.validate_user_email(dados['email']):
            return {"message": "Já existe cadastro para o email '{}'".format(dados['email'])}, 400
        if Usuario.validate_user_pis(dados['pis']):
            return {"message": "Já existe cadastro para o PIS '{}'".format(dados['pis'])}, 400
        if Usuario.validate_user_cpf(dados['cpf']):
            return {"message": "Já existe cadastro para o CPF '{}'".format(dados['cpf'])}, 400

        try:
            user = UsuarioModel(**dados)
            user.save_usuario()
        except:
            return {'message': 'Houve um erro ao tentar cadastrar o usuário'}, 500

        return {'message': 'Usuário criado com sucesso'}, 201


class UsuarioLogin(Resource):

    @classmethod
    def post(cls):
        atributos_login = reqparse.RequestParser()
        atributos_login.add_argument('email', type=str, required=True, help="Este campo não pode estar em branco")
        atributos_login.add_argument('senha', type=str, required=True, help="Este campo não pode estar em branco")
        dados = atributos_login.parse_args()

        usuario = UsuarioModel.find_usuario_by_email(dados['email'])

        if usuario and hmac.compare_digest(dados['senha'], usuario.senha):
            token_de_acesso = create_access_token(identity=usuario.id)
            return {'access_token': token_de_acesso}, 200

        return {'message': 'Email ou senha incorretos'}, 401


class UsuarioLogout(Resource):

    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return {'message': 'Até mais, e volte logo'}, 200
