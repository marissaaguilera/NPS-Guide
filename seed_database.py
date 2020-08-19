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
data_dict = data_value[0] 

all_parks = []

parks_list = data_dict['parks']
for park in parks_list: 
    
    if park['designation'] == 'National Park':
        park_name, designation, siteURL = (park['fullName'],
                                        park['designation'], 
                                        park['url'])

        db_park = crud.create_park(park_name, 
                                designation, 
                                siteURL)
        split = park['states'].split(',')
        crud.add_states_by_park(db_park, split)
        # crud.add_activities_by_park(db_park, db_activity)
        all_parks.append(db_park)
    else: 
        continue


# Create Activities
data_value = park_data['data']
data_dict = data_value[0] 

all_activities = []
for activity in data_value:
    activity = activity['name']

    db_activity = crud.create_activity(activity)
    all_activities.append(db_activity)



# Create Bucketlists
user_id = user.user_id
park_id = db_park.park_id
bucketlist = crud.create_bucketlist(user_id, park_id)



#Create BucketlistItem
bucketlist_id = bucketlist.bucketlist_id
activity_id = db_activity.activity_id

# date_string = input('Enter a date (i.e. 8 September, 2020)')
# order = datetime.strptime(date_string, '%d %B, %Y')
order = datetime.now()

bucektlistitem = crud.create_bucketlist_item(bucketlist_id, 
                                activity_id, 
                                order)


#ISSUES
#with bucketlist table
#with bucketlistitem table 



#query for park.states 
#see what i have on objects 
#run crud py and call functions 
#place in functions 
#routes and seeded 