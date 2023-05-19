from fastapi import FastAPI
from MongoDB import MongoDB
import JsonBuilder 

#creat the fastapi app
app = FastAPI(title="ChimichangApp")
#create an instance of the mongodb that we are connecting to
db = MongoDB("mongodb+srv://Developer:QjeAr4lwRkKYsiBW@ragerslist.kcn47su.mongodb.net/?retryWrites=true&w=majority","RagersUsernames")

@app.get("/getRagers")
async def getRagersList():
    db.set_cluster("Ragers")
    ragers = db.get({})
    return ragers 

@app.get("/getpotentialRagers")
async def getRagersList():
    db.set_cluster("PotentialRagers")
    ragers = db.get({})
    return ragers 

@app.post("/addRager")
async def addRager(rager_object: JsonBuilder.Rager):
    json = JsonBuilder.BuildJson(rager_object)
    db.set_cluster("Ragers")
    db.post(json)
    db.set_cluster("PotentialRagers")
    db.delete(json["_id"])
    return 

@app.post("/submitRagerReview")
async def submitRager(rager_object: JsonBuilder.Rager):
    json = JsonBuilder.BuildJson(rager_object)
    db.set_cluster("Ragers")
    if db.count({"_id": json["_id"]}) > 0:
        db.update(json["_id"])
        return
    db.set_cluster("PotentialRagers")
    if db.count({"_id": json["_id"]}) > 0:
        db.update(json["_id"])
        return
    db.post(json)
    return
