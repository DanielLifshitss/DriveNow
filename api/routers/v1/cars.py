from fastapi import APIRouter

car_router = APIRouter(
    prefix="/v1/cars",
    tags=["cars"]
)

@car_router.get("/")
async def get_cars():
    return None

@car_router.post("/")
async def create_car():
    return None

@car_router.update("/{car_id}")
async def update_car():
    return None