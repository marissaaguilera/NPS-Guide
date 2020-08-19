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


@app.route("/")
def root():
    return render_template("root.html")









# @app.route('/')
# def homepage():
#     """View homepage."""

#     return render_template('homepage.html')


#can i have the route the same as homepage since it is on there?
# @app.route('/login', methods=['POST'])
# def user_login():
#     """Login a user."""

#     username = request.form.get('username')
#     password = request.form.get('password')

#     user = crud.get_user_by_username(username)

#     if user is None:
#         flash('Username Error: Account does not exist')
#         return redirect('/')
    
#     elif user.password != password:
#         flash('Password Error: Incorrect password')
#         return redirect('/')
    
#     elif user.password == password:
#         session['user'] = username
#         session['user_id'] = user.user_id #or user_id 
#         print('user logged in', session['user_id'])
#         return redirect('/explore')



# @app.route('/register', methods=['POST'])
# def register_user():
#     """Create a new user."""

#     first_name = request.form.get('first_name')
#     last_name = request.form.get('last_name')
#     email = request.form.get('email')
#     username = request.form.get('username')
#     password = request.form.get('password')

#     user = crud.get_user_by_email(email)
#     if user:
#         flash('Email already associated with an account. Try again.')
#     else:
#         crud.create_user(first_name, last_name, email, username, password)
#         flash('Account successfully created. Please log in.')



# @app.route('/logout')
# def user_logout():
#     """Log out a user."""

#     if 'user' in session:
#         session['user']
#     session.pop('user', None) 

#     return redirect('/')




# @app.route('/explore')
# def choose_park():
#     """Search for parks on National Park Service API."""


#     states = request.args.get('states', '')
#     designation = request.args.get('designation', '')
#     fullName = request.args.get('fullName', '')

#     response = requests.get(url, params=payload)

#     data = response.json()
#     parks = data#what to put here 

#     return render_template('choose_park.html', 
#                             pformat=pformat,
#                             )







# @app.route('/activities')
# def activities():
#     """Shows all activities for that park."""



# @app.route('/bucketlist')
# def bucketlist():
    """Shows the user's bucketlist with their saved activities."""


# PAGES 
# homepage - login & new user registration are dropdown menus on homepage  
#login
#register
#logout
# choose park (search by state or type in park)
# activities available at park (includes a few pics of the park and activities can be saved to a bucketlist)
# bucketlist (this is a list that users can add activities to, list is per park)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')