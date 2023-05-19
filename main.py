from fastapi import FastAPI
from MongoDB import MongoDB
import JsonBuilder 

#creat the fastapi app
app = FastAPI(title="ChimichangApp")
#create an instance of the mongodb that we are connecting to
db = MongoDB("mongodb+srv://Developer:QjeAr4lwRkKYsiBW@ragerslist.kcn47su.mongodb.net/?retryWrites=true&w=majority","RagersUsernames")

@app.get("/getRagers")
async def getRagers(game: int):
    db.set_cluster("Ragers")
    ragers = db.get({"game": game})
    return ragers 

@app.get("/getpotentialRagers")
async def getPotentialRagers(game: int):
    db.set_cluster("PotentialRagers")
    ragers = db.get({"game": game})
    return ragers 

@app.post("/addRager")
async def addRager(rager_object: JsonBuilder.Rager):
    json = JsonBuilder.BuildRagerJson(rager_object)
    db.set_cluster("Ragers")
    db.post(json)
    db.set_cluster("PotentialRagers")
    db.delete(json["playerName"], json["game"])
    return {"message": "success"}

@app.post("/addReport")
async def addReport(rager_object: JsonBuilder.Rager):
    json = JsonBuilder.BuildRagerJson(rager_object)
    db.set_cluster("Ragers")
    db.update(json["playerName"], json["game"])
    return {"message": "success"}


@app.post("/submitRagerReview")
async def submitRager(Potentialrager_object: JsonBuilder.PotentialRager):
    json = JsonBuilder.BuildPotnetialRagerJson(Potentialrager_object)
    db.set_cluster("Ragers")
    if db.count({"playerName": json["playerName"], "game": json["game"]}) > 0:
        db.update(json["playerName"], json["game"])
        return {"message": "this player has already been submited. We will add a report to the player"}
    db.set_cluster("PotentialRagers")
    if db.count({"playerName": json["playerName"], "game": json["game"]}) > 0:
        db.update(json["playerName"], json["game"])
        return {"message": "this player has already been submited. We will add a report to the player"}
    db.post(json)
    return {"message": "success"}

@app.delete("/deletePotentialRager")
async def deletePotentialRager(rager_object: JsonBuilder.Rager):
    json = JsonBuilder.BuildRagerJson(rager_object)
    db.set_cluster("PotentialRagers")
    db.delete(json["playerName"], json["game"])
    return {"message": "success"}

@app.delete("/deleteRager")
async def deleteRager(rager_object: JsonBuilder.Rager):
    json = JsonBuilder.BuildRagerJson(rager_object)
    db.set_cluster("Ragers")
    db.delete(json["playerName"], json["game"])
    return{"message": "success"}