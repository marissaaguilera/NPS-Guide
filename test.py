"""Tests for NPS Flask app."""

from unittest import TestCase
from server import app  
from model import connect_to_db #db, example_data
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

#do i need a teardown here? 

#do i need a setup here? 
    def test_login(self):
        """Test login page."""

        result = self.client.post("/login", 
                                data={"email":"tammy.walsh@hotmail.com", "password":"wait"}, 
                                follow_redirects=True)
        self.assertIn(b"You are a valued user", result.data)

#do i need a tear down here? 


class FlaskTestDatabase(TestCase):
    """Flask tests that use the database."""


    def setUp(self):
        """Code to run before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql://npsdb")

        # Create tables and add sample data
        db.create_all()
        example_data()


    def tearDown(self):
    """Do at end of every test."""

    db.session.remove()
    db.drop_all()
    db.engine.dispose()


#   def test_some_flask_route(self):
#       """Some non-database test..."""

#       result = self.client.get("/my-route")
#       self.assertEqual(result.status_code, 200)
#       self.assertIn('<h1>Test</h1>', result.data)

def tearDown(self):
    """Code to run after every test."""






if __name__ == '__main__':
    unittest.main()




#TESTING NOTES:    
#setup, test1, teardown (test login)
#setup, test2, teardown (test create user)
#python3 -m -v unittest test.py

