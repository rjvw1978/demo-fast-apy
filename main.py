from fastapi import FastAPI
import models.user
from database import engine
import routers.auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Orígenes permitidos
    allow_credentials=True,           # Permitir cookies/autenticación
    allow_methods=["*"],              # Métodos HTTP permitidos
    allow_headers=["*"],              # Headers permitidos
)

models.user.Base.metadata.create_all(bind=engine)   

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(routers.auth.router)


