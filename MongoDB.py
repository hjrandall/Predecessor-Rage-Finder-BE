# This class is for setting up the connection to mongodb
#pymongo is the library we use to connect to our mongodb
import pymongo
from pymongo import MongoClient
# bson.json_util is the library we use to make the cursor we recieve back from mongodb into a json object
from bson.json_util import dumps
class MongoDB:
    def __init__(self,dbUrl,db):
        # The dbUrl is the connection string you get from mongo in order to connect to your mongo instance
        # The db is the name of the database in your mongo instance you want to connect to
        # The cluster is which "table" you want to access in the database
        self.mongoUrl = MongoClient(dbUrl,)
        self.db = self.mongoUrl[db]
        self.cluster = ""

    # This is to set which "table" you will want to search or make changes to in the CRUD methods
    def set_cluster(self,cluster):
        self.cluster = self.db[cluster]
        return
    
    # The next four methods are the CRUD methods for the mongo db
    def post(self,json):
        self.cluster.insert_one(json)
        return 
    def get(self, json):
        cursor = self.cluster.find(json)
        list_cursor = list(cursor)
        json = dumps(list_cursor)
        return json
    def delete(self,playerName, game):
        self.cluster.delete_one({"playerName": playerName, "game": game})
        return
    def update(self,playerName, game):
        self.cluster.update_one({ "playerName": playerName, "game": game},{"$inc": {"reports": 1}})
        return 
    def count(self,json):
        documents = list(self.cluster.find(json))
        count = len(documents)
        return  count
