FROM python:3.10-slim

# Set environment variables for Python and Django
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /app/

# Collect static files (if needed) and run migrations on container startup
CMD python manage.py collectstatic --noinput && \
    python manage.py migrate && \
    gunicorn Bitcube.wsgi:application --bind 0.0.0.0:8000
