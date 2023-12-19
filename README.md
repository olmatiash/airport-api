# Airport API Service

### Overview
Airport API Service is a comprehensive solution for managing airplanes, flights, ticket booking.
It allows for efficient flight planning and ticket.

### Features
- JWT authenticated
- Admin panel /admin/
- Documentation is located at /api/doc/swagger/
- Airport management including location coordinates and associated routes.
- Information regarding airplane types and seating arrangements.
- Routes, schedules, and real-time updates on flights.
- Simply process of booking tickets for passengers.
- Efficient handling of ticket orders from creation to completion.


### DB Sructure

<img width="954" alt="db_stucture" src="https://media.mate.academy/airport_diagram_ce181e403f.png">


## Getting Started

### Prerequisites
- Python 3.8+
- Django 3.2+
- Django Rest Framework

### Installation
**Clone the repository**:
   ```bash
   git clone https://github.com/olmatiash/airport-api/
   cd airport-api
  ```
Install required packages:
```
pip install -r requirements.txt
```

### Environment Setup
Create a .env file based on the .env.sample template.

```python
SECRET_KEY=DJANGO_SECRET_KEY
POSTGRES_HOST=POSTGRES_HOST
POSTGRES_DB=POSTGRES_DB
POSTGRES_USER=POSTGRES_USER
POSTGRES_PASSWORD=POSTGRES_PASSWORD
```


### Set up the database:
```python
python manage.py makemigrations
python manage.py migrate
```

Create a superuser:
```python
python manage.py createsuperuser
```

Run the development server:
```python
python manage.py runserver
```

### Getting access
```
- create user http://127.0.0.1:8000//api/user/register/
- get acces token http://127.0.0.1:8000//api/user/token/
```
### Run with Docker

Build and run the container:
```python
docker-compose up --build
```


Visit http://127.0.0.1:8000/ in your browser.


API Documentation
For detailed API documentation, visit:

- Swagger UI: http://127.0.0.1:8000/api/doc/swagger/
- Redoc: http://127.0.0.1:8000/api/doc/redoc/
