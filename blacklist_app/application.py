import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from app.db.blacklist_db import db
from flask_jwt_extended import JWTManager
from app.api.api import BlacklistRegister, BlacklistHealth, BlacklistToken, BlacklistGetEmail, BlacklistDelete

#Creamos la aplicacion de Flask
application = Flask(__name__)

#Ponemos configuraciones de la app
application.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.getenv('RDS_USERNAME')}:{os.getenv('RDS_PASSWORD')}"
    f"@{os.getenv('RDS_HOSTNAME')}:{os.getenv('RDS_PORT')}/{os.getenv('RDS_DB_NAME')}"
)
application.config['JWT_SECRET_KEY'] = 'supersecretkey'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['PROPAGATE_EXCEPTIONS'] = True
application.config['JWT_TOKEN_LOCATION'] = ['headers']
application.config['JWT_HEADER_NAME'] = 'Authorization'
application.config['JWT_HEADER_TYPE'] = 'Bearer'
application.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600

#Inicializamos la base de datos
if not application.config.get('TESTING'):
    with application.app_context():
        db.init_app(application)
        db.create_all()

#Habilitamos CORS
CORS(application)

#Inicializamos el JWTManager
jwt = JWTManager(application)

#Registramos la API RESTful
api = Api(application)
api.add_resource(BlacklistRegister, '/v1/blacklists')
api.add_resource(BlacklistHealth, '/v1/blacklists/health')
api.add_resource(BlacklistToken, '/v1/blacklists/token')
api.add_resource(BlacklistGetEmail, '/v1/blacklists/<string:email>')
api.add_resource(BlacklistDelete, '/v1/blacklists/delete')

if __name__ == '__main__':
    application.run(port = 5000, debug = True)
