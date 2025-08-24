from flask import Flask
from .routes.api import api_bp
from .routes.views import views_bp
from app.db import mongo
from config import DB_URI,AUTH_EMAIL,AUTH_PWD
from .utils import mail
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    allow_origins = [
        "http://localhost:5000",
        "http://localhost:3000",
        "http://localhost:8000", 
        "https://horleng.vercel.app/"
    ]
    CORS(app, origins=allow_origins)


    app.config["MONGO_URI"] = DB_URI
    # Initialize PyMongo
    mongo.init_app(app)

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = AUTH_EMAIL
    app.config['MAIL_PASSWORD'] = AUTH_PWD
    mail.init_app(app)

    # Config
    app.config.from_object("config")

    # Register Blueprints
    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(views_bp)

    return app
