"""Server for NPS Guide."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined 

app = Flask(__name__)



@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


# PAGES 
# homepage
# login
# new user registration 
# choose park (search by state or type in park)
# activities available at park (includes a few pics of the park and activities can be saved to a bucketlist)
# bucketlist (this is a list that users can add activities to, list is per park)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')