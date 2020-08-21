"""Server for NPS Guide."""

from flask import (Flask, render_template, request, jsonify,
                    flash, session, redirect)
from model import connect_to_db
import crud
import os
import sys
import requests
import json

app = Flask(__name__)
app.secret_key = "lans"


########################## HOMEPAGE ###################################

@app.route('/')
def homepage():
    """Shows the homepage."""

    return render_template('root.html')


########################## LOGIN ###################################
# @app.route('/login')
# def show_login():
#     """Show login page."""

#     return render_template('login.html')

#do i need this route? 

#hit routes with fetch request and return a json 
#not using flash messages return 

@app.route('/api/login', methods=['POST'])
def login():
    """User login."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user is None: 

        return 
        #return a json dictionary 
        #define as status and return status as a key 
        # 

    elif user.email != password: 

    
    elif user.password == password:
        session['user'] = email 
        session['user_id'] = user.user_id
        print('Successfully logged in!')
        return

########################## CREATE USER ###################################

@app.route('/register', methods=['POST'])
def register():
    """Create a new user."""

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user: 
        flash('Cannot create an account with that email. Try again.')
        return redirect('/register')
    else: 
        crud.create_user(fname, lname, email, password)
        flash('Account created. Please login.')
    return redirect('/login')

########################## LOGOUT ###################################
@app.route('/logout', methods=['GET'])
def logout():
    """User logout."""

    if 'user' in session:
        session['user']
    session.pop('user', None)

    return redirect('/')

########################## GET USER ###################################

# @app.route('/get_user')
# def get_user():
#     """Get information on logged in user."""

#     user_fname = crud.get_user_by_fname(session['fname'])
#     # print(user_fname.fname)
#     return user_fname.fname

########################## SEARCH PARK ###################################

# @app.route('/explore')
# def search_park():
    """Search for parks on National Park Service API."""

# choose park (search by typing in the park and suggestions show up)
    # fullName = request.args.get('fullName')
    # states = request.args.get('states') 
    # response = requests.get(url, params=payload)

    # data = response.json()
    # parks = data#what to put here 

    # return render_template('choose_park.html', 
    #                         pformat=pformat)
                            
########################## VIEW/SAVE ACTIVTIES ###################################


# @app.route('/activities')
# def activities():
    """Shows all activities for that park."""
#activities available at park and activities can be saved to a bucketlist



# @app.route('/bucketlist')
# def bucketlist():
    # """Shows the user's bucketlist with their saved activities."""
# bucketlist (this is a list that users can add activities to, list is per park)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')



    ##PLAN: 
    #MVP FIRST
        #- user login
        #- user registration
        #- user logout 
        #- search parks
        #- view activities by park 
        #- add activities to bucketlist 