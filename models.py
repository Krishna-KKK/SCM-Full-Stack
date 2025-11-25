from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
 
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str = "user"
 
class UserInDB(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str
    role: str

class User(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str
    role: str
 
class Shipment(BaseModel):
    Container_Id: str
    Route_Details: str
    Good_Type: str
    Device_Name: str
    Date: datetime
    PO_Number: str
    Delivery_Number: str
    NOC_Number: str
    Batch_Id: str
    Serial_Number: str
    Description: Optional[str] = None

class UserUpdate(BaseModel):
    name: str
    email: EmailStr
    role: str
    
class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    role: str
    created_at: datetime
    updated_at: Optional[datetime]


    