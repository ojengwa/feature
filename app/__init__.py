from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate


# Create the instances of the Flask extensions (flask-sqlalchemy, flask-login, etc.) in
# the global scope, but without any arguments passed in. 
db = SQLAlchemy()
bcrypt = Bcrypt()
login = LoginManager()
login.login_view = "users.login"


def create_app(config_name=None):
    app = Flask(__name__)
    app.config.from_object(config_name)
    initialize_extensions(app)
    register_blueprints(app)
    return app


def initialize_extensions(app):
    # Pass the application instance to each Flask extension instance to
    #  bind it to the Flask application instance (app)

    db.init_app(app)
    bcrypt.init_app(app)
    login.init_app(app)

    # Flask-Migrate throws an error with the new pattern
    Migrate(app, db)

    # Flask-Login configuration
    from .models import User

    @login.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()


def register_blueprints(app):
    # Register each Blueprint with the Flask application instance (app)
    from .users import users_blueprint
    from .feature_requests import feature_requests_blueprint

    app.register_blueprint(users_blueprint)
    app.register_blueprint(feature_requests_blueprint)
