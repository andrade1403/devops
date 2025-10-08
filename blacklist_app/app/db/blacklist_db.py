import uuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

#Creamos base de datos
db = SQLAlchemy()

class Blacklist(db.Model):
    __tablename__ = 'blacklist'
    
    id = db.Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    email = db.Column(db.String(255), unique = True, nullable = False)
    appId = db.Column(UUID(as_uuid = True), nullable = False)
    blockedReason = db.Column(db.String(255), nullable = True)
    ipAddress = db.Column(db.String(45), nullable = False)
    createdAt = db.Column(db.DateTime, server_default = db.func.now())