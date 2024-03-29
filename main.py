from fastapi import FastAPI
from MongoDB import MongoDB
import JsonBuilder 
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

#create an instance of the mongodb that we are connecting to
db = MongoDB("mongodb+srv://Developer:QjeAr4lwRkKYsiBW@ragerslist.kcn47su.mongodb.net/?retryWrites=true&w=majority","RagersUsernames")

#creat the fastapi app
app = FastAPI(
    docs_url=None, # Disable docs (Swagger UI)
    redoc_url=None, # Disable redoc
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/getRagers")
async def getRagers(game: JsonBuilder.getRagers):
    json =JsonBuilder.BuildgetJson(game)
    db.set_cluster("Ragers")
    ragers = db.get(json)
    return ragers 

@app.post("/getpotentialRagers")
async def getPotentialRagers(game: JsonBuilder.getRagers):
    json =JsonBuilder.BuildgetJson(game)
    db.set_cluster("PotentialRagers")
    ragers = db.get(json)
    return ragers 

@app.post("/getAppeals")
async def getAppeals(game: JsonBuilder.getRagers):
    json =JsonBuilder.BuildgetJson(game)
    db.set_cluster("Appeals")
    appeals = db.get(json)
    return appeals

@app.post("/addRager")
async def addRager(rager_object: JsonBuilder.Rager):
    json = JsonBuilder.BuildRagerJson(rager_object)
    db.set_cluster("Ragers")
    db.post(json)
    db.set_cluster("PotentialRagers")
    db.delete(json["playerName"], json["game"])
    return {"message": "The rager has been added"}

@app.post("/addReport")
async def addReport(rager_object: JsonBuilder.Rager):
    json = JsonBuilder.BuildRagerJson(rager_object)
    db.set_cluster("Ragers")
    db.update(json["playerName"], json["game"])
    return {"message": "A report has been added to the f{json.playerName}"}


@app.post("/submitRagerReview")
async def submitRager(Potentialrager_object: JsonBuilder.PotentialRager):
    json = JsonBuilder.BuildPotnetialRagerJson(Potentialrager_object)
    db.set_cluster("Ragers")
    if db.count({"playerName": json["playerName"], "game": json["game"]}) > 0:
        db.update(json["playerName"], json["game"])
        return {"message": "Your rager report has been submited"}
    db.set_cluster("PotentialRagers")
    if db.count({"playerName": json["playerName"], "game": json["game"]}) > 0:
        db.update(json["playerName"], json["game"])
        return {"message": "Your rager report has been submited"}
    db.post(json)
    return {"message": "Your rager report has been submited"}

@app.post("/submitAppeal")
async def submitAppeal(appeal_object: JsonBuilder.Appeal):
    json = JsonBuilder.BuildAppealJson(appeal_object)
    db.set_cluster("Appeals")
    if db.count({"playerName": json["playerName"], "game": json["game"]}) > 0:
        return {"message": "You have already submited an appeal and it is under further review"}
    db.post(json)
    return {"message": "Your appeal has been submited."}

@app.post("/deletePotentialRager")
async def deletePotentialRager(rager_object: JsonBuilder.Rager):
    json = JsonBuilder.BuildRagerJson(rager_object)
    db.set_cluster("PotentialRagers")
    db.delete(json["playerName"], json["game"])
    return {"message": "The potential rager has been deleted."}

@app.post("/deleteRager")
async def deleteRager(appeal_object: JsonBuilder.Appeal):
    json = JsonBuilder.BuildAppealJson(appeal_object)
    db.set_cluster("Ragers")
    db.delete(json["playerName"], json["game"])
    return{"message": "The rager has been deleted."}

@app.post("/deleteAppeal")
async def deleteRager(appeal_object: JsonBuilder.Appeal):
    json = JsonBuilder.BuildAppealJson(appeal_object)
    db.set_cluster("Appeals")
    db.delete(json["playerName"], json["game"])
    return{"message": "The appeal has been deleted."}