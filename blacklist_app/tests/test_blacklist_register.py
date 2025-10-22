import pytest
from flask import Flask
from flask_jwt_extended import JWTManager
from blacklist_app.app.api.api import BlacklistRegister

@pytest.fixture
def app():
    #Creamos una aplicacion de Flask para pruebas
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'supersecretkey'
    JWTManager(app)

    return app

def test_blacklist_register_campos_faltantes(app, mocker):
    #Mockeamos la verificacion del JWT para que siempre pase
    mocker.patch("flask_jwt_extended.view_decorators.verify_jwt_in_request")
    
    #Simulamos un request JSON con solo "email"
    with app.test_request_context(
        '/v1/blacklists',
        method = 'POST',
        json = {'email': 'test@example.com'},
    ):
        #Importamos la clase BlacklistRegister
        resource = BlacklistRegister()

        #Llamamos el metodo post a probar la validacion de campos faltantes
        response, status = resource.post()
        
        #Salidas esperadas
        assert status == 400
        assert response == {
            'msg': 'Hay campos necesarios que no están presentes en la solicitud'
        }
