
from datetime import datetime,timezone
from sqlalchemy.orm import Session
from database.models import Car, CarStatus, Rental
from app.middleware.metrics import recalc_metrics

def register_rental(db: Session, car_id: int, customer_name: str):
    car = db.query(Car).filter(Car.id == car_id).first()
    if not car: raise ValueError("Car not found")
    if car.status != CarStatus.AVAILABLE:
        raise ValueError("Car not available")

    rental = Rental(car_id=car_id, customer_name=customer_name)
    car.status = CarStatus.RENTED

    db.add(rental)
    db.commit()
    db.refresh(rental)
    recalc_metrics(db)
    return rental

def end_rental(db: Session, rental_id: int, new_status: CarStatus):
    rental = db.query(Rental).filter(Rental.id == rental_id).first()
    if not rental: raise ValueError("Rental not found")
    if rental.end_date: raise ValueError("Already ended")

    rental.end_date = datetime.now(timezone.utc)
    car = db.query(Car).filter(Car.id == rental.car_id).first()
    car.status = new_status

    db.commit()
    db.refresh(rental)
    recalc_metrics(db)
    return rental
