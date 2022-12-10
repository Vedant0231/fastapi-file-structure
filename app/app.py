from fastapi import FastAPI
from app.Routes.competition import competition
from app.Routes.entry import entry
from app.Routes.user import user

app = FastAPI()

app.include_router(competition)
app.include_router(entry)
app.include_router(user)