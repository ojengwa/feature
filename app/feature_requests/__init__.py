"""
The feature_requests Blueprint handles the feature_request management for this application.
Specifically, this Blueprint allows for new feature_requests to be created, updated and 
viewed in the application.
"""
from flask import Blueprint, jsonify, make_response
feature_requests_blueprint = Blueprint('feature_requests', __name__, template_folder='templates')

from . import routes

@feature_requests_blueprint.errorhandler(403)
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)


@feature_requests_blueprint.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@feature_requests_blueprint.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
