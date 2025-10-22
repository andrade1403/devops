import pytest
from application import application

@pytest.fixture()
def app():
    #Creamos la aplicacion con configuracion de prueba
    application.config.update({
        'TESTING': True,
    })

    yield application

@pytest.fixture()
def client(app):
    return app.test_client()