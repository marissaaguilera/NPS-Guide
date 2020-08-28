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
            print('Incorrect Password. Please try again.')
            return redirect('/login')

        elif user:
            session['user'] = email
            session['user_id'] = user.user_id
            print('Successfully logged in!')
            return redirect('/parks')
#flash does not work but when i use print it prints in the terminal
#logic works 

    return render_template('login.html')


def is_logged_in():
    """Checking if there is a user logged in."""

    return 'user_id' in session



def logged_in_user(user_id):
    """Get information on the user that is logged in."""

    user = crud.get_user_by_id(user_id)
    
    # User.query.get(session['user_id'])
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
            flash('Cannot create an account with that email. Please try again.')
        else:
            crud.create_user(fname, lname, email, password)
            flash('Account created.') #not working 
            return redirect('/parks') 
    else:

        return render_template("registration.html")




@app.route('/logout', methods=['GET'])
def logout():
    """User logout."""

    if 'user' in session:
        del session['user']
        flash('Logged Out.') #check if this works 

        #or
    # session.pop('user', None)
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

@app.route('/user/<user_id>/bucketlists')
def all_users_bucketlists(user_id):
    """Show all the bucketlists for a particular user."""

    user = crud.get_user_by_id(user_id)

    return render_template('bucketlist_form.html', user=user)



@app.route('/bucketlists/<bucketlist_id>')
def get_specific_bucketlist(bucketlist_id):
    """Shows a user the details for a specific bucketlist."""

    bucketlist = crud.get_bucketlist_by_id(bucketlist_id)

    return render_template('bucketlist_details.html', bucketlist=bucketlist)



@app.route('/create-bucketlist', methods=['POST', 'GET'])
def new_bucketlist():
    """Creates a new bucketlist for a user."""

    user_id = session['user_id']
  

#get user that is in session
    user = crud.get_user_by_id(user_id)
    # session['user'] = user
    print('>>>>>>>>>>>>>', user)

#get park that is in hidden input 
    park = request.form.get('park_id')
    print('>>>>>>>>>>>>>', park)

#activities that they selected from request and the park from request
    activity = request.form.getlist('activities')
    print('>>>>>>>>>>>>', activity)



    does_bucketlist_exist = crud.get_bucketlist_by_park_and_user(park, user)
# run this to check if user has park id for bucketlist get_bucketlist_by_park(park_id, user_id)




    #checking if user already has a list with that park id 
    if does_bucketlist_exist:
        print('>>>>>>>>> here') #add to bucketlist by park id
    else:
        print('>>>>>>>>no bucketlist found ') #create new bucketlist 
# if not add these activities it a new bucketlist
    


    # new_bucketlist = crud.create_bucketlist(user_id)
    # new_bucketlist_item = crud.create_bucketlist_item(bucketlist_id, activity_id, order)

    # user_bucketlist = new_bucketlist, new_bucketlist_item, user_id

    return redirect('/user/<user_id>/bucketlist')


#STEP ONE 
#get user that is in session 
#get park that is in the hidden input 
#print those out 


#STEP TWO 
#activities that they selected from request and the park from request
#print out checked boxes 

#STEP THREE
#check to see if bucketlist exists for park/user and if it does add to existing bucketlist
# if not add these activities it a new bucketlist
 
 #when submits it will check if they have a bucketlist or not 


#STEP FOUR 
#last step is to send to database to update existing or create a new list 




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
