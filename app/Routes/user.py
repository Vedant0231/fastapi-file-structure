from fastapi import APIRouter

user = APIRouter()

@user.get("/user",tags=['user'])
def user1():
    return "demo"

@user.post("/userpost",tags=['user'])
def user2():
    return "demo"

@user.put("/userput",tags=['user'])
def user3():
    return "demo"

@user.delete("/userdelete",tags=['user'])
def user4():
    return "demo"        
