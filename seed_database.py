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
#run seed only after this, my drop and create already happened 

with open('data/parkinfo.json') as f: 
    park_data = json.loads(f.read())




#Create users, 100 users
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





#Create Parks, 19 parks 
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

        all_parks.append(db_park)
    else: 
        continue





# Create Activities, 40 activities
data_value = park_data['data']
data_dict = data_value[0] #data dictionary

all_activities = []
for activity in data_value:
    activity = activity['name']

    db_activity = crud.create_activity(activity)
    all_activities.append(db_activity)





#Create States

state_code, park_id 
data_value = park_data['data']
data_dict = data_value[0]

all_states = [] 
parks_list = data_dict['parks']

for park in parks_list: 
        state_code = (park['states'])

        # state = crud.get_state_by_state_code(state_code)
        
        # if state_code in all_states:
        #     pass
        # else:
        all_states.append(state_code)
set(all_states)
state = crud.create_state(state_code)


        #checking if i get the state i want, duplicate states





# Create Bucketlists, empty until user creates 
user_id = user.user_id
park_id = db_park.park_id
bucketlist = crud.create_bucketlist(user_id, park_id)



#BucketlistItems
# def seed_bucketlistitem(bucketlist, activity):
# """Create bucketlistitem."""

date_string = input('Enter a date (i.e. 8 September, 2020)')
order = datetime.strptime(date_string, '%d %B, %Y')

# bucketlist_id, activity_id, order
bucektlistitem = crud.create_bucketlist_item(bucketlist_id, 
                                activity_id, 
                                order)


#NOTES/QUESTIONS

#can i just create a list of all 50 states and 
# seed the db that way then make the relationship later?

#do i need state table, bucketlist table 

#ISSUES
#with state table
#with bucketlistitem table 

