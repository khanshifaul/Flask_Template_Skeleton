from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_migrate import Migrate
from flask_mail import Mail
from flask_login import LoginManager
from flask_config import Base

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
mail = Mail()
migrate = Migrate()

def create_app(config_class='Base'):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app)
    mail.init_app(app)
    from . import main
    from . import auth
    from . import user
    app.register_blueprint(main)
    app.register_blueprint(main)
    app.register_blueprint(user)
    return app

    
