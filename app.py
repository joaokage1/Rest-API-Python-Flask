from flask import Flask
from flask_restful import  Api
from resources.usuario import Usuarios, Usuario

app = Flask(__name__)
api = Api(app)
    
api.add_resource(Usuarios,'/usuarios')
api.add_resource(Usuario, '/usuarios/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)