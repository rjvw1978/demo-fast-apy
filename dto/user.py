from pydantic import BaseModel

class UserRequest(BaseModel):
    first_name: str
    last_name: str   
    email: str
    password: str
    role: str

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str   
    email: str
    role: str

    class Config:
        orm_mode = True