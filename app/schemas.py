from pydantic import BaseModel, EmailStr
from datetime import datetime
from fastapi import Form
    
class UserCreate(BaseModel):
    username: EmailStr
    password: str

    @classmethod
    def as_form(cls, username: str = Form(...), password: str = Form(...)):
        return cls(username=username, password=password)

class Users(BaseModel):
    username: EmailStr
    password: str

class UserRegis(BaseModel):
    id: int
    username: EmailStr
    class Config:
        orm_mode = True

class Userlogin(BaseModel):
    username: EmailStr
    password: str

    @classmethod
    def as_form(cls, username: str = Form(...), password: str = Form(...)):
        return cls(username=username, password=password)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: str

class operation(BaseModel):
    place: str
    days: int
    option: str