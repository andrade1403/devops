from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager
from blacklist_app.app.db.blacklist_db import db
from blacklist_app.app.api.api import BlacklistRegister, BlacklistHealth, BlacklistToken

def create_app():
    #Creamos la aplicacion de Flask
    app = Flask(__name__)

    #Ponemos configuraciones de la app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@database-1.c5gmauekem4x.us-east-1.rds.amazonaws.com:5432/devops'
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

    return app
