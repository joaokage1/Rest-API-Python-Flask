from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse

from models.endereco_model import EnderecoModel

atributos = reqparse.RequestParser()
atributos.add_argument('pais', type=str, required=True, help="Este campo não pode estar em branco")
atributos.add_argument('estado', type=str, required=True, help="Este campo não pode estar em branco")
atributos.add_argument('municipio', type=str, required=True, help="Este campo não pode estar em branco")
atributos.add_argument('cep', type=int, required=True, help="Este campo não pode estar em branco")
atributos.add_argument('rua', type=str, required=True, help="Este campo não pode estar em branco")
atributos.add_argument('numero', type=int, required=True, help="Este campo não pode estar em branco")
atributos.add_argument('complemento', type=str)


class Endereco(Resource):

    @jwt_required()
    def get(self, id):
        endereco = EnderecoModel.find_endereco_by_id(id)
        if endereco:
            return endereco.json()

        return {'message': 'Endereço não encontrado'}, 404

    @jwt_required()
    def put(self, id):
        endereco = EnderecoModel.find_endereco_by_id(id)
        if endereco:
            dados = atributos.parse_args()

            try:
                endereco.update_usuario(**dados)

            except Exception as e:
                return {'message': 'Houve um erro ao tentar atualizar o usuário {}'.format(e)}, 500

            return {'message': 'Endereço atualizado'}, 200

        return {'message': 'Endereço não encontrado'}, 404


class EnderecoCadastro(Resource):

    def post(self):
        dados = atributos.parse_args()
        endereco = EnderecoModel(**dados)
        endereco.save_endereco()
        return {'message': 'Endereço criado com sucesso'}, 201
