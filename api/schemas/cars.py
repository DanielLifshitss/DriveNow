from typing import Optional
from pydantic import BaseModel,ConfigDict
from typing import List
from database.models.car import CarStatus

class CarBase(BaseModel):
    model: str
    year: int

class CarCreate(CarBase):
    pass

class CarUpdate(BaseModel):
    model: Optional[str] = None
    year: Optional[int] = None
    status: Optional[CarStatus] = None

class CarOut(CarBase):
    id: int
    status: CarStatus
    model_config = ConfigDict(from_attributes=True)

class CarsList(BaseModel):
    cars: List[CarOut]
