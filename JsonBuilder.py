import json
from pydantic import BaseModel

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
def BuildAppealJson(appeal):
    json = {
        "playerName": appeal.playerName,
        "reasons": appeal.reasons,
        "game": appeal.game
    }
    return json
def BuildgetJson(get):
    json = {
        "game": get.game
    }
    return json

class PotentialRager(BaseModel):
    playerName: str
    recordingID: str
    reasons: str
    reports: int
    game: str

class Rager(BaseModel):
    playerName: str
    reports: int
    game: str
class Appeal(BaseModel):
    playerName: str
    reasons: str
    game: str

class getRagers(BaseModel):
    game: str


