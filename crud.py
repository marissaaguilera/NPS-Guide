"""CRUD (create, read, update, delete) operations."""

from model import db, User, Park, Activity, Bucketlist, BucketlistItem, connect_to_db
#importing classes

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

def get_user():
    """Return all users."""
    
    return User.query.all()










if __name__ == '__main__':
    from server import app
    connect_to_db(app)