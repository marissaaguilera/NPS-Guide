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


# loads park/activity data from json file 
with open('data/parkinfo.json') as f: #can't have an underscore in the file name
    park_data = json.loads(f.read())




#Create parks
# def create_park(park_name, state_code, designation, siteURL):

data_value = park_data['data']
data_dict = data_value[0]

all_parks = []
for key, value in data_dict.items(): #getting values(keys = id, name, parks) from the data dictionary 
    parks_list = data_dict['parks']
    for info in parks_list: #info is a dict, values = states, fullName, url, parkcode, designation, name
        for k, v in info.items(): #accesses keys and values in dictionary 
            # print(k, v)
            park_name, state_code, designation, siteURL = (park['name'],
                                            park['states'], 
                                            park['designation'], 
                                            park['url'])

            db_park = crud.create_park(park_name, 
                                    state_code, 
                                    designation, 
                                    siteURL)

            all_parks.append(db_park)

    
# Create activities
# def create_activity(activity_name, park, bucketlistitem):



# Create bucketlist
# def create_bucketlist(user, park, bucketlistitem):



#Create bucketlist item
# def create_bucketlist_item(bucketlist_id, item_id, activity_id):



# Create 100 users
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

    print(user)





#NOTES:

#want to create a function for every table, for the create function 
#have api file, make api request, get response, use response in seed file and create a 
#api.py for api calls 

#if des == national park else continue 