import time
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from prometheus_client import Gauge, Summary, generate_latest, CONTENT_TYPE_LATEST
from sqlalchemy.orm import Session
from database import models

ACTIVE_CARS = Gauge("active_cars_total", "Number of available cars")
ONGOING_RENTALS = Gauge("ongoing_rentals_total", "Rentals with no end date")
REQUEST_LATENCY = Summary("request_latency_seconds", "Request latency", ["method","path"])

def recalc_metrics(db: Session):
    ACTIVE_CARS.set(db.query(models.Car).filter(models.Car.status == models.CarStatus.AVAILABLE).count())
    ONGOING_RENTALS.set(db.query(models.Rental).filter(models.Rental.end_date.is_(None)).count())

class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.monotonic()
        response = await call_next(request)
        duration = time.monotonic() - start
        REQUEST_LATENCY.labels(request.method, request.url.path).observe(duration)
        return response

async def metrics_endpoint():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
