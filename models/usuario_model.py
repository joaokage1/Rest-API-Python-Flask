from models.endereco_model import EnderecoModel


class UsuarioModel:

    def __init__(self, id, nome, email, senha, cpf, pis, endereco: EnderecoModel):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.pis = pis
        self.endereco: EnderecoModel = endereco

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha,
            'cpf': self.cpf,
            'pis': self.pis,
            'endereco': self.endereco,
        }
