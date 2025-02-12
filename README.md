# Bitcube RESTful API

This project implements a simple RESTful API for managing room bookings at Bitcube. It is built using Django and Django REST Framework, and it utilizes PostgreSQL for data storage. A browsable API front end is provided by Django REST Framework, which makes it easy to interact with the API through your web browser.

## Project Overview

- **Resource:** `room_booking`  
  The API manages room bookings with the following attributes:
  - **Room_Id:** Automatically generated UUID
  - **Booked_by:** Name of the person booking
  - **Booking_start:** The start date and time of the booking
  - **Duration_minutes:** Duration of the booking in minutes
  - **Booking_end:** Read-only computed value (booking_start + duration_minutes)

- **Features:**  
  - **CRUD operations:** Create, Retrieve, Update, and Delete room bookings  
  - **Validation:** Ensures that the duration is positive and other data integrity checks  
  - **Browsable API:** Access a friendly front end at `http://127.0.0.1:8000/` to view and interact with the API

## Setup and Running the Project

This project is containerized using Docker. Docker and docker-compose are used to run the application along with a PostgreSQL database.

### Building and Running with Docker

1. **Build and start the containers:**

    In the project root, run:
    ```bash
    docker-compose up --build
    ```

    This command:
    - Builds the Docker image for the web service.
    - Starts the PostgreSQL database container.
    - Runs Django migrations automatically.
    - Starts the Django development server on port 8000.

2. **Stopping the containers:**

    To stop the services, press `Ctrl+C` in the terminal or run:
    ```bash
    docker-compose down
    ```

## API Endpoints

When running, the API is accessible at:  
- **API Root:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
- **Room Booking Endpoint:** [http://127.0.0.1:8000/room_booking/](http://127.0.0.1:8000/room_booking/)

From the DRF browsable API, you can create new bookings, view existing ones, and click on individual bookings to update or delete them.

## Windows Command-Line Examples

You can also interact with the API using `curl` via Windows Command Prompt (CMD) or PowerShell.

### Using CMD

```batch
REM CREATE a new room booking
curl -X POST -H "Content-Type: application/json" -d "{\"booked_by\": \"John Doe\", \"booking_start\": \"2025-02-11T10:00:00Z\", \"duration_minutes\": 60}" http://127.0.0.1:8000/room_booking/

REM RETRIEVE a room booking (replace <room_id> with the actual ID)
curl -X GET http://127.0.0.1:8000/room_booking/<room_id>/

REM UPDATE a room booking (full update; replace <room_id> with the actual ID)
curl -X PUT -H "Content-Type: application/json" -d "{\"booked_by\": \"Jane Doe\", \"booking_start\": \"2025-02-11T11:00:00Z\", \"duration_minutes\": 90}" http://127.0.0.1:8000/room_booking/<room_id>/

REM DELETE a room booking (replace <room_id> with the actual ID)
curl -X DELETE http://127.0.0.1:8000/room_booking/<room_id>/
```

### Using CMD

```batch
# CREATE a new room booking
Invoke-RestMethod -Method POST -Uri "http://127.0.0.1:8000/room_booking/" `
    -ContentType "application/json" -Body '{"booked_by": "John Doe", "booking_start": "2025-02-11T10:00:00Z", "duration_minutes": 60}'

# RETRIEVE a room booking (replace <room_id> with the actual ID)
Invoke-RestMethod -Method GET -Uri "http://127.0.0.1:8000/room_booking/<room_id>/"

# UPDATE a room booking (replace <room_id> with the actual ID)
Invoke-RestMethod -Method PUT -Uri "http://127.0.0.1:8000/room_booking/<room_id>/" `
    -ContentType "application/json" -Body '{"booked_by": "Jane Doe", "booking_start": "2025-02-11T11:00:00Z", "duration_minutes": 90}'

# DELETE a room booking (replace <room_id> with the actual ID)
Invoke-RestMethod -Method DELETE -Uri "http://127.0.0.1:8000/room_booking/<room_id>/"
```

## API Testing

Unit tests for the API are located in tests.py and can be run with the following command inside the Docker container:

```batch
docker-compose exec web python manage.py test
```

his will execute the CRUD tests and verify that the API behaves as expected.
