"""Server for NPS Guide."""

from flask import (Flask, render_template, request, jsonify,
                    flash, session, redirect)
from model import User, connect_to_db
from datetime import datetime
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



@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login."""


    if request.method == 'POST':
        session.pop('user_id', None)

        email = request.form['email']
        password = request.form['password']

        user = crud.get_user_by_email(email)

        if not user:
            flash('Account does not exist. Please try again.')
            return redirect('/login')

        elif user.password != password: 
            flash('Incorrect Password. Please try again.')
            return redirect('/login')

        elif user:
            session['user'] = email
            session['user_id'] = user.user_id
            flash('Successfully logged in!')
            return redirect('/parks')

    return render_template('login.html')


def is_logged_in():
    """Checking if there is a user logged in."""

    return 'user_id' in session



def logged_in_user():
    """Get information on the user that is logged in."""
    
    user = User.query.get(session['user_id'])
    return user



@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration."""

    if request.method == 'POST':

        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        password = request.form.get('password')

        user = crud.get_user_by_email(email)

        if user: 
            flash('Cannot create an account with that email. Please try again.') #not working 
        else:
            crud.create_user(fname, lname, email, password)
            flash('Account created.') #not working 
            return redirect('/parks') 
    else:

        return render_template('registration.html')




@app.route('/logout', methods=['GET'])
def logout():
    """User logout."""

    if 'user' in session:
        del session['user']
        flash('Logged Out.')

    return redirect('/')


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



# @app.route('/search-parks', methods=['GET'])
# def search_parks(park_id):
#     """Using the search bar to go to a park park."""

#     park_id = request.form.get('park_id')
#     print('>>>>>>>>>>>>>HERE', park_id) 

#     # park_id = crud.get_park_by_id(park_id)

#     return redirect(f'/parks/{park_id}')


#post request to server when i want to change something 
#getting user (accessing user, show bucketlists)
#using user object to show all users bucketlist 
#loop over bucketlis - has park and park name 
# loop over bucketlistitem 


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

@app.route('/profile/<user_id>')
def user_profile(user_id):
    """Shows a users profile with all their bucketlists."""

    user = crud.get_user_by_id(user_id)
    bucketlists = crud.get_bucketlist_by_user(user_id)

  

    return render_template('user_profile.html', user=user, bucketlists=bucketlists)



@app.route('/bucketlists/<bucketlist_id>')
def get_specific_bucketlist(bucketlist_id):
    """Shows a user the details for a specific bucketlist."""

    bucketlist = crud.get_bucketlist_by_id(bucketlist_id)

    return render_template('bucketlist_details.html', bucketlist=bucketlist)




@app.route('/profile/bucketlists/<bucketlist_id>')
def select_bucketlist_from_profile(bucketlist_id):
    """A user can access a specific bucketlist from a link in their profile."""

    bucketlist = crud.get_bucketlist_by_id(bucketlist_id)

    return render_template('bucketlist_details.html', bucketlist=bucketlist)




@app.route('/adding-activities', methods=['POST', 'GET'])
def adding_to_a_bucketlist():
    """Creates a new bucketlist for a user."""

    user_id = session['user_id'] 

    park_id = request.form.get('park_id')
    #get park that is in hidden input 

    activity_list = request.form.getlist('activities')

    saved_dates = request.form.get('activity_date')
    print('>>>>>>>>>>>', saved_dates)


    #checking if user already has a bucketist with that park id 
    bucketlist = crud.get_bucketlist_by_park_and_user(park_id, user_id)

    if not bucketlist: 
        bucketlist = crud.create_bucketlist(user_id, park_id)
        print('>>>>>>>>no bucketlist found ') 

    for activity_id in activity_list:
        # int(activity_list[activity_id])
        new_bucketlist_item = crud.create_bucketlist_item(bucketlist.bucketlist_id, activity_id, datetime.now())

    
    return redirect(f'bucketlists/{bucketlist.bucketlist_id}')




# @app.route('/saving-order', methods=['GET', 'POST'])
# def saving_order():
#     """Saves the date that a user enters to complete activity."""

#     user_id = session['user_id']
#     print('>>>>>>>>>>>>',user_id)

#     saved_dates = request.form.get('activity-date')
#     print('>>>>>>>>>>>', saved_dates)

#     return redirect(f'bucketlists/{bucketlist.bucketlist_id}')





#maybe this route can be combining with one above? 

# javascript search for javascript and jquery 
# input and then pull it out
#see what info is given on the backend 
#convert to python date object to save to database 
#



if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')


#Post is used to send data 
#Get is used to request data 
