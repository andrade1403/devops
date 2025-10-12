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
    
    def getEmailFromBlacklist(self, email: str):
        try:
            #Buscamos el email en la base de datos
            blacklist_entry = self.session.query(Blacklist).filter_by(email=email).first()
            
            if blacklist_entry:
                return {
                    'email': blacklist_entry.email,
                    'found': True,
                    'blockedReason': blacklist_entry.blockedReason,
                }
            else:
                return {
                    'email': email,
                    'found': False,
                }
        
        except Exception as e:
            return str(e)