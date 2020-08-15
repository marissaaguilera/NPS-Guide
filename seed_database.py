"""Script to seed database."""
import os 
import json
from datetime import datetime
from random import choice 
import crud, model, server

"""Using Faker to generate information for 100 users."""
from faker import Faker #fake users 
fake = Faker()

os.system('dropdb npsdb') #dropping my database
os.system('createdb npsdb') #creating my database 

model.connect_to_db(server.app)
model.db.create_all()



#Tables: User, Park, Activity, State, ParkState, Bucketlist, BucketlistItem (7)

#Users - THIS WORKS
def seed_users():
    """Create 100 users."""

    # loads park/activity data from json file 
    with open('data/parkinfo.json') as f: 
    park_data = json.loads(f.read())

    for user in range(100):

        extension = ['@gmail.com', '@yahoo.com', '@hotmail.com']

        first = fake.first_name()
        last = fake.last_name()
        username = first[0] + last
        username = username.lower()
        email =  f'{first}.{last}{choice(extension)}'
        email = email.lower()
        password = fake.word()

        user = crud.create_user(username, first, last, email, password)
        # user = crud.create_user(fake.user_name(), fake.first_name(), fake.last_name(), fake.email(), fake.word())



#Parks - (This works)
def seed_parks():
    """Create parks."""

    # loads park/activity data from json file 
    with open('data/parkinfo.json') as f: 
    park_data = json.loads(f.read())

    data_value = park_data['data']
    data_dict = data_value[0] 

    all_parks = []


    for key, value in data_dict.items(): 
        parks_list = data_dict['parks']
        for park in parks_list: 
            #  values = states, fullName, url, parkcode, designation, name
            if park['designation'] == 'National Park':
                park_name, state_code, designation, siteURL = (park['fullName'],
                                                park['states'], 
                                                park['designation'], 
                                                park['url'])
    # def create_activity(activity_name, park, bucketlistitem):
                db_park = crud.create_park(park_name, 
                                        state_code, 
                                        designation, 
                                        siteURL)

                all_parks.append(db_park)
            else: 
                continue



# Activities - (Doesn't work)
def seed_activities():
    """Create activites."""

    # loads park/activity data from json file 
    with open('data/parkinfo.json') as f: 
    park_data = json.loads(f.read())

    data_value = park_data['data']
    data_dict = data_value[0] #data dictionary


    all_activities = []
    for key, value in data_dict.items(): 
        activity = data_dict['name'] 
        parks_list = data_dict['parks']

        for park in parks_list: 
            activity_name, park, bucketlistitem = (activity,
                                            park[''],)

            db_activity = crud.create_activity(activity_name, #do i need to add relationships to this 
                                        bucketlistitem) #how to do this for bucketlistitem 
            all_activities.append(db_activity)


#States - 
def seed_states():
    """Create states."""

    # loads park/activity data from json file 
    with open('data/parkinfo.json') as f: 
    park_data = json.loads(f.read())

    #state_code, park_id 
    data_value = park_data['data']
    data_dict = data_value[0] #data dictionary


    all_states = []
    for key, value in data_dict.items(): 
        parks_list = data_dict['parks']
        for park in parks_list: 
                state_code, park_id = (park['states']) #do i need to include park_id

                db_state = crud.create_state(state_code) #how to do this for bucketlistitem 
                all_states.append(db_state) 




#Parkstates - 
def seed_parkstates():
    """Create parkstate."""

    # loads park/activity data from json file 
    with open('data/parkinfo.json') as f: 
    park_data = json.loads(f.read())


# Bucketlist
def seed_bucketlist():
    """Create bucketlist."""

    # loads park/activity data from json file 
    with open('data/parkinfo.json') as f: 
    park_data = json.loads(f.read())

# def create_bucketlist(user, park, bucketlistitem):


def seed_bucketlistitem():
"""Create bucketlistitem."""

# loads park/activity data from json file 
with open('data/parkinfo.json') as f: 
park_data = json.loads(f.read())

# def create_bucketlist_item(bucketlist_id, item_id, activity_id):







seed_users()
seed_parks()
seed_activities()
seed_states()
seed_parkstates() #maybe dont need this 
seed_bucketlist() #maybe dont need this 
seed_bucketlistitem() #maybe dont need this 




#Questions:
#do you include your relationships in when you seed the database?

#NOTES:

#want to create a function for every table, for the create function 
#have api file, make api request, get response, use response in seed file and create a 
#api.py for api calls 

#if des == national park else continue 