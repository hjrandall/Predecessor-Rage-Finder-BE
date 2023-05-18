from fastapi import FastAPI, Request, openapi
from MongoDB import MongoDB
from ValidateJson import ValidateJson , ValidateRageSubmision

#creat the fastapi app
app = FastAPI(title="ChimichangApp")
#create an instance of the mongodb that we are connecting to
db = MongoDB("mongodb+srv://Developer:QjeAr4lwRkKYsiBW@ragerslist.kcn47su.mongodb.net/?retryWrites=true&w=majority","RagersUsernames")

@app.get("/getRagersList")
def getRagersList():
    db.set_cluster("Ragers")
    ragers = db.get({})
    return ragers 

@app.post("/submitRager")
def submitRager(json):
    db.set_cluster("PotentialRagers")
    validated = ValidateJson(json) 
    # if validated:
    #     db.post(json)
    #     return
    return 
