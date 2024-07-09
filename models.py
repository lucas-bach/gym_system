from pydantic import BaseModel
from typing import Optional


class CreatePeople(BaseModel):
    name: str
    fk_addres: str
    fk_graduation: str
    birth_date: str
    email: str
    phone: str    
    cpf: str
    is_student: str
    is_teacher: str
    

class UpdatePeople(BaseModel):
    name: Optional[str] = None
    fk_addres: Optional[str] = None
    fk_graduation:Optional[str] = None
    birth_date:Optional[str] = None
    email: Optional[str] = None
    phone:Optional[str] = None   
    cpf: Optional[str] = None
    is_student:Optional[str] = None
    is_teacher:Optional[str] = None
   

class CreateAddres(BaseModel):
    state: str
    city: str
    street: str
    

class UpdateAddres(BaseModel):
    state: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    

class CreateGraduation(BaseModel):
    color: str
    degree: str


class UpdateGraduation(BaseModel):
    color: Optional [str] = None
    degree: Optional [str] = None
 