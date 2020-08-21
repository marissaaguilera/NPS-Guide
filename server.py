"""Server for NPS Guide."""

from flask import (Flask, render_template, request, jsonify,
                    flash, session, redirect)
from model import connect_to_db
import crud
import os
import sys
import requests
import json
from jinja2 import StrictUndefined

"""Server for nps app."""
app = Flask(__name__)
app.secret_key = "lans"
app.jinja_env.undefined = StrictUndefined


########################## HOMEPAGE ###################################

@app.route('/')
def homepage():
    """Shows the homepage."""

    return render_template('homepage.html')

#this shows on my site 
########################## LOGIN ###################################
@app.route('/login', methods=['GET'])
def show_login():
    """Show login form."""

    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    """User login."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)


    if not user: 
        flash('Account does not exist. Please try again.')
        return redirect('/login')

    elif user.email != password: 
        flash('Incorrect Password. Please try again.')
        return redirect('/login')
    
    elif user.password == password:
        session['user'] = email 
        session['user_id'] = user.user_id
        print('Successfully logged in!')
        return redirect('/api/search-park')
        # return render_template('choose_park.html')


########################## CREATE USER ###################################


@app.route('/register', methods=['GET', 'POST'])
def create_user():
    """Get info from registration."""
    
    if request.method == 'POST':
        crud.create_user(request.form['fname'], request.form['lname'],
                         request.form['email'], request.form['password'])

    return render_template("registration.html")

#this shows on my site 

########################## LOGOUT ###################################
@app.route('/logout', methods=['GET'])
def logout():
    """User logout."""

    if 'user' in session:
        del session['user']
        flash('Logged Out.')

        #or
    # session.pop('user', None)
    return redirect('/')


########################## SEARCH PARK ###################################

@app.route('/api/search-park')
def search_park():
    """Search for parks on National Park Service API."""

    park = get_park_by_park_name(park_name)

    return render_template('choose_park.html')
#this park shows 
                            
########################## VIEW/SAVE ACTIVTIES ###################################


@app.route('/activities')
def activities():
    """Shows all activities for that park."""
#activities available at park and activities can be saved to a bucketlist
pass

########################## BUCKETLIST ###################################

# @app.route('/bucketlist')
# def bucketlist():
    # """Shows the user's bucketlist with their saved activities."""
# bucketlist (this is a list that users can add activities to, list is per park)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')



    ##PLAN: 
    #MVP FIRST
        #- user login (implement on html, js file)
        #- user registration (implement on html, js file)
        #- user logout (implement on html, js file)
        #- search parks (all)
        #- view activities by park (all)
        #- add activities to bucketlist (all)










########################## MOVING TO REACT ###################################
#react LOGIN
# @app.route('/api/login', methods=['POST'])
# def login():
#     """User login."""

#     data = request.get_json(force=True)
#     #get_json converts the JSON object into python data for us and 
#     #returns an object or none if ssilent = true
#     email = data['email']
#     password = data['password']

#     user = crud.get_user_by_email(email)

#     if user: 
#         full_name = user.fname + user.lname
#         session['user'] = email 
#         session['user_id'] = user.user_id
#         #full_name = f'{user.fname} {user.lname}'

#         if (user.email == email) and (user.password == password):
#             return jsonify([user.user_id, full_name, user.email])

#     else: 
#         return jsonify({'Account not found. Please register.'})


#react REGISTRATION
# @app.route('/register', methods=['POST'])
# def register():
#     """Create a new user."""
#     data = request.get_json(force=True)
#     fname = data['fname']
#     lname = data['lname']
#     email = data['email']
#     password = data['password']

#     user = crud.create_user(fname, lname, email, password)

#     # user = crud.get_user_by_email(email)

#     if user: 
#         session.clear()
#         return jsonify({'Account created. Please login.'})
