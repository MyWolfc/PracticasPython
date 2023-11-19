from flask import Flask
from flask_cors import CORS
from database import db
from encriptador import bcrypt
from flask_migrate import Migrate
from config import BasicConfig
from routes.user.user import appuser
from routes.imagenes.Imagen import imagenuser

app = Flask(__name__)
app.config.from_object(BasicConfig)
CORS(app)
app.register_blueprint(appuser)
app.register_blueprint(imagenuser)
bcrypt.init_app(app)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)