import os

class BaseConfig(object):
    WTF_CSRF_ENABLED = True

    # os.urandom(32).hex()
    SECRET_KEY = '866345de20e7cff5bf074c9319028d2a372e25f1b99f52323ae9ea4b7fd1a152'

    DB_PASS = 'GziP(Mszc!2V'

    # Get the folder of the top-level directory of this project
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, '../app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    WTF_CSRF_ENABLED = True


class TestConfig(BaseConfig):
    
    DEBUG = True

    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, '../app_test.db')

    # Enable the TESTING flag to disable the error catching during request handling
    # so that you get better error reports when performing test requests against the application.
    TESTING = True

    # Bcrypt algorithm hashing rounds (reduced for testing purposes only!)
    BCRYPT_LOG_ROUNDS = 4
    
    # Disable CSRF tokens in the Forms
    WTF_CSRF_ENABLED = False


class ProductionConfig(BaseConfig):
    DEBUG = False
    SECRET_KEY = os.environ['SECRET_KEY']

    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI', 'sqlite:///' + os.path.join(BASEDIR, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Bcrypt algorithm hashing rounds
    BCRYPT_LOG_ROUNDS = 15
