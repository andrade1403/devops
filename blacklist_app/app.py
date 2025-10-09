from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from app.db.blacklist_db import db
from flask_jwt_extended import JWTManager
from app.api.api import BlacklistRegister, BlacklistHealth, BlacklistToken

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

#Activamos contexto de la aplicacion
app_context = app.app_context()
app_context.push()

#Inicializamos la base de datos
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
