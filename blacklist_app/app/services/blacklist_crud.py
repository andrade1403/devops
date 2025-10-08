from app.db.blacklist_db import db, Blacklist

class BlacklistCRUD:
    def __init__(self):
        self.session = db
    
    def addEmailToBlacklist(self, information: dict):
        try:
            #Creamos el nuevo registro
            new_blacklist_email = Blacklist(**information)

            #Hacemos persistencia
            self.session.add(new_blacklist_email)
            self.session.commit()

            return new_blacklist_email
        
        except Exception as e:
            self.session.rollback()
            raise e