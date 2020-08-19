"""CRUD (create, read, update, delete) operations."""

#importing classes from model.py
from model import db, User, Park, Activity, ParkActivity, State, ParkState, Bucketlist, BucketlistItem, connect_to_db
from datetime import datetime


#Tables: User, Park, Activity, ParkActivity, State, ParkState, Bucketlist, BucketlistItem (8)


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

    return User.query.get(user_id).first()


def get_user_by_email(email):
    """Return a user by their email."""

    return User.query.filter(User.email == email).first()


def get_user_by_username(username):
    """Return a user by their username."""

    return User.query.filter(User.username == username).first()





#Park
def create_park(park_name, designation, siteURL):
    """Create and return a new park."""

    park = Park(park_name=park_name,  
                designation=designation, 
                siteURL=siteURL)
    
    db.session.add(park)
    db.session.commit()

    return park


def get_parks():
    """Return all parks."""

    return Park.query.all()
    # return Park.query.filter_by(Park.designation == 'National Park').all() #test this after i get data!


def get_park_by_id(park_id):
    """Return a park by primary key."""

    return Park.query.get(park_id).first()


def get_park_by_park_name(park_name):
    """Return a park by the park name."""

    return Park.query.filter(Park.park_name == park_name).first()






#Activity
def create_activity(activity_name):
    """Create and return a new activity."""

    activity = Activity(activity_name=activity_name)
    
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






#ParkActivity 
def create_park_activity(activity_id, park_id):
    """Create and return a new park/activity relationship."""

    park_activity = ParkActivity(activity_id=activity_id, 
                                park_id=park_id)
    
    db.session.add(park_activity)
    db.session.commit()

    return park_activity

def get_activities_by_park():
    """Return a park by the activitiy id."""

    return db.session.query(Activity, Park).join(Park).all()
#need to have db.session.query when using join 






#State 
def create_state(state_code):
    """Create and return a new bucketlist."""

    state = State(state_code=state_code)
    
    db.session.add(state)
    db.session.commit()

    return state

def get_states():
    """Return all states."""

    return State.query.all()

def get_state_by_id(state_id):
    """Return a state by primary key."""

    return State.query.get(state_id)

def get_state_by_state_code(state_code):
    """Return a state by the state code."""

    return State.query.filter(State.state_code == state_code).first()






#ParkState
def create_park_state(state_id, park_id):
    """Create and return a new park/state relationship."""

    park_state = ParkState(state_id=state_id, 
                park_id=park_id)
    
    db.session.add(park_state)
    db.session.commit()

    return park_state

def get_states_by_park():
    """Return a park by the state_id."""

    return db.session.query(Park, State).join(State).all()
#need to have db.session.query when using join 






#Bucketlist
def create_bucketlist(user_id, park_id):
    """Create and return a new bucketlist."""

    # user_id = get_user_by_id(user_id)
    # park_id = get_park_by_id(park_id)
    bucketlist = Bucketlist(user_id=user_id, 
                            park_id=park_id)

    return bucketlist

def get_bucketlists():
    """Return all bucketlists."""

    return Bucketlist.query.all()

def get_bucketlist_by_id(bucketlist_id):
    """Return a bucketlist by the primary key."""

    return Bucketlist.query.get(bucketlist_id)

def get_bucketlist_by_user(user_id):
    """Retrun all bucketlists by a user id."""
    # user_id = get_user_by_id(user_id)
    return Bucketlist.query.filter(Bucketlist.user_id == user_id).all()


def get_bucketlist_by_park(park_id):
    """Retrun a users bucketlist by a park id."""
    # park_id = get_park_by_id(park_id)
    return Bucketlist.query.filter(Bucketlist.park_id == park_id).all()





#BucketlistItem
def create_bucketlist_item(bucketlist_id, activity_id, order):
    """Create and return a bucketlist item."""

    item = BucketlistItem(bucketlist_id=bucketlist_id, 
                        activity_id=activity_id, 
                        order=order)

    db.session.add(item)
    db.session.commit()

    return item



if __name__ == '__main__':
    from server import app
    connect_to_db(app)


#MVP 
#user login, 
#new user registration
#choose park by search bar (user will type park)
#shows activities available at that park 
#add activities to bucketlist 