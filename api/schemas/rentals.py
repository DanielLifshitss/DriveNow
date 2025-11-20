from pydantic import BaseModel,ConfigDict
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
    model_config = ConfigDict(from_attributes=True)
