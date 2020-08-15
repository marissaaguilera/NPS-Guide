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
with open('data/parkinfo.json') as f: 
    park_data = json.loads(f.read())


#Create parks

data_value = park_data['data']
data_dict = data_value[0]

all_parks = []


for key, value in data_dict.items(): 
    parks_list = data_dict['parks']
    for park in parks_list: 
        print('PARK:', park, '\n')
        # for k, v in park.items():#park is a dict, values = states, fullName, url, parkcode, designation, name
            # print('KEY:', k, 'VALUE:', v, '\n')
        if park['designation'] == 'National Park':
            park_name, state_code, designation, siteURL = (park['name'],
                                            park['states'], 
                                            park['designation'], 
                                            park['url'])

            db_park = crud.create_park(park_name, 
                                    state_code, 
                                    designation, 
                                    siteURL)

            all_parks.append(db_park)
        else: 
            continue

    
# Create activities
# def create_activity(activity_name, park, bucketlistitem):

# all_activities = []
# # data = park_data.get('data', 0)
# data_value = park_data['data']
# data_dict = data_value[0]

# for key, value in data_dict.items():
#     activity = 


# movies_in_db = []
# for movie in movie_data:
#     title, overview, poster_path = (movie['title'],
#                                     movie['overview'],
#                                     movie['poster_path'])
#     release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

#     db_movie = crud.create_movie(title,
#                                  overview,
#                                  release_date,
#                                  poster_path)
#     movies_in_db.append(db_movie)

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