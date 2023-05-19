import json
from pydantic import BaseModel

# this takes the Rager class and turns it into json data
def BuildJson(Rager):
    json = {
        "reocrdingID": Rager.recordingID,
        "_id": Rager.playerName,
        "reasons": Rager.reasons,
        "reports": 1
    }
    return json
# this class is the model for the json that will be sent in from the front end
class Rager(BaseModel):
    recordingID: str
    playerName: str
    reasons: str
    reports: int | None


