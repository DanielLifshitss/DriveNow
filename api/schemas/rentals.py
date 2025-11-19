from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from database.models.car import CarStatus

class RentalCreate(BaseModel):
    car_id: int
    customer_name: str

class RentalEndRequest(BaseModel):
    new_status: CarStatus = CarStatus.AVAILABLE

class RentalOut(BaseModel):
    id: int
    car_id: int
    customer_name: str
    start_date: datetime
    end_date: Optional[datetime]
    class Config:
        from_attributes = True