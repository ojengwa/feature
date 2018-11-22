"""
This file (test_feature_requests.py) contains the functional tests for the feature request blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the feature requests blueprint.
"""
from datetime import datetime, timedelta

def test_home_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Feature Request App!" in response.data
    assert b"Need an account?" in response.data
    assert b"Existing user?" in response.data


def test_my_feature_requests_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/my_feature_requests' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/my_feature_requests')
    assert response.status_code == 200
    assert b"Feature Request!" in response.data
    assert b"Need an account?" in response.data
    assert b"Existing user?" in response.data


def test_feature_requests_api(test_client):
    """
    GIVEN a Flask application
    WHEN the '/api/v1.0/feature_requests' page is requested (GET)
    THEN check that the response is a JSON array of feature requests
    """
    response = test_client.post('/api/v1.0/feature_requests')
    assert response.status_code == 200
    assert b"Welcome to the Feature Request App!" not in response.data


def test_my_feature_requests_api(test_client):
    """
    GIVEN a Flask application
    WHEN the '/api/v1.0/my_feature_requests' page is requested (GET)
    THEN check that the response is a JSON array of my feature requests
    """
    response = test_client.post('/api/v1.0/my_feature_requests')
    assert response.status_code == 200
    assert b"Welcome to the Feature Request App!" not in response.data


def test_feature_request_api(test_client):
    """
    GIVEN a Flask application
    WHEN the '/api/v1.0/feature_requests' page is requested (GET)
    THEN check that the response is a feature request JSON object
    """
    feature_request_id = 1
    response = test_client.post(
        '/api/v1.0/feature_requests/' + feature_request_id)
    assert response.status_code == 200
    assert b"Welcome to the Feature Request App!" not in response.data


def test_valid_create_feature_request(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/api/v1.0/feature_requests' page is posted to (POST)
    THEN check the response is valid and the user is logged in
    """
    feature = dict(
        title='Lorem Ipsum',
        description=(
            'And lead, praseodymium and platinum, plutonium,'
            'Palladium, promethium, potassium, polonium,'
            'And tantalum, technetium, titanium, tellurium,'
            'And cadmium and calcium and chromium and curium.'
            'There\'s sulfur, californium and fermium, berkelium,'
            'And also mendelevium, einsteinium, nobelium,'
            'And argon, krypton, neon, radon, xenon, zinc and rhodium,'
            'And chlorine, carbon, cobalt, copper, tungsten, tin and sodium.'
            'These are the only ones of which the news has come to Harvard,'
            'And there may be many others but they haven\'t been discovered.'),
        client='Client A',
        client_priority=1,
        available_on=datetime.now() + timedelta(days=30),
        product_area='Billings',
        requested_by=1)
    response = test_client.post('/api/v1.0/feature_requests',
                                data=feature)
    assert response.status_code == 201
    assert b"Thanks for registering, atticus@gmail.com!" in response.data
    assert b"Welcome atticus@gmail.com!" in response.data
    assert b"Feature Request App" in response.data
    assert b"Logout" in response.data
    assert b"Login" not in response.data
    assert b"Register" not in response.data

    """
    GIVEN a Flask application
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b"Goodbye!" in response.data
    assert b"Feature Request App" in response.data
    assert b"Logout" not in response.data
    assert b"Login" in response.data
    assert b"Register" in response.data


def test_invalid_registration(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/api/v1.0/feature_requests' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = test_client.post('/api/v1.0/feature_requests',
                                data=dict(email='bernard@gmail.com',
                                          password='IWillAddValue:)',
                                          confirm='IWillAddValue:)'),   # Does NOT match!
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"Thanks for registering, bernard@gotthejob.com!" not in response.data
    assert b"Welcome bernard@gotthejob.com!" not in response.data
    assert b"[This field is required.]" not in response.data
    assert b"Feature Request App" in response.data
    assert b"Logout" not in response.data
    assert b"Login" in response.data
    assert b"Register" in response.data
