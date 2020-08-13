"""CRUD (create, read, update, delete) operations."""

#importing classes from model.py
from model import db, User, Park, Activity, Bucketlist, BucketlistItem, connect_to_db
# from datetime import datetime


#User
def create_user(username, fname, lname, email, password):
    """Create and return a new user."""

    user = User(username=username, 
                fname=fname,
                lname=lname, 
                email=email, 
                password=password)

    db.session.add(user)
    db.session.commit()

    return user


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary_key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by their email."""

    return User.query.filter(User.email == email).first()


def get_user_by_username(username):
    """Return a user by their username."""

    return User.query.filter(User.username == username).first()


#Park
def create_park(park_name, state_code, designation, imageURL):
    """Create and return a new park."""

    park = Park(park_name=park_name, 
                state_code=state_code, 
                designation=designation, 
                imageURL=imageURL)
    
    db.session.add(park)
    db.session.commit()

    return park


def get_parks():
    """Return all parks."""

    # Park.query.all()
    # return Park.query.all()
    return Park.query.filter(Park.designation == 'national park').all() #test this after i get data!


def get_park_by_id(park_id):
    """Return a park by primary key."""

    return Park.query.get(park_id)


def get_park_by_park_name(park_name):
    """Return a park by the park name."""

    return Park.query.filter(Park.park_name == park_name).first()


def get_parks_by_state(state_code):
    """Return parks by the state."""

    return Park.query.filter(Park.state_code == state_code).all()


def get_park_by_park_designation(designation):
    """Return a park by the park designation (ntl park, ntl monument, ntl rec area)."""

    return Park.query.filter(Park.designation == designation).first()


#Activity
def create_activity(activity_name, park, bucketlistitem):
    """Create and return a new activity."""

    activity = Activity(activity_name=activity_name, 
                        park=park, 
                        bucketlistitem=bucketlistitem)
    
    db.session.add(activity)
    db.session.commit()

    return activity


def get_activities():
    """Return all activities."""

    return Activity.query.all()


def get_activity_by_id(activity_id):
    """Return activity by primary key."""

    return Activity.query.get(activity_id)


def get_activity_name(activity_name):
    """Return an activity by the name."""

    return Activity.query.filter(Activity.activity_name == activity_name).first()


#Bucketlist
def create_bucketlist(user, park, bucketlistitem):
    """Create and return a new bucketlist."""

    bucketlist = Bucketlist(user=user, 
                            park=park, 
                            bucketlistitem=bucketlistitem)

    return bucketlist

def get_bucketlists():
    """Return all bucketlists."""

    return Bucketlist.query.all()

def get_bucketlist_by_id(bucketlist_id):
    """Return a bucketlist by the primary key."""

    return Bucketlist.query.get(bucketlist_id)

def get_bucketlist_by_user(user):
    """Retrun all bucketlists by a user."""

    return Bucketlist.query.filter(Bucketlist.user == user).all()


def get_bucketlist_by_park(park):
    """Retrun a users bucketlist by a park."""

    return Bucketlist.query.filter(Bucketlist.park == park).all()


#BucketlistItem
def create_bucketlist_item(bucketlist_id, item_id, activity_id):
    """Create and return a bucketlist item."""

    item = BucketlistItem(bucketlist_id=bucketlist_id, 
                        item_id=item_id, 
                        activity_id=activity_id)

    db.session.add(item)
    db.session.commit()

    return item

    # item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # bucketlist_id = db.Column(db.Integer, db.ForeignKey('bucketlists.bucketlist_id'), nullable=False)
    # activity_id = db.Column(db.Integer, db.ForeignKey('activities.activity_id'), nullable=False)
    # order = db.Column(db.Integer, nullable=True) #favorite to least favorite / have order by date, time 
    # #date of event = db.Column(db.dateTime) #ascending order by date in the bucketlist 
    # #orderby as a field ()date option 
    # bucketlists = db.relationship('Bucketlist')
    # activities = db.relationship('Activity')






#.all, .first, .filter, .get, .filterby

if __name__ == '__main__':
    from server import app
    connect_to_db(app)