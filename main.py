from fastapi import FastAPI
import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://Developer:QjeAr4lwRkKYsiBW@ragerslist.kcn47su.mongodb.net/?retryWrites=true&w=majority")
db = cluster["RagersUsernames"]
collection = db["Ragers"]
app = FastAPI()
@app.get("/")
def root():
    # post = {"hello": 0}
    # collection.insert_one(post)
    return {"helo": "Chrisssss"}