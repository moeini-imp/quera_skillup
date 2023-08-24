# Use an appropriate Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the FastAPI code and requirements file into the container
COPY . /app/
COPY requirements.txt /app/

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Install Redis server
RUN apt-get update && apt-get install -y redis-server

# Expose the ports for FastAPI and Redis
EXPOSE 8000 6379

# Command to run both FastAPI and Redis
CMD ["bash", "-c", "service redis-server start && uvicorn api:app --host 0.0.0.0 --port 8000"]
