import jwt
import datetime
from config import BasicConfig
from app import db,bcrypt

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    email = db.Column(db.String(255),unique=True,nullable = False)
    password = db.Column(db.String(255),nullable = False)
    registered_on=db.Column(db.DateTime,nullable=False)
    admin = db.Column(db.Boolean,nullable = False)

    def __init__(self,email,password,admin=False) -> None:
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password,BasicConfig.BCRYPT_LOG_ROUNDS
        ).decode()
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def enconde_auth_token(self,user_id):
        try:
            payload={
                'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=10),
                'iat':datetime.datetime.utcnow(),
                'sub':user_id
            }
            print(payload)
            return jwt.encode(
                payload,
                BasicConfig.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            print(e)
            return e
    
    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload= jwt.decode(auth_token,BasicConfig.SECRET_KEY,algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError as e:
            return 'Signature Expired Please log in again'
        except jwt.InvalidTokenError as e:
            return 'Invalid token'

class Images(db.Model):
    __tablename__ = 'user_images'
    id_images = db.Column(db.Integer,primary_key =True)
    type = db.Column(db.String(255),nullable=False)
    data = db.Column(db.LargeBinary,nullable=False)
    rendered_data = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    region = db.relationship('User',backref='users')