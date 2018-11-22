import enum
from datetime import datetime

from app import db, bcrypt


class User(db.Model):
    '''
    Class that represents a user of the application

    The following attributes of a user are stored in this table:
        email address
        password (hashed using Bcrypt)
        authenticated flag (indicates if a user is logged in or not)
        date that the user registered on
    '''

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    hashed_password = db.Column(db.Binary(60), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    created_on = db.Column(db.DateTime, nullable=True)
    role = db.Column(db.String, default='user')
    feature_requests = db.relationship('FeatureRequest')

    def __init__(self, email, plain_password, role='user'):
        self.email = email
        self.hashed_password = bcrypt.generate_password_hash(plain_password)
        self.authenticated = False
        self.created_on = datetime.now()
        self.role = role

    def set_password(self, plain_password):
        self.hashed_password = bcrypt.generate_password_hash(plain_password)

    def is_correct_password(self, plain_password):
        return bcrypt.check_password_hash(self.hashed_password, plain_password)

    @property
    def is_authenticated(self):
        '''Return True if the user is authenticated.'''
        return self.authenticated

    @property
    def is_active(self):
        '''Always True, as all users are active.'''
        return True

    @property
    def is_anonymous(self):
        '''Always False, as anonymous users aren't supported.'''
        return False

    def get_id(self):
        '''Return the id of a user to satisfy Flask-Login's requirements.'''
        return str(self.id)

    def __repr__(self):
        return '<User {}>'.format(self.email)


class Clients(enum.Enum):
    client_one = 'Client A'
    client_two = 'Client B'
    client_three = 'Client C'


class ProductAreas(enum.Enum):
    policies = 'Policies'
    billing = 'Billing'
    claims = 'Claims'
    reports = 'Reports'


class FeatureRequest(db.Model):
    '''
    Class that represents a feature request by a user

    The following attributes of a feature are stored in this table:
        title
        description
        client ( 'Client A', 'Client B', 'Client C')
        client priority: A numbered priority according to the client (1...n).
         Client Priority numbers should not repeat for the given client, 
         so if a priority is set on a new feature as '1', then all other
          feature requests for that client should be reordered.
        The date that the client is hoping to have the feature.
        A selection list of product areas ('Policies', 'Billing', 'Claims', 'Reports')
    '''

    __tablename__ = 'feature_requests'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    client = db.Column(db.Enum(Clients), nullable=False)
    client_priority = db.Column(db.Integer)
    assigned_priority = db.Column(db.Integer)
    product_area = db.Column(db.Enum(ProductAreas), nullable=False)
    available_on = db.Column(db.DateTime, nullable=True)
    requested_by = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, title, description, client, client_priority,
                 available_on, product_area, requested_by):
        self.title = title
        self.description = description
        self.client = client
        self.client_priority = client_priority
        self.assigned_priority = client_priority
        self.product_area = product_area
        self.available_on = available_on
        self.requested_by = requested_by

    def get_id(self):
        '''Return the id of a user to satisfy Flask-Login's requirements.'''
        return str(self.id)

    def __repr__(self):
        return '<Feature Request {0} from {1}>'.format(self.title, self.requested_by)

    def save(self):
        super(FeatureRequest, self).save()
        

@db.event.listens_for(FeatureRequest.client_priority, 'modified')
def tabulate_priorities(feature_request, event):
    FeatureRequest.query.filter_by(
        client_priority=feature_request.client_priority,
        client=feature_request.client).update(
        {
            'assigned_priority': FeatureRequest.assigned_priority + 1
        }
    )
