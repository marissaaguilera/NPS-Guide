"""Models for national park service bucketlists."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


#Tables: User, Park, Activity, ParkActivity, State, ParkState, Bucketlist, BucketlistItem (8)

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    bucketlists = db.relationship('Bucketlist')

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'



class Park(db.Model):
    """A park."""

    __tablename__ = 'parks'

    park_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    park_name = db.Column(db.String, nullable=False)
    designation = db.Column(db.String)  #designation (ntl park, ntl monument, ntl rec area)
    siteURL = db.Column(db.String)

    # bucketlists = db.relationship('Bucketlist')
    states = db.relationship('State', secondary="parkstates")
    activities = db.relationship('Activity', secondary="parkactivities")
    parkstate = db.relationship('ParkState')
    bucketlists = db.relationship('Bucketlist')

    #check where the plurals 

    def __repr__(self):
        return f'<Park park_id={self.park_id} park_name={self.park_name}>'



class State(db.Model):
    """A state."""

    __tablename__ = 'states'

    state_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    state_code = db.Column(db.String)

    parks = db.relationship('Park', secondary="parkstates")
    parkstates = db.relationship('ParkState')
  
    def __repr__(self):
        return f'<State state_id={self.state_id} state_code={self.state_code}>'

#error; column has to be unique or else db won't know what to use, 
# foreign key should always be primary key of that table. 



class Activity(db.Model):
    """An activity."""

    __tablename__ = 'activities'

    activity_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    activity_name = db.Column(db.String)

    bucketlistitems = db.relationship('BucketlistItem')
    parks = db.relationship('Park', secondary="parkactivities")
    parkactivities = db.relationship('ParkActivity')

    def __repr__(self):
        return f'<Activity activity_id={self.activity_id} activity_name={self.activity_name}>'



class ParkActivity(db.Model):
    """A park and activity relationship."""

    __tablename__ = 'parkactivities'
    

    park_activity_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.activity_id'), nullable=False)
    park_id = db.Column(db.Integer, db.ForeignKey('parks.park_id'), nullable=False)

    park = db.relationship('Park')
    activity = db.relationship('Activity')
  
    #park to park activity is one to many 
    #activity to park activity is one to many 

    #relating a one single activity to one single park 
  
    def __repr__(self):
        return f'<Park Activity activity_id={self.activity_id} park_id={self.park_id}>'


#remember the one to many and many to many relationships 


class ParkState(db.Model):
    """A park and state relationship."""

    __tablename__ = 'parkstates'
    #park_state place underscore in between 

    parkstate_id = db.Column(db.Integer, autoincrement=True, primary_key=True) #maybe don't need this 
    state_id = db.Column(db.Integer, db.ForeignKey('states.state_id'), nullable=False)
    park_id = db.Column(db.Integer, db.ForeignKey('parks.park_id'), nullable=False)

    park = db.relationship('Park')
    state = db.relationship('State')

  
    def __repr__(self):
        return f'<Park State state_id={self.state_id} park_id={self.park_id}>'


class Bucketlist(db.Model):
    """ A user's bucketlist."""
    #bucketlist is per park / different lists 

    __tablename__ = 'bucketlists'

    bucketlist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    park_id = db.Column(db.Integer, db.ForeignKey('parks.park_id'), nullable=False)

    
    user = db.relationship('User')
    bucketlistitems = db.relationship('BucketlistItem')
    park = db.relationship('Park')
    activities = db.relationship('Activity', secondary='bucketlistitems')
#one bucketlist will have activies thorugh bucketlititems table 
    #bucketlistitem.park_activity.activity.activity_name 


    def __repr__(self):
        return f'<Bucketlist bucketlist_id={self.bucketlist_id} user_id={self.user_id}>'


class BucketlistItem(db.Model):
    """ An item in a bucketlist."""

    __tablename__ = 'bucketlistitems'

    item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    bucketlist_id = db.Column(db.Integer, db.ForeignKey('bucketlists.bucketlist_id'), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.activity_id'), nullable=False)
    order = db.Column(db.DateTime, nullable=True)
    #one bucketlist item is associated with one 
    #related to a single activity and a single park through park activity 
    
    bucketlists = db.relationship('Bucketlist')
    park = db.relationship('Park', secondary="bucketlists")
    activity = db.relationship('Activity')


    def __repr__(self):
        return f'<Bucketlist Items item_id={self.item_id} bucketlist_id={self.bucketlist_id}>'



def connect_to_db(flask_app, db_uri='postgresql:///npsdb', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app
    connect_to_db(app)

