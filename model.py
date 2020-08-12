"""Models for park service app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column()
    fname = db.Column()
    lname = db.Column()
    email = db.Column()
    password = db.Column()

    def __repr__(self):
        return f'<User user_id={self.user_id} fname={self.fname} email={self.email}>'


class Park(db.Model):
    """A park."""

    __tablename__ = 'parks'

    park_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    activity_id = db.Column(db.Integer)
    things_to_do_id = db.Column(db.Integer)

    #add columns
    #add repr

class Bucketlist(db.Model):
    """ A bucketlist."""

    __tablename__ = 'bucketlists'

    #add columns
    #add repr

class BucketlistItem(db.Model):
    """ An item in a bucketlist."""

    __tablename__ = 'bucketlistitems'

    #add columns
    #add repr


#create connect to db function 
#add SQLAlchemy URI, Echo, track modifications 




if __name__ == '__main__':
    from server import app
    # connect_to_db(app)

#maybe try from an api at first and then maybe try a table
# problems with apis is that too many requests might slow me down.

#write a class/structure to a table