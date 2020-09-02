"""Script to seed database."""

import os 
import json
from datetime import datetime
from random import choice 
import crud, model, server

"""Using Faker to generate information for 100 users."""
from faker import Faker #fake users 
fake = Faker()

#Tables: User, Park, Activity, ParkActivity, State, ParkState, Bucketlist, BucketlistItem (8)

os.system('dropdb npsdb')
os.system('createdb npsdb')
model.connect_to_db(server.app)
model.db.create_all()
#run python3 seed_database

with open('data/parkinfo.json') as f: 
    park_data = json.loads(f.read())




#Create users
all_users = []
for user in range(50):
    extension = ['@gmail.com', '@yahoo.com', '@hotmail.com']

    # username = first[0] + last
    # username = username.lower()
    first = fake.first_name()
    last = fake.last_name()
    email =  f'{first}.{last}{choice(extension)}'
    email = email.lower()
    password = fake.word()

    user = crud.create_user(first, last, email, password)
    all_users.append(user)




#Create States
states = [ "AK", "AL", "AR", "AS", "AZ", "CA", "CO", "CT",
            "DC", "DE", "FL", "GA", "GU", "HI", "IA", "ID",
            "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", 
            "MI","MN","MO", "MS", "MT","NC","ND","NE","NH",
            "NJ","NM","NV","NY","OH","OK","OR","PA","PR","RI",
            "SC","SD","TN","TX","UT","VA","VI","VT","WA", "WI", 
            "WV", "WY"]

for state in states:
    crud.create_state(state)





#Create Parks
data_value = park_data['data']
data_dict = data_value
#this only accesses 

all_parks = set()
all_activities = []

for value in data_value: 
    parks_list = value['parks']

    db_activity = crud.create_activity(value['name'])
    all_activities.append(db_activity)

    

    for park in parks_list: 
        
        if park['designation'] == 'National Park':
            park_name, designation, siteURL = (park['fullName'],
                                            park['designation'], 
                                            park['url'])

            db_park = crud.create_park(park_name, 
                                    designation, 
                                    siteURL)
            
            crud.create_park_activity(db_activity.activity_id, db_park.park_id)

            if db_park not in all_parks:
                split = park['states'].split(',')
                crud.add_states_by_park(db_park, split)
                all_parks.add(db_park)
        else: 
            continue
        #avoid having duplicate parks



# Create Bucketlists
user_id = user.user_id
park_id = db_park.park_id
bucketlist = crud.create_bucketlist(user_id, park_id)



#Create BucketlistItem
bucketlist_id = bucketlist.bucketlist_id
activity_id = db_activity.activity_id

date_string = input('Enter a date in MM/DD/YYYY format')
order = datetime.strptime(date_string, '%d %B, %Y')
# order = datetime.now()

bucektlistitem = crud.create_bucketlist_item(bucketlist_id, 
                                activity_id, 
                                order)

