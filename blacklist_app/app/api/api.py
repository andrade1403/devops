from flask import jsonify
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
        return jsonify({'token': token}), 200

class BlacklistRegister(Resource):
    @jwt_required()
    def post(self):
        #Extraemos datos del request
        data = request.get_json()
        
        #Validamos que todos los campos necesarios esten presentes
        if not all(key in data for key in ('email', 'appId')):
            return jsonify({"msg": 'Hay campos necesarios que no están presentes en la solicitud'}), 400

        #Validamos que el email tenga un formato correcto
        if not Helper.validateEmail(data.get('email')):
            return jsonify({'msg': 'El email proporcionado no tiene un formato válido'}), 400
        
        #Validamos que el appId sea un UUID valido
        if not Helper.validateUUID(data.get('appId')):
            return jsonify({'msg': 'El appId proporcionado no es un UUID válido'}), 400
        
        #Obtenemos ip del request
        data = Helper.getIpAddress(data, request)

        #Validamos si se pudo obtener la ip
        if not data.get('ipAddress'):
            return jsonify({'msg': 'No se pudo obtener la dirección IP del cliente'}), 400

        #Guardamos el email en base de datos
        salida = blacklist_crud.addEmailToBlacklist(data)

        #Validamos si hubo un error al guardar en base de datos
        if isinstance(salida, str):
            return jsonify({'msg': f'Error al agregar el email a la lista negra: {salida}'}), 500

        return jsonify({'msg': 'Usuario agregado a la lista negra exitosamente'}), 200
        
class BlacklistHealth(Resource):
    def get(self):
        return jsonify({'status': 'pong'}), 200