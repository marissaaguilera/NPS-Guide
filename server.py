"""Server for NPS Guide."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
import os
import sys
import requests
from jinja2 import StrictUndefined 

app = Flask(__name__)
app.secret_key = "lans"
app.jinja_env.undefined = StrictUndefined

# API_KEY = os.environ['NPS_KEY']



@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route('/explore')
def choose_park():
    """Search for parks on National Park Service API."""

#payload 
#api key
#res=request.get () should return req object

    #url wrong? 
    #am i doing this api in the right place? 
    #do i need a secrets.sh file if im creating tables with my api data 
    #do this again with the activities function or just once? 
    #does the data populate into a file or i have to create the file?

    url = 'https://developer.nps.gov/api/v1/parks?parkCode=acad&api_key=QtofanIIdwMJ4Q5FfVkKQPFGB1hjC0SOH3vdOb2e'
    payload = {'api_key' : 'NPS_KEY'}

    states = request.args.get('states', '')
    designation = request.args.get('designation', '')
    fullName = request.args.get('fullName', '')

    response = requests.get(url, params=payload)

    data = response.json()
    parks = data#what to put here 

    return render_template('choose_park.html', 
                            pformat=pformat,
                            )







@app.route('/activities')
def activities():
    """Shows all activities for that park."""

    url = 'https://developer.nps.gov/api/v1/parks?parkCode=acad&api_key=QtofanIIdwMJ4Q5FfVkKQPFGB1hjC0SOH3vdOb2e'
    payload = {'api_key' : 'NPS_KEY'}


@app.route('/bucketlist')
def bucketlist():
    """Shows the user's bucketlist with their saved activities."""


# PAGES 
# homepage - login & new user registration are dropdown menus on homepage  
# choose park (search by state or type in park)
# activities available at park (includes a few pics of the park and activities can be saved to a bucketlist)
# bucketlist (this is a list that users can add activities to, list is per park)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')