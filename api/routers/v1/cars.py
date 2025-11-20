from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import get_db
from api.schemas.cars import CarCreate, CarUpdate, CarsList, CarStatus, CarOut
from database.services.car_service import (list_cars as get_list_cars, add_car, update_car as car_update_service_func)
from logs.logger import setup_logging

logger = setup_logging()

car_router = APIRouter(
    prefix="/v1/cars",
    tags=["cars"]
)

@car_router.get("/", response_model=CarsList)
async def list_cars(status_filter: CarStatus = None, db: Session = Depends(get_db)) -> CarsList:
    logger.info(f"Listing cars with status filter")
    return CarsList(cars=get_list_cars(db, status_filter))

@car_router.post("/", response_model=CarOut)
async def create_car(car: CarCreate, db: Session = Depends(get_db)) -> CarOut:
    logger.info(f"Creating car: {car.model}, Year: {car.year}")
    created = add_car(db, car.model, car.year)
    return created

@car_router.patch("/{car_id}", response_model=CarOut)
async def update_car(car_id: int, payload: CarUpdate, db: Session = Depends(get_db)) -> CarOut:
    try:
        logger.info(f"Updating car ID {car_id} with data: {payload}")
        return car_update_service_func(db, car_id, payload.model, payload.year, payload.status)
    except ValueError as e:
        logger.error(f"Error updating car ID {car_id}: {str(e)}")
        raise HTTPException(404, str(e))