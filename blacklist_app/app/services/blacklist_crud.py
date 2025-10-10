from blacklist_app.app.db.blacklist_db import db, Blacklist

class BlacklistCRUD:
    def __init__(self):
        self.session = db.session
    
    def addEmailToBlacklist(self, information: dict):
        try:
            #Creamos el nuevo registro
            new_blacklist_email = Blacklist(**information)

            #Hacemos persistencia
            self.session.add(new_blacklist_email)
            self.session.commit()
        
        except Exception as e:
            self.session.rollback()
            return str(e)
    
    def deleteAllBlacklist(self):
        try:
            #Borramos todos los registros
            self.session.query(Blacklist).delete()

            #Hacemos persistencia
            self.session.commit()
        
        except Exception as e:
            self.session.rollback()
            return str(e)