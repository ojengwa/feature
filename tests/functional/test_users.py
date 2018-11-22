"""
This file (test_users.py) contains the functional tests for the users blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the users blueprint.
"""


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


def test_home_page_post(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is is posted to (POST)
    THEN check that a '405' status code is returned
    """
    response = test_client.post('/')
    assert response.status_code == 405
    assert b"Welcome to the Feature Request App!" not in response.data


def test_login_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/login' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/login')
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Email" in response.data
    assert b"Password" in response.data


def test_valid_login_logout(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/login',
                                data=dict(
                                    email='bernard@gmail.com',
                                          password='whatpass1234'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"Thanks for logging in, bernard@gmail.com!" in response.data
    assert b"Welcome bernard@gmail.com!" in response.data
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


def test_invalid_login(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/login' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = test_client.post('/login',
                                data=dict(email='bernard@gmail.com',
                                          password='badPa33w04d'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"ERROR! Incorrect login credentials." in response.data
    assert b"Feature Request App" in response.data
    assert b"Logout" not in response.data
    assert b"Login" in response.data
    assert b"Register" in response.data


def test_valid_registration(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/register' page is posted to (POST)
    THEN check the response is valid and the user is logged in
    """
    response = test_client.post('/register',
                                data=dict(email='atticus@gmail.com',
                                          password='toKillaJayBird',
                                          confirm='toKillaJayBird'),
                                follow_redirects=True)
    assert response.status_code == 200
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
    WHEN the '/register' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = test_client.post('/register',
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
