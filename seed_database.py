"""Script to seed database."""

from datetime import datetime
from random import choice 

"""Using Faker to generate information for 100 users."""
from faker import Faker #fake users 
fake = Faker()

import os 
import json
import crud, model, server

os.system('dropdb npsdb') #dropping my database
os.system('createdb npsdb') #creating my database 

model.connect_to_db(server.app)
model.db.create_all()


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

#Create parks
# def create_park(park_name, state_code, designation, imageURL):



# Create activities
# def create_activity(activity_name, park, bucketlistitem):



# Create bucketlist
# def create_bucketlist(user, park, bucketlistitem):



#Create bucketlist item
# def create_bucketlist_item(bucketlist_id, item_id, activity_id):




    #want to do this for every table, for the create function 

#loads park/activity data from json file 
# with open('') as f:

#have api file, make api request, get response, use response in seed file and create a 
#api.py for api calls 

#if des == national park else continue 