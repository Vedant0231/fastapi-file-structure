from fastapi import APIRouter

competition = APIRouter()

@competition.get("/competition",tags=['competition'])
def user():
    return "demo"

@competition.post("/competitionpost",tags=['competition'])
def user():
    return "demo"

@competition.put("/competitionput",tags=['competition'])
def user():
    return "demo"

@competition.delete("/competitiondelete",tags=['competition'])
def user():
    return "demo"        
