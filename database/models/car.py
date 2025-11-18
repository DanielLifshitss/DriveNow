from datetime import datetime
from enum import Enum
from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship
from base import Base

class CarStatus(Enum):
    AVAILABLE = "available"
    RENTED = "rented"
    MAINTENANCE = "maintenance"
    

class Car(Base):
    
    __tablename__ = "cars"
    
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    status = Column(Enum(CarStatus), nullable=False, default=CarStatus.AVAILABLE)
    rentals = relationship("Rental", back_populates="car")
    
