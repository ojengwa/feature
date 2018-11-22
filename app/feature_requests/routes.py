from flask import (render_template, request, flash, redirect, url_for, jsonify)
from flask_login import login_user, current_user, login_required, logout_user

from . import feature_requests_blueprint
from app.models import FeatureRequest
from app import db


@feature_requests_blueprint.route('/')
def index():
    return render_template('feature_requests/list.html')


@feature_requests_blueprint.route('/my_feature_requests')
@login_required
def display_my_feature_requests():
    return render_template('feature_requests/list.html')

# API blueprints
@feature_requests_blueprint.route('/api/v1.0/feature_requests', methods=['GET'])
def get_feature_requests():
    return jsonify(FeatureRequest.query.all())

@feature_requests_blueprint.route('/api/v1.0/my_feature_requests', methods=['GET'])
@login_required
def get_my_feature_requests():
    return jsonify(current_user.feature_requests)

@feature_requests_blueprint.route('/api/v1.0/feature_requests/<int:feature_request_id>', methods=['GET'])
def get_feature_request(feature_request_id):
    feature_request = FeatureRequest.query.get_or_404(feature_request_id)
    return jsonify({'feature_request': feature_request})


@feature_requests_blueprint.route('/api/v1.0/feature_requests', methods=['POST'])
@login_required
def create_feature_request():
    
    if request.method == 'POST':
        if request.json:
            feature_request = FeatureRequest(**request.json)
            db.session.add(feature_request)
            db.session.commit()
            return jsonify(feature_request), 201
    abort(400)


@feature_requests_blueprint.route('/api/v1.0/feature_requests/<int:feature_request_id>', methods=['PUT'])
def update_feature_request(feature_request_id):
    feature_request = FeatureRequest.query.get_or_404(feature_request_id)
    if request.method == 'POST':
        if request.json:
            feature_request = FeatureRequest.query.update(**request.json).where(id=feature_request_id)
            db.session.add(feature_request)
            db.session.commit()
            return jsonify(feature_request), 200
    abort(400)



@feature_requests_blueprint.route('/api/v1.0/feature_requests/<int:feature_request_id>', methods=['DELETE'])
@login_required
def delete_feature_request(feature_request_id):
    FeatureRequest.query.get_or_404(feature_request_id)
    FeatureRequest.query.delete(feature_request_id)
    return jsonify({'result': True})
