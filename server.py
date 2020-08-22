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


########################## USER ROUTES ###################################

@app.route('/')
def homepage():
    """Shows the homepage."""

    return render_template('homepage.html')



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
        return redirect('/parks') 



@app.route('/register', methods=['GET'])
def show_registeration():
    """Shows registration form."""
   
    return render_template("registration.html")



@app.route('/register', methods=['POST'])
def create_user():
    """Get info from registration."""

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user: #checking if that email is in use already 
        flash('Cannot create an account with that email. Please try again.')
    else:
        crud.create_user(fname, lname, email, password)
        flash('Account created.')
        return redirect('/parks') #they are logged in and now can go to the parks page. 



@app.route('/logout', methods=['GET'])
def logout():
    """User logout."""

    if 'user' in session:
        del session['user']
        flash('Logged Out.')

        #or
    # session.pop('user', None)
    return redirect('/')


#FIX ME########
# @app.route('users/profile/<fname>')
# def show_user_profile(fname):
#     """Show users profile."""

#     user = crud.get_user_by_email(email)
#     user_bucketlist = crud.get_bucketlist_by_user(user_id)

#     return render_template('user_profile.html', user=user, user_bucketlist=user_bucketlist)

# pass


#FIX ME#########
# @app.route('/users/<user_id>')
# def show_user(user_id):
#     """Show the details on a particular user."""

#     user = crud.get_user_by_id(user_id)

#     return render_template('')

#     pass
#add an all users html page 


########################## PARK & ACTIVITY ROUTES ###################################

@app.route('/parks/<park_id>')
def show_park(park_id):
    """Show the details on a particular park."""

    park = crud.get_park_by_id(park_id)

    return render_template('park_details.html', park=park)



@app.route('/parks', methods=['GET'])
def all_parks():
    """Retrieve parks."""

    parks = crud.get_parks()

    return render_template('parks.html', parks=parks)



@app.route('/activities/<activity_id>')
def show_activity(activity_id):
    """Show the details on a particular activity."""

    activity = crud.get_activity_by_id(activity_id)

    return render_template('activity_details.html', activity=activity)



@app.route('/activities', methods=['GET'])
def get_activities():
    """Retrieve activities."""

    activities = crud.get_activities()

    return render_template('activities.html', activities=activities)


########################## BUCKETLIST ROUTES ###################################

# @app.route('')
# def create_bucketlist():
#     """Allows a user to create a bucketlist."""
#     pass


# @app.route('/bucketlist/<bucketlist_id>')
# def bucketlist_form(bucketlist_id):
#     """Show bucketlist form."""

#     bucketlist = crud.get_bucketlist_by_id(bucketlist_id)

#     return render_template('bucketlist.html', bucketlist=bucketlist)




# @app.route()
# def create_bucketlist():
#     """Handle creating a bucketlist."""
#     pass



# build out activities and activityi and activitiy id 


# build out a route to display the bucketlist form 
# and a route to handle submission of that form 
# allows you to ccreate a bucektlist 

#create a form , checkbox for each activitiy for the user to add an 
# activityi to their bucketlist

# then route to view bucketlist






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


#Post is used to send data 
#Get is used to request data 










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
