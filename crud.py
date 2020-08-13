"""CRUD (create, read, update, delete) operations."""

from model import db, User, Park, Activity, Bucketlist, BucketlistItem, connect_to_db
#importing classes


#Users
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


def get_user_by_id(user_id):
    """Return a user by their ID/primary_key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by their email."""

    return User.query.filter(User.email == email).first()


def get_user_by_username(username):
    """Return a user by their username."""

    return User.query.filter(User.username == username).first()









if __name__ == '__main__':
    from server import app
    connect_to_db(app)