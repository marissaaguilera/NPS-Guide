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


@app.route('/')
def homepage():
    """View homepage."""

    return render_template("homepage.html")

@app.route('/create-user')
def register():
    """Create a new user."""

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user: 
        flash('Cannot create an account with that email. Try again.')
    else: 
        crud.create_user(fname, lname, email, password)
        flash('Account created. Please login.')
    return redirect('/')


@app.route('/login')
def login():
    """User login."""

    #username and password 
    username = request.form.get('username')
    password = request.form.get('password')

    #check if they are already a user 
    # if they are a user send them to the explore page 
    # if they are not a user flash a message that to sign up

    #password invalid 
    #username invalid 

    user = crud.get_user_by_email(email)

    if user is None: 
        flash('Account does not exist.')
        return redirect('/')

    elif user.email != password: 
        flash('Incorrect Password')
        return redirect('/')

    elif user.email != email:
        flash('Incorrect Username')
        return redirect('/')
    
    elif user.password == password:
        session['user'] = email 
        session['user_id'] = user.user_id
        print('Successfully logged in!')
        return redirect('/explore')




    


# @app.route('/login')
# def login():
#     """View a login page."""

#     return render_template("root.html")




#Notes: 
#work on MVP and then return to this to see if i can implemenet react to my site 





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