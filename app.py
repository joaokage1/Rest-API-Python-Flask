import datetime

from flask import Flask, jsonify
from flask_restful import Api

from blacklist import BLACKLIST
from resources.usuario import Usuario, UsuarioCadastro, UsuarioLogin, UsuarioLogout
from resources.endereco import Endereco, EnderecoCadastro
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'MyJWTSecretKeyForFlaskApplication'
# app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=1)
app.config['JWT_BLACKLIST_ENABLED'] = True

api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def cria_banco():
    banco.create_all()


@jwt.token_in_blocklist_loader
def verifica_blacklist(self, token):
    return token['jti'] in BLACKLIST


@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    return jsonify({'message': 'Você está deslogado'}), 401


api.add_resource(Usuario, '/usuarios/<int:id>')
api.add_resource(UsuarioCadastro, '/cadastro')
api.add_resource(UsuarioLogin, '/login')
api.add_resource(UsuarioLogout, '/logout')
api.add_resource(Endereco, '/endereco/<int:id>')
api.add_resource(EnderecoCadastro, '/endereco')

if __name__ == '__main__':
    from sql_alchemy import banco

    banco.init_app(app)
    app.run(debug=True)
