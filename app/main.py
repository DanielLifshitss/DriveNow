from fastapi import FastAPI
from api.routers.v1.cars import car_router
from api.routers.v1.rentals import rental_router

app = FastAPI()
app.include_router(car_router)
app.include_router(rental_router)

@app.get("/")
async def health_check():
    return {"status":"OK"}

@app.get("metrics")
async def get_metrics():
    return None