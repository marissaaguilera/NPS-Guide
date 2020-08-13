"""Script to seed database."""

from datetime import datetime
import os 
import json
import crud, model, server

os.system('dropdb npsdb') #dropping my database
os.system('createdb npsdb') #creating my database 

model.connect_to_db(server.app)
model.db.create_all()


#loads park/activity data from json file 
# with open('') as f:



#python3 -i model.py

#psql npsdb (this gets me into my database)