from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import get_db
from api.schemas.rentals import RentalCreate, RentalEndRequest, RentalOut
from database.services.rentals_service  import register_rental, end_rental as end_rental_service_func
from logs.logger import setup_logging

logger = setup_logging()

rental_router = APIRouter(
    prefix="/v1/rentals",
    tags=["rentals"]
)

@rental_router.post("/", response_model=RentalOut)
async def create_rental(r: RentalCreate, db: Session = Depends(get_db)) -> RentalOut:
    try:
        logger.info(f"Registering rental for car ID {r.car_id} to customer {r.customer_name}")
        return register_rental(db, r.car_id, r.customer_name)
    except ValueError as e:
        logger.error(f"Error registering rental for car ID {r.car_id}: {str(e)}")
        raise HTTPException(400, str(e))

@rental_router.post("/{rental_id}/end", response_model=RentalOut)
async def end_rental(rental_id: int, payload: RentalEndRequest, db: Session = Depends(get_db)) -> RentalOut:
    try:
        logger.info(f"Ending rental ID {rental_id} with new status: {payload.new_status}")
        return end_rental_service_func(db, rental_id, payload.new_status)
    except ValueError as e:
        logger.error(f"Error ending rental ID {rental_id}: {str(e)}")
        raise HTTPException(400, str(e))