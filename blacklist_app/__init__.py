from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager
from blacklist_app.app.db.blacklist_db import db
from blacklist_app.app.api.api import BlacklistRegister, BlacklistHealth, BlacklistToken, BlacklistDelete

def create_app():
    #Creamos la aplicacion de Flask
    app = Flask(__name__)

    #Ponemos configuraciones de la app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://proyectogrupo10:proyectogrupo10@terraform-20251011113807389200000001.cifuwoics1ov.us-east-1.rds.amazonaws.com:5432/proyect_db'
    app.config['JWT_SECRET_KEY'] = 'supersecretkey'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_HEADER_NAME'] = 'Authorization'
    app.config['JWT_HEADER_TYPE'] = 'Bearer'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600

    #Inicializamos la base de datos
    with app.app_context():
        db.init_app(app)
        db.create_all()

    #Habilitamos CORS
    CORS(app)

    #Inicializamos el JWTManager
    jwt = JWTManager(app)

    #Registramos la API RESTful
    api = Api(app)
    api.add_resource(BlacklistRegister, '/blacklists')
    api.add_resource(BlacklistHealth, '/blacklists/health')
    api.add_resource(BlacklistToken, '/blacklists/token')
    api.add_resource(BlacklistDelete, '/blacklists/delete')

    return app
