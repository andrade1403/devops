import re
import uuid

class Helper:
    @staticmethod
    def validateUUID(app_id: str):
        try:
            #Intentamos convertir el appId a un objeto UUID
            uuid.UUID(app_id)
            return True
        
        except ValueError:
            return False

    @staticmethod
    def validateEmail(email: str):
        #Validamos que sea un string
        if not isinstance(email, str):
            return False
        
        #Expresion regular para validar el formato del email
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        return re.match(email_regex, email) is not None

    @staticmethod
    def getIpAddress(data: dict, request):
        #Obtenemos la ip del request si hay proxy
        if request.headers.get('X-Forwarded-For'):
            data['ipAddress'] = request.headers.get('X-Forwarded-For').split(',')[0]

        else:
            data['ipAddress'] = request.remote_addr
        
        return data