from pydantic import BaseModel
from typing import Optional


class CreatePeople(BaseModel):
    name: str
    addres: str
    graduation: str
    birth_date: str
    email: str
    phone: str
    sexo: Optional[str]
    state: str
    namestate: str
    city: str

class UpdatePeople(BaseModel):
    name: Optional[str] = None
    addres: Optional[str] = None
    graduation:Optional[str] = None
    birth_date:Optional[str] = None
    email: Optional[str] = None
    phone:Optional[str] = None
    sexo: Optional[str] = None
    state: Optional[str] = None
    namestate:Optional[str] = None
    city:Optional[str] = None
