from fastapi import FastAPI
from MongoDB import MongoDB

#creat the fastapi app
app = FastAPI()
#create an instance of the mongodb that we are connecting to
db = MongoDB("mongodb+srv://Developer:QjeAr4lwRkKYsiBW@ragerslist.kcn47su.mongodb.net/?retryWrites=true&w=majority","RagersUsernames")

@app.get("/getRagersList")
def getRagersList():
    db.set_cluster("Ragers")
    ragers = db.get({})
    return ragers 