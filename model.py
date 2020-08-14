"""Models for national park service bucketlists."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()




class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String)
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
    state_code = db.Column(db.String)
    designation = db.Column(db.String)  #designation (national park, national monument, national rec area)
    siteURL = db.Column(db.String)

    activities = db.relationship('Activity')
    bucketlists = db.relationship('Bucketlist')

    def __repr__(self):
        return f'<Park park_id={self.park_id} park_name={self.park_name} state_code={self.state_code}>'


class Activity(db.Model):
    """An activity."""

    __tablename__ = 'activities'

    activity_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    activity_name = db.Column(db.String)
    park_id = db.Column(db.Integer, db.ForeignKey('parks.park_id'), nullable=False)

    # park = db.relationship('Park', backref='activities')
    park = db.relationship('Park')
    bucketlistitem = db.relationship('BucketlistItem')

    def __repr__(self):
        return f'<Activity activity_id={self.activity_id} activity_name={self.activity_name}>'


class Bucketlist(db.Model):
    """ A user's bucketlist."""
    #bucketlist is per park / different lists 

    __tablename__ = 'bucketlists'

    bucketlist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    park_id = db.Column(db.Integer, db.ForeignKey('parks.park_id'), nullable=False) #could have an orderby clause 
    
    user = db.relationship('User')
    park = db.relationship('Park')
    bucketlistitem = db.relationship('BucketlistItem')


    def __repr__(self):
        return f'<Bucketlist bucketlist_id={self.bucketlist_id} user_id={self.user_id} park_id={self.park_id} order={self.order}>'


class BucketlistItem(db.Model):
    """ An item in a bucketlist."""

    __tablename__ = 'bucketlistitems'


    item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    bucketlist_id = db.Column(db.Integer, db.ForeignKey('bucketlists.bucketlist_id'), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.activity_id'), nullable=False)
    order = db.Column(db.Integer, nullable=True) #favorite to least favorite / have order by date, time 
    #date of event = db.Column(db.dateTime) #ascending order by date in the bucketlist 
    #orderby as a field ()date option 
    bucketlists = db.relationship('Bucketlist')
    activities = db.relationship('Activity')

    def __repr__(self):
        return f'<Bucketlist Items item_id={self.item_id} bucketlist_id={self.bucketlist_id} activity_id={self.activity_id}>'




def connect_to_db(flask_app, db_uri='postgresql:///npsdb', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

#My database is called "npsdb"
#createdb npsdb, python3 -i model.py, db.create_all(), quit(), psql npsdb 

#python3 -i model.py
#psql npsdb (this gets me into my database)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)