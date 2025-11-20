from fastapi import FastAPI
from api.routers.v1.cars import car_router
from api.routers.v1.rentals import rental_router
from app.middleware.metrics import metrics_endpoint
from logs.logger import setup_logging
from  database.session import engine
from database.models import car, rentals as models
from database.base import Base

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(car_router)
app.include_router(rental_router)
logger = setup_logging()

@app.get("/")
async def health_check():
    logger.info("Health check endpoint called")
    return {"status":"OK"}

@app.get("/metrics")
async def metrics():
    logger.info("Metrics endpoint called")
    return await metrics_endpoint()