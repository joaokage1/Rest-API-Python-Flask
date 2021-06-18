from sql_alchemy import banco


class UsuarioModel(banco.Model):
    __tablename__ = 'usuarios'

    id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(80))
    email = banco.Column(banco.String)
    senha = banco.Column(banco.String)
    cpf = banco.Column(banco.String)
    pis = banco.Column(banco.String)
    endereco_id = banco.Column(banco.Integer, banco.ForeignKey('enderecos.id'))
    endereco = banco.relationship('EnderecoModel')

    def __init__(self, nome, email, senha, cpf, pis, endereco_id):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.pis = pis
        self.endereco_id = endereco_id

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'cpf': self.cpf,
            'pis': self.pis,
            'endereco': self.endereco.json() if self.endereco else None,
        }

    def save_usuario(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_usuario(self):
        if self.endereco:
            self.endereco.delete_endereco()

        banco.session.delete(self)
        banco.session.commit()

    def update_usuario(self, nome, senha):
        self.nome = nome
        self.senha = senha
        banco.session.add(self)
        banco.session.commit()

    @classmethod
    def find_usuario_by_id(cls, id):
        usuario = cls.query.filter_by(id=id).first()
        if usuario:
            return usuario
        return None

    @classmethod
    def find_usuario_by_email(cls, email):
        usuario = cls.query.filter_by(email=email).first()
        if usuario:
            return usuario
        return None

    @classmethod
    def find_usuario_by_cpf(cls, cpf):
        usuario = cls.query.filter_by(cpf=cpf).first()
        if usuario:
            return usuario
        return None

    @classmethod
    def find_usuario_by_pis(cls, pis):
        usuario = cls.query.filter_by(pis=pis).first()
        if usuario:
            return usuario
        return None
