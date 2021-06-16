
class EnderecoModel:

    def __init__(self, pais, estado, municipio, cep, rua, numero, complemento):
        self.pais = pais
        self.estado = estado
        self.municipio = municipio
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.complemento = complemento

    def json(self):
        return {
            'pais': self.pais,
            'estado': self.estado,
            'municipio': self.municipio,
            'cep': self.cep,
            'rua': self.rua,
            'numero': self.numero,
            'complemento': self.complemento,
        }
