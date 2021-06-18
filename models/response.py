from models.usuario_model import UsuarioModel
from models.endereco_model import EnderecoModel


class Response:

    def __init__(self, usuario, endereco_usuario):
        self.UsuarioModel = usuario
        self.EnderecoModel = endereco_usuario

    def json(self):
        return {
            'usuario': self.UsuarioModel.json(),
            'endereco': self.EnderecoModel.json(),
        }
