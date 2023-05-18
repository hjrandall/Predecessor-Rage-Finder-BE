import json
def ValidateJson(JSon):
    try:
        json.loads(JSon)
    except ValueError as err:
        return False
    return True
def ValidateRageSubmision(JSon,db):
    if db.get({"_id": JSon._id}):
        return False
    elif JSon._id =="" or JSon.recordingID =="" or JSon.reasons ==[]:
        return False
    return True

