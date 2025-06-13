from fastapi import FastAPI
import models.user
from database import engine
import routers.users
import routers.auth

app = FastAPI()

models.user.Base.metadata.create_all(bind=engine)   

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(routers.users.router)
app.include_router(routers.auth.router)


