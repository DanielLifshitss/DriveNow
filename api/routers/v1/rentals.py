#Containse all rentals API endpoints for version 1
from fastapi import APIRouter

rental_router = APIRouter(
    prefix="/v1/rentals",
    tags=["rentals"]
)

@rental_router.post("/")
async def create_rental():
    return None

@rental_router.post("/{rental_id}/end")
async def end_rental():
    return None