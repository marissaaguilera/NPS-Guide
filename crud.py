"""CRUD (create, read, update, delete) operations."""

#importing classes from model.py
from model import db, User, Park, Activity, ParkActivity, State, ParkState, Bucketlist, BucketlistItem, connect_to_db
from datetime import datetime


#Tables: User, Park, Activity, ParkActivity, State, ParkState, Bucketlist, BucketlistItem (8)


#User
def create_user(fname, lname, email, password):
    """Create and return a new user."""

    user = User(fname=fname,
                lname=lname, 
                email=email, 
                password=password)

    db.session.add(user)
    db.session.commit()

    return user
      # This is what it returns: <User user_id=71 email=michelle.valdez@gmail.com>


def get_users():
    """Return all users."""

    return User.query.all()
#returns me userd id and email 


def get_user_by_id(user_id):
    """Return a user by primary_key."""

    return User.query.get(user_id)
#returns me userd id and email 


def get_user_by_email(email):
    """Return a user by their email."""

    return User.query.filter(User.email == email).first()
#returns me userd id and email 

def get_user_by_fname(fname):
    """Return a user by their email."""

    return User.query.filter(User.fname == fname).first()
#returns me userd id and email 



#Park
def create_park(park_name, designation, siteURL):
    """Create and return a new park."""
    park = get_park_by_park_name(park_name)

    if not park:
        park = Park(park_name=park_name,  
                    designation=designation, 
                    siteURL=siteURL)
    
        db.session.add(park)
        db.session.commit()

    return park
#Returns this: <Park park_id=20 park_name=Zion National Park>

def get_parks():
    """Return all parks."""

    return Park.query.all()
#returns all parks and park ids 

def get_park_by_id(park_id):
    """Return a park by primary key."""

    return Park.query.get(park_id)
#returns park and park id 


def get_park_by_park_name(park_name):
    """Return a park by the park name."""

    return Park.query.filter(Park.park_name == park_name).first()
#returns park and park id 






#Activity
def create_activity(activity_name):
    """Create and return a new activity."""

    activity = Activity(activity_name=activity_name)
    
    db.session.add(activity)
    db.session.commit()

    return activity
#Returns this: <Activity activity_id=41 activity_name=Hiking>

def get_activities():
    """Return all activities."""

    return Activity.query.all()
#returns all activities

def get_activity_by_id(activity_id):
    """Return activity by primary key."""

    return Activity.query.get(activity_id)
#returns activity and activity id 


def get_activity_by_activity_name(activity_name):
    """Return an activity by the name."""

    return Activity.query.filter(Activity.activity_name == activity_name).first()
#returns activity and activity id 






#ParkActivity 
def create_park_activity(activity_id, park_id):
    """Create and return a new park/activity relationship."""

    park_activity = ParkActivity(activity_id=activity_id, 
                                park_id=park_id)
    
    db.session.add(park_activity)
    db.session.commit()

    return park_activity
#returns this: <Park Activity activity_id=41 park_id=6>


def get_activities_by_park(): #doesnt work 
    """Return a park by the activitiy id."""

    # return Activity.query.filter((Activity.activity_id == park_id) | (Activity.activity_id == park_id)).all()    

    return db.session.query(Activity, Park).join(Activity).all()



#State 
def create_state(state_code):
    """Create and return a new bucketlist."""

    state = State(state_code=state_code)
    
    db.session.add(state)
    db.session.commit()

    return state
#returns this: <State state_id=56 state_code=CA>

def get_states():
    """Return all states."""

    return State.query.all()
#returns all states

def get_state_by_id(state_id):
    """Return a state by primary key."""

    return State.query.get(state_id)
#returns state and state id

def get_state_by_state_code(state_code):
    """Return a state by the state code."""

    return State.query.filter(State.state_code == state_code).first()
#returns state and state id






#ParkState
def create_park_state(state_id, park_id):
    """Create and return a new park/state relationship."""

    park_state = ParkState(state_id=state_id, 
                park_id=park_id)
    
    db.session.add(park_state)
    db.session.commit()

    return park_state

def get_states_by_park(park_id):
    """Return a park by the state_id."""

    return ParkState.query.filter(ParkState.park_id == park_id).all()

    # return db.session.query(Park, State).join(State).all()
#need to have db.session.query when using join 

def add_states_by_park(park, park_state_codes):
    """Linking park to a specific state code."""

    for code in park_state_codes: #this list is coming from split [CA, OR, WA]
        state = get_state_by_state_code(code)
        parkstate = create_park_state(state.state_id, park.park_id)

        #this will give me state object from db 




#Bucketlist
def create_bucketlist(user_id, park_id):
    """Create and return a new bucketlist."""

    # user_id = get_user_by_id(user_id)
    # park_id = get_park_by_id(park_id)
    bucketlist = Bucketlist(user_id=user_id, 
                            park_id=park_id)
    
    db.session.add(bucketlist)
    db.session.commit()

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

    bucketlistitem = BucketlistItem(bucketlist_id=bucketlist_id, 
                        activity_id=activity_id, 
                        order=order)

    db.session.add(bucketlistitem)
    db.session.commit()

    return bucketlistitem



if __name__ == '__main__':
    from server import app
    connect_to_db(app)


#doesnt work
#get_activities_by_park
#create_park_state
#get_states_by_park
#add_states_by_park
#create_bucketlist
#get_bucketlist
#all of bucketlist and bucketlist item 