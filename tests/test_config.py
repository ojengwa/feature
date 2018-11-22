import pytest
from datetime import datetime, timedelta
from app import create_app, db
from app.models import (User, FeatureRequest, Clients, ProductAreas)


@pytest.fixture(scope='module')
def new_user():
    user = User('bernard@gmail.com', 'uselessPassword')
    return user

@pytest.fixture(scope='module')
def new_feature_request():
    request = FeatureRequest(
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
        client=Clients.client_one,
        client_priority=1,
        available_on=datetime.now() + timedelta(days=30),
        product_area=ProductAreas.billing,
        requested_by=1)
        
    return request


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('app.config.TestConfig')

    client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield client

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()

    # Insert user data
    user1 = User(email='bernard@gmail.com', plain_password='whatpass1234')
    user2 = User(email='brytecore@gmail.com', plain_password='PaSsWoRd')

    db.session.add(user1)
    db.session.add(user2)

    # Insert feature request
    request1 = FeatureRequest(
        title='Lorem Ipsum',
        description=(
            'In publishing and graphic design, lorem ipsum is a'
            ' placeholder text used to demonstrate the visual form of a document'
            ' without relying on meaningful content. Replacing the actual content'
            ' with placeholder text allows designers to design the form of the'
            ' content before the content '),
        client=Clients.client_one,
        client_priority=1,
        available_on=datetime.now() + timedelta(days=30),
        product_area=ProductAreas.billing,
        requested_by=1)

    request2 = FeatureRequest(
        title='The Knight who say ni',
        description=(
            'There\'s antimony, arsenic, aluminum, selenium,'
            'And hydrogen and oxygen and nitrogen and rhenium,'
            'And nickel, neodymium, neptunium, germanium,'
            'And iron, americium, ruthenium, uranium,'
            'Europium, zirconium, lutetium, vanadium,'
            'And lanthanum and osmium and astatine and radium,'
            'And gold, protactinium and indium and gallium,'
            'And iodine and thorium and thulium and thallium. '),
        client=Clients.client_three,
        client_priority=4,
        available_on=datetime.now() + timedelta(days=4),
        product_area=ProductAreas.claims,
        requested_by=2)

    request3 = FeatureRequest(
        title='Stan Lee',
        description=(
            'There\'s yttrium, ytterbium, actinium, rubidium,'
            'And boron, gadolinium, niobium, iridium,'
            'There\'s strontium and silicon and silver and samarium,'
            'And bismuth, bromine, lithium, beryllium, and barium.'
            'There\'s holmium and helium and hafnium and erbium,'
            'And phosphorus and francium and fluorine and terbium,'
            'And manganese and mercury, molybdenum, magnesium,'
            'Dysprosium and scandium and cerium and cesium.'),
        client=Clients.client_three,
        client_priority=1,
        available_on=datetime.now() + timedelta(days=54),
        product_area=ProductAreas.claims,
        requested_by=1)

    db.session.add(request1)
    db.session.add(request2)
    db.session.add(request3)

    # Commit the changes to the DB
    db.session.commit()

    yield db

    db.drop_all()
