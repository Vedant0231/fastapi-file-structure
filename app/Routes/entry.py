from fastapi import APIRouter

entry = APIRouter()

@entry.get("/entry",tags=['entry'])
def user():
    return "demo"

@entry.post("/entrypost",tags=['entry'])
def user():
    return "demo"

@entry.put("/entryput",tags=['entry'])
def user():
    return "demo"

@entry.delete("/entrydelete",tags=['entry'])
def user():
    return "demo"        
