from sql_alchemy import banco


class EnderecoModel(banco.Model):
    __tablename__ = 'enderecos'

    id = banco.Column(banco.BigInteger, primary_key=True)
    pais = banco.Column(banco.String(80))
    estado = banco.Column(banco.String)
    municipio = banco.Column(banco.String)
    cep = banco.Column(banco.Integer)
    rua = banco.Column(banco.String)
    numero = banco.Column(banco.Integer)
    complemento = banco.Column(banco.String)

    def __init__(self, id, pais, estado, municipio, cep, rua, numero, complemento):
        self.id = id
        self.pais = pais
        self.estado = estado
        self.municipio = municipio
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.complemento = complemento

    def json(self):
        return {
            'id': self.id,
            'pais': self.pais,
            'estado': self.estado,
            'municipio': self.municipio,
            'cep': self.cep,
            'rua': self.rua,
            'numero': self.numero,
            'complemento': self.complemento,
        }
