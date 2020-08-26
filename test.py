"""Tests for NPS Flask app."""

from unittest import TestCase
from server import app  

#setup, test1, teardown (test login)
#setup, test2, teardown (test create user)

class NPSFlaskTests(TestCase):
    """Tests for my NPS site."""


def setUp(self):
    """Code to run before every test."""

    #Get Flask test client
    self.client = app.test_client()
    #Show Flask errrors that happen during tests 
    app.config['TESTING'] = True

def test_login(self):
    """Test login page."""

    result = self.client.post("/login", 
                            data={}, 
                            follow_redirects=True)
    self.assertIn(b"You are a valued user", result.data)


#   def test_some_flask_route(self):
#       """Some non-database test..."""

#       result = self.client.get("/my-route")
#       self.assertEqual(result.status_code, 200)
#       self.assertIn('<h1>Test</h1>', result.data)

def tearDown(self):
    """Code to run after every test."""


#python3 -m -v unittest test.py


#Testing Flask and databases
def setUp(self):
    """Code to run before every test."""


    self.client = app.test_client()
    app.config['TESTING'] = True

    connect_to_db(app, "postgresql://testdb")

    db.create_all()
    example_data()


if __name__ == '__main__':
    unittest.main()