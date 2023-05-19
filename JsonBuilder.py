import json
from pydantic import BaseModel

# this takes the Rager class and turns it into json data
def BuildPotnetialRagerJson(PotentialRager):
    json = {
        "playerName": PotentialRager.playerName,
        "recordingID": PotentialRager.recordingID,
        "reasons": PotentialRager.reasons,
        "reports": PotentialRager.reports,
        "game": PotentialRager.game
    }
    return json

def BuildRagerJson(Rager):
    json = {
        "playerName": Rager.playerName,
        "reports": Rager.reports,
        "game": Rager.game
    }
    return json

class PotentialRager(BaseModel):
    playerName: str
    recordingID: str
    reasons: str
    reports: int | None
    game: int

class Rager(BaseModel):
    playerName: str
    reports: int
    game: int


