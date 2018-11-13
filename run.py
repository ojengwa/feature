import os
from app import create_app


# Call the Application Factory function to construct a Flask application instance
# using the standard configuration on the FLASK_CONFIG environment variable
#  or the default dev config
FLASK_CONFIG = os.getenv('FLASK_CONFIG', 'app.config.DevConfig')

app = create_app(FLASK_CONFIG)
