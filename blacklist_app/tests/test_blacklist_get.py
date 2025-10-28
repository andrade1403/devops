import pytest
from flask import Flask
from flask_jwt_extended import JWTManager
from app.api.api import BlacklistGetEmail
from unittest.mock import patch, MagicMock

@pytest.fixture
def app():
    # Create a Flask test app
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test-secret-key'
    JWTManager(app)
    return app

# Test cases for BlacklistGetEmail
def test_get_email_success(app, mocker):
    # Mock JWT verification
    mocker.patch('flask_jwt_extended.view_decorators.verify_jwt_in_request')
    
    # Mock the blacklist_crud.getEmailFromBlacklist method
    mock_response = {
        'found': True,
        'email': 'test@example.com',
        'appId': '123e4567-e89b-12d3-a456-426614174000',
        'blockedReason': 'Test reason',
        'createdAt': '2023-01-01T00:00:00',
        'ipAddress': '192.168.1.1'
    }
    
    with patch('app.api.api.blacklist_crud.getEmailFromBlacklist', return_value=mock_response):
        with app.test_request_context():
            resource = BlacklistGetEmail()
            response, status_code = resource.get('test@example.com')
            
            assert status_code == 200
            assert response == mock_response

def test_get_email_not_found(app, mocker):
    # Mock JWT verification
    mocker.patch('flask_jwt_extended.view_decorators.verify_jwt_in_request')
    
    # Mock the blacklist_crud.getEmailFromBlacklist method to return not found
    with patch('app.api.api.blacklist_crud.getEmailFromBlacklist', return_value={'found': False}):
        with app.test_request_context():
            resource = BlacklistGetEmail()
            response, status_code = resource.get('nonexistent@example.com')
            
            assert status_code == 404
            assert response == {'msg': 'El email nonexistent@example.com no se encuentra en la lista negra'}

def test_get_email_empty_parameter(app, mocker):
    # Mock JWT verification
    mocker.patch('flask_jwt_extended.view_decorators.verify_jwt_in_request')
    
    with app.test_request_context():
        resource = BlacklistGetEmail()
        response, status_code = resource.get('')
        
        assert status_code == 400
        assert response == {'msg': 'Se requiere un parámetro de búsqueda'}

def test_get_invalid_email_format(app, mocker):
    # Mock JWT verification
    mocker.patch('flask_jwt_extended.view_decorators.verify_jwt_in_request')
    
    with app.test_request_context():
        resource = BlacklistGetEmail()
        response, status_code = resource.get('invalid-email')
        
        assert status_code == 400
        assert response == {'msg': 'El email proporcionado no tiene un formato válido'}

# Test JWT protection
def test_get_email_unauthorized():
    # Don't mock JWT verification to test the decorator
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test-secret-key'
    JWTManager(app)
    
    with app.test_request_context():
        resource = BlacklistGetEmail()
        response = resource.get('test@example.com')
        # Should return a 401 Unauthorized when JWT is missing
        assert response[1] == 401  # 401 is the default status code for missing JWT