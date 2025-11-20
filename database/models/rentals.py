from datetime import datetime,timezone
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship  
from database.base import Base


class Rental(Base):
    
    __tablename__ = "rentals"
    
    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey("cars.id"), nullable=False)
    customer_name = Column(String, nullable=False)
    start_date = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
    end_date = Column(DateTime, nullable=True)
    car = relationship("Car", back_populates="rentals")
