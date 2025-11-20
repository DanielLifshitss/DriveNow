# DriveNow Service
DriveNow - Technical Assignment – Vehicle Management System for a Car Rental Company
The system is built using a Layered / Clean Architecture approach:

### Presentation Layer (API)
```bash
FastAPI routers (api/routers)
Request/response models (schemas)
```
### Service Layer (Business Logic)
```bash
Car creation, updates, filtering
Rental lifecycle management
Validation unrelated to HTTP
Data Layer (Persistence)
SQLAlchemy models (database/models)
DB session management
Query + write operations
```
### Infrastructure Layer
```bash
Logging
Middleware
Docker
Environment configuration
```
## Project Stracture - Hexagonal / Ports-and-Adapters (light version):
```bash
drivenow/
│
├── app/
│   ├── __init__.py
│   ├── main.py                
│   ├── middleware/               
│       ├── __init__.py 
│       └── metric.py
├── api/
│   ├── __init__.py
│   ├── routers/version/               
│   │   ├── __init__.py
│   │   ├── cars.py           
│   │   └── rentals.py                    
│   ├── schemas/               
│       ├── __init__.py
│       ├── cars.py
│       └── rentals.py           
│
├── database/
│   ├── __init__.py
│   ├── connection.py
│   ├── base.py          
│   ├── models/                
│   │   ├── __init__.py
│   │   ├── car.py
│   │   └── rentals.py
│   ├── services/                  
│       ├── __init__.py
│       ├── car_service.py
│       └── rentals_service.py
├── logs/
│   ├── __init__.py
│   ├── logger.py    
│
├── tests/
│   ├── __init__.py
│   └── test_service.py 
├── requirements.txt           
├── Dockerfile     
├── docker-compose.yml                
└── README.md 
```

## Projcet Installation:
### Local Installations:
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
### Docker Installations:
```bash
docker build -t drivenow .
docker-compose up --build
```

## Endpoints:
### Cars:
```bash
GET /v1/cars/ -get all cars
POST /v1/cars/ -create new car
PATCH /v1/cares/{car_id} -update car
```
### Rentals:
```bash
POST /v1/rentals/ -create new rental
POST /v1/rentals/{rental_id}/end - end rental
```

### Defaults:
```bash
GET / -Health Check
POST /metrics
```

## Swagger (FastAPI Docs):
### Endpoints:
<img width="1243" height="593" alt="drivenow swagger" src="https://github.com/user-attachments/assets/faaca198-fb03-49a0-9223-d10d1b2ac365" />

### Schemas:
<img width="725" height="680" alt="drivenow schemas" src="https://github.com/user-attachments/assets/d528448c-1c4f-4527-8c00-71d6e565cbcc" />

## Testings:
### Pytest:
<img width="1287" height="191" alt="drivenow pytest resault" src="https://github.com/user-attachments/assets/69e72a77-d33c-4f19-9038-f9e5516bf9f3" />
<img width="433" height="128" alt="drivenow pytest cache" src="https://github.com/user-attachments/assets/e25ee4c0-488f-4bf4-8f17-6e135b8cd2e8" />

## Logs from logger:
<img width="688" height="164" alt="loggssssssssssssssssss" src="https://github.com/user-attachments/assets/e279a34b-7a6a-4288-b239-af0d45f8f414" />

## Endpoint Excecutions:

### Endpoint:
```bash
POST /v1/cars/ -create new car
```
### Swagger Screenshot:
<img width="1083" height="489" alt="drivenow add car swagger execute 1" src="https://github.com/user-attachments/assets/17233220-e856-446e-a8c7-017934079172" />
<img width="729" height="661" alt="drivenow add car swagger response" src="https://github.com/user-attachments/assets/4abee9a7-fec3-4e50-96b9-e38505e84318" />

### Console log Screenshot:
<img width="431" height="20" alt="drivenow add care log" src="https://github.com/user-attachments/assets/c87a353c-b712-4822-bc84-c3b518807572" />

### Database Screenshot:
<img width="468" height="224" alt="drivenow add care database show" src="https://github.com/user-attachments/assets/ca175078-f95c-4bb8-95c2-dcf7e54d86a6" />

```bash
PATCH /v1/cares/{car_id} -update car
```
### Swagger Screenshot:
<img width="1085" height="568" alt="drivenow update car swagger" src="https://github.com/user-attachments/assets/64939c5e-593a-448c-9d09-32df457e955e" />
<img width="730" height="671" alt="drivenow update car swagger response" src="https://github.com/user-attachments/assets/b5fbd5d3-5a7e-41cc-a6cf-4bb5d922de85" />

### Console log Screenshot:
<img width="440" height="21" alt="drivenow update car log" src="https://github.com/user-attachments/assets/61b51a28-6300-491e-a6e8-bb9d53a553e5" />

### Database Screenshot:
<img width="462" height="222" alt="drivenow update car db change" src="https://github.com/user-attachments/assets/0f82ad02-5db0-4cd8-a11c-9287a323692f" />

```bash
POST /v1/rentals/ -create new rental
```
### Swagger Screenshot:
<img width="1152" height="511" alt="drivenow rentcar enpoint swagger" src="https://github.com/user-attachments/assets/d46017a6-54e2-4d8a-8ea5-36cf20a6987b" />
<img width="721" height="675" alt="drivenow rentcar swagger resault" src="https://github.com/user-attachments/assets/4a5ed1a0-ab32-4661-8827-f51466059b88" />

### Console log Screenshot:
<img width="448" height="18" alt="drivenow rentcar endpoint log" src="https://github.com/user-attachments/assets/cac9dc3e-0903-4ce9-9553-6839cbb3463c" />

### Database Screenshot:
<img width="615" height="221" alt="drivenow rentcar db" src="https://github.com/user-attachments/assets/308480a3-af27-4b6f-b1b2-b522806834bc" />

```bash
POST /v1/rentals/ -create new rental
```
### Swagger Screenshot:
<img width="957" height="497" alt="drivenow end rental endpoint swagger" src="https://github.com/user-attachments/assets/2044634f-a88f-4053-8c9d-69e17edf45c4" />
<img width="725" height="667" alt="drivenow end rental endpoint response" src="https://github.com/user-attachments/assets/5980a831-d462-4d09-8a8c-1d7d3805e2ac" />

### Console log Screenshot:
<img width="485" height="18" alt="drivenow end rental log" src="https://github.com/user-attachments/assets/c009e4f2-0a43-4a05-ae92-3c619933e159" />

### Database Screenshot:
<img width="676" height="220" alt="drivenow endrental db" src="https://github.com/user-attachments/assets/733cac0c-92fc-4f39-84ad-a6a36976d6d9" />











