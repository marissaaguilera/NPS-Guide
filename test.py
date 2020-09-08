"""Tests for NPS Flask app."""

from unittest import TestCase
from server import app  
from model import connect_to_db, db #, User #, example_data
from flask import session




class FlaskTestsBasics(TestCase):
    """Flask tests."""


    def setUp(self):
        """Code to run before every test."""

        #Get Flask test client
        self.client = app.test_client()
        #Show Flask errrors that happen during tests 
        app.config['TESTING'] = True


    def test_homepage(self):
        """Testing homepage."""

        result = self.client.get("/")
        self.assertIn(b"Welcome", result.data)


    def test_login(self):
        """Test login page."""

        result = self.client.post("/login", 
                                data={"email":"marissaeaguilera@gmail.com", "password":"hurry"}, 
                                follow_redirects=True)

        self.assertIn(b"You are a valued user", result.data)




class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""


    def setUp(self):
        """Code to run before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql://npsdb")

        # Create tables and add sample data
        db.create_all()
        example_data() #need to add this


    def tearDown(self):
        """Do at end of every test."""

    db.session.remove()
    db.drop_all()
    db.engine.dispose()


    def test_parks_list(self):
        """Test parks page."""

    result = self.client.get("/parks")
    self.assertIn(b"Parks Working", result.data) #change this


    def test_park_details(self):
        """Test park details page."""

    result = self.client.get("/parks/<park_id>")
    self.assertIn(b"Park Details Working", result.data) #change this



class FlaskTestsLoggedIn(TestCase):
    """Flask tests with user logged in to session."""

    def setUp(self):
        """Stuff to do before every test."""

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'
        self.client = app.test_client()

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1

    def test_parks_page(self):
        """Test important page."""

        result = self.client.get("/parks")
        self.assertIn(b"You are a valued user", result.data)


# flask test basic tests - test login not working 
# flask test database - not working due to example data 
# flask test logged in - not working 
# flask test logged out
# flask test log in log out 












#QUESTIONS
#do i need example data for testing?  yes need example data 
#test login doesnt work 
#do i need to have a set up and tear down wrapping each function - only need both once 



#test parks routes 
#activities available route 
# test create bucketlist and verify thing were added 
#run tests to see that things fail correctly 



if __name__ == '__main__':
    import unittest
    
    unittest.main()




#TESTING NOTES:    
#setup, test1, teardown (test login)
#setup, test2, teardown (test create user)
#python3 -m -v unittest test.py

