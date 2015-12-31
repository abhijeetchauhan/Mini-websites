import pymongo
from pymongo import MongoClient

# connect to the database
connection=MongoClient("localhost",27017)
db=connection.test

# handle to names collection
names=db.names
item=names.find_one()
print item['name']
