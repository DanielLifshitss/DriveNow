from typing import Optional, List
from sqlalchemy.orm import Session
from database.models.car import Car, CarStatus
from app.middleware.metrics import recalc_metrics

def add_car(db: Session, model: str, year: int, status: CarStatus = CarStatus.AVAILABLE):
    car = Car(model=model, year=year, status=status)
    db.add(car)
    db.commit()
    db.refresh(car)
    recalc_metrics(db)
    return car

def update_car(db: Session, car_id: int, model: Optional[str], year: Optional[int], status: Optional[CarStatus]):
    car = db.query(Car).filter(Car.id == car_id).first()
    if not car: raise ValueError("Car not found")
    if model: car.model = model
    if year: car.year = year
    if status: car.status = status
    db.commit()
    db.refresh(car)
    recalc_metrics(db)
    return car

def list_cars(db: Session, status: Optional[CarStatus]) -> List[Car]:
    q = db.query(Car)
    if status: q = q.filter(Car.status == status)
    return q.all()
