"""CRUD (create, read, update, delete) operations."""

#importing classes from model.py
from model import db, User, Park, Activity, Bucketlist, BucketlistItem, connect_to_db


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

    return Park.query.filter(Park.designation == 'national park') #test this!


def get_park_by_id(park_id):
    """Return a park by primary key."""

    return Park.query.get(park_id)








if __name__ == '__main__':
    from server import app
    connect_to_db(app)