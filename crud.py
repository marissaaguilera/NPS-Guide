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
      # Returns a user object: <User user_id=71 email=michelle.valdez@gmail.com>


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary_key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by their email."""

    return User.query.filter(User.email == email).first()


def get_user_by_fname(fname):
    """Return a user by their email."""

    return User.query.filter(User.fname == fname).first()




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
#Returns park object: <Park park_id=20 park_name=Zion National Park>


def get_parks():
    """Return all parks."""

    return Park.query.all()


def get_park_by_id(park_id):
    """Return a park by primary key."""

    return Park.query.get(park_id)


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
#Returns activity object: <Activity activity_id=41 activity_name=Hiking>

def get_activities():
    """Return all activities."""

    return Activity.query.all()


def get_activity_by_id(activity_id):
    """Return activity by primary key."""

    return Activity.query.get(activity_id)


def get_activity_by_activity_name(activity_name):
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
#Returns ParkActivity object: <Park Activity activity_id=41 park_id=6>


def get_activities_by_park():
    """Return a park by the activitiy id."""

    # return Activity.query.filter((Activity.activity_id == park_id) | (Activity.activity_id == park_id)).all()    

    return db.session.query(Activity, Park).join(Activity).all()
#FIXME



#State 
def create_state(state_code):
    """Create and return a new bucketlist."""

    state = State(state_code=state_code)
    
    db.session.add(state)
    db.session.commit()

    return state
#Returns state object: <State state_id=56 state_code=CA>


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


def get_states_by_park(park_id):
    """Return states by the park_id."""

    return ParkState.query.filter(ParkState.park_id == park_id).all()


def add_states_by_park(park, park_state_codes):
    """Linking park to a specific state code."""

    for code in park_state_codes: #this list is coming from split [CA, OR, WA]
        state = get_state_by_state_code(code)
        parkstate = create_park_state(state.state_id, park.park_id)

        #this will give me state object from db 




#Bucketlist
def create_bucketlist(user_id, park_id):
    """Create and return a new bucketlist."""

    bucketlist = Bucketlist(user_id=user_id, park_id=park_id)
    
    db.session.add(bucketlist)
    db.session.commit()

    return bucketlist
    #Returns a bucketlist object: <Bucketlist bucketlist_id=5 user_id=2>


def get_bucketlists():
    """Return all bucketlists."""

    return Bucketlist.query.all()


def get_bucketlist_by_id(bucketlist_id):
    """Return a bucketlist by the primary key."""

    return Bucketlist.query.get(bucketlist_id)


def get_bucketlist_by_user(user_id):
    """Return all bucketlists by a user id."""

    return Bucketlist.query.filter(Bucketlist.user_id == user_id).all()


def get_bucketlist_by_park_and_user(park_id, user_id):
    """Return a users bucketlist by a park id."""
    # park_id = get_park_by_id(park_id)
    return Bucketlist.query.filter(Bucketlist.park_id == park_id, Bucketlist.user_id == user_id).first()


# def get_bucketlistitems_in_bucketlist():


#BucketlistItem
def create_bucketlist_item(bucketlist_id, activity_id, order):
    """Create and return a bucketlist item."""


    #won't tell me why im adding, maybe fix later 
    bucketlistitem = get_bucketlist_item_by_activity_and_bucketlist(activity_id=activity_id, bucketlist_id=bucketlist_id)

    if bucketlistitem is None: 

        bucketlistitem = BucketlistItem(activity_id=activity_id, 
                                        bucketlist_id=bucketlist_id, 
                                        order=order)
        db.session.add(bucketlistitem)
        db.session.commit()
    
    return bucketlistitem



def get_bucketlist_item_by_activity_and_bucketlist(activity_id, bucketlist_id):

    return BucketlistItem.query.filter(BucketlistItem.activity_id == activity_id, BucketlistItem.bucketlist_id == bucketlist_id).first()



def get_bucketlist_item_by_id(item_id):
    """Return a bucketlistitem by the primary key."""

    return BucketlistItem.query.get(item_id)




def update_bucketlistitem_order(item_id, order):


    item = get_bucketlist_item_by_id(item_id)

    item.order = order
    db.session.add(item)
    db.session.commit()

    return item






# def get_all_bucketlist_items(park_id):
#     """Returns all bucketlistitems by park."""
    
#     return BucketlistItem.query.filter(BucketlistItems.bucketlist.park.park_id)


# 2020-09-17

if __name__ == '__main__':
    from server import app
    connect_to_db(app)