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

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


class Park(db.Model):
    """A park."""

    __tablename__ = 'parks'

    park_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    park_name = db.Column(db.String, nullable=False)
    state_code = db.Column(db.String)
    designation = db.Column(db.String)  #designation (national park, national monument, national rec area)
    imageURL = db.Column(db.String)

    def __repr__(self):
        return f'<Park park_id={self.park_id} park_name={self.park_name} state_code={self.state_code}>'


class Activity(db.Model):
    """An activity."""

    __tablename__ = 'activities'

    activity_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    activity_name = db.Column(db.String)
    park_id = db.Column(db.Integer, db.ForeignKey('parks.park_id'), nullable=False)

    park = db.relationship('Park', backref='bucketlists')

    def __repr__(self):
        return f'<Activity activity_id={self.activity_id} activity_name={self.activity_name}>'


class Bucketlist(db.Model):
    """ A user's bucketlist."""

    __tablename__ = 'bucketlists'

    bucketlist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False) #when do you and dont you place nullable? 
    park_id = db.Column(db.Integer, db.ForeignKey('parks.park_id'), nullabl=False)
    order = db.Column(db.Integer)

    user = db.relationship('User', backref='bucketlists')
    park = db.relationship('Park', backref='bucketlists')


    def __repr__(self):
        return f'<Bucketlist bucketlist_id={self.bucketlist_id} user_id={self.user_id} 
                park_id={self.park_id} order={self.order}>'


class BucketlistItem(db.Model):
    """ An item in a bucketlist."""

    __tablename__ = 'bucketlistitems'


    item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    bucketlist_id = db.Column(db.Integer, db.ForeignKey('bucketlist.bucketlist_id'), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.activity_id'), nullable=False)

    bucketlist = db.relationship('Bucketlist', backref='bucketlists')
    activity = db.relationship('Activity', backref='bucketlists')

    def __repr__(self):
        return f'<Bucketlist Items item_id={self.item_id} bucketlist_id={self.bucketlist_id} 
                activity_id={self.activity_id}>'




def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')



if __name__ == '__main__':
    from server import app
    connect_to_db(app)