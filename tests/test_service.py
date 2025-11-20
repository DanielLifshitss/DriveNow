
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.schemas.cars import  CarStatus
from database.services import car_service, rentals_service
from database.base import Base

def get_db():
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    TestingSession = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    return TestingSession()

def test_add_car():
    db = get_db()
    car = car_service.add_car(db, "Toyota", 2020)
    assert car.id is not None

def test_register_rental():
    db = get_db()
    car = car_service.add_car(db, "Honda", 2021)
    rental = rentals_service.register_rental(db, car.id, "Bob")
    assert rental.id is not None

def test_end_rental():
    db = get_db()
    car = car_service.add_car(db, "Mazda", 2019)
    rental = rentals_service.register_rental(db, car.id, "Alice")
    ended = rentals_service.end_rental(db, rental.id, CarStatus.AVAILABLE)
    assert ended.end_date is not None
