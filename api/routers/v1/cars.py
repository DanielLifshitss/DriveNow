from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import get_db
from api.schemas.cars import CarCreate, CarUpdate, CarsList, CarStatus, CarOut
from database.services.car_service import list_cars, add_car, update_car 

car_router = APIRouter(
    prefix="/v1/cars",
    tags=["cars"]
)

@car_router.get("/", response_model=CarsList)
async def list_cars(status_filter: CarStatus = None, db: Session = Depends(get_db)) -> CarsList:
    return CarsList(cars=list_cars(db, status_filter))

@car_router.post("/", response_model=CarOut)
async def create_car(car: CarCreate, db: Session = Depends(get_db)) -> CarOut:
    created = add_car(db, car.model, car.year)
    return created

@car_router.patch("/{car_id}", response_model=CarOut)
async def update_car(car_id: int, payload: CarUpdate, db: Session = Depends(get_db)) -> CarOut:
    try:
        return update_car(db, car_id, payload.model, payload.year, payload.status)
    except ValueError as e:
        raise HTTPException(404, str(e))