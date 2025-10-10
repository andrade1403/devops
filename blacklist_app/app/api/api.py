from flask import request
from flask_restful import Resource
from blacklist_app.app.utils.helper import Helper
from blacklist_app.app.services.blacklist_crud import BlacklistCRUD
from flask_jwt_extended import jwt_required, create_access_token

#Creamos instancia del CRUD
blacklist_crud = BlacklistCRUD()

class BlacklistToken(Resource):
    def post(self):
        #Creamos token JWT
        token = create_access_token(identity = 'blacklist_service')
        return {'token': token}, 200

class BlacklistRegister(Resource):
    @jwt_required()
    def post(self):
        #Validamos que el request tenga JSON válido
        try:
            data = request.get_json()
        except Exception:
            return {'msg': 'El cuerpo de la solicitud debe ser JSON válido'}, 400

        #Validamos que data no sea None
        if data is None:
            return {'msg': 'El cuerpo de la solicitud no puede estar vacío'}, 400

        #Validamos que todos los campos necesarios esten presentes
        if not all(key in data for key in ('email', 'appId')):
            return {"msg": 'Hay campos necesarios que no están presentes en la solicitud'}, 400

        #Validamos que los campos no estén vacíos
        if not data.get('email') or not data.get('email').strip():
            return {'msg': 'El campo email no puede estar vacío'}, 400

        if not data.get('appId') or not data.get('appId').strip():
            return {'msg': 'El campo appId no puede estar vacío'}, 400

        #Validamos que el email tenga un formato correcto
        if not Helper.validateEmail(data.get('email').strip()):
            return {'msg': 'El email proporcionado no tiene un formato válido'}, 400

        #Validamos que el appId sea un UUID valido
        if not Helper.validateUUID(data.get('appId').strip()):
            return {'msg': 'El appId proporcionado no es un UUID válido'}, 400

        #Validamos la longitud del campo reason si está presente
        if 'reason' in data and data.get('reason'):
            if len(data.get('reason').strip()) > 255:
                return {'msg': 'El campo reason no puede exceder 255 caracteres'}, 400

        #Normalizamos los datos
        data['email'] = data.get('email').strip().lower()
        data['appId'] = data.get('appId').strip()
        if 'reason' in data and data.get('reason'):
            data['reason'] = data.get('reason').strip()

        #Obtenemos ip del request
        data = Helper.getIpAddress(data, request)

        #Validamos si se pudo obtener la ip
        if not data.get('ipAddress'):
            return {'msg': 'No se pudo obtener la dirección IP del cliente'}, 400

        #Guardamos el email en base de datos
        salida = blacklist_crud.addEmailToBlacklist(data)

        #Validamos si hubo un error al guardar en base de datos
        if isinstance(salida, str):
            return {'msg': f'Error al agregar el email a la lista negra: {salida}'}, 500

        return {'msg': 'Usuario agregado a la lista negra exitosamente'}, 200
        
class BlacklistHealth(Resource):
    def get(self):
        return {'status': 'pong'}, 200