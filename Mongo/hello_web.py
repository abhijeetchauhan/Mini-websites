import bottle
import pymongo

# this is handler to default path to the web server

@bottle.route('/')
def index():
  # connection to mongoDB
  connection=pymongo.MongoClient("localhost",27017)
  # attach the test database
  db=connection.test
  # get handle for names collection
  name=db.names
  # find a single document
  item=name.find_one()
  return "<b>Hello %s</b>"%item['name']

bottle.run(host='localhost',port=8080)