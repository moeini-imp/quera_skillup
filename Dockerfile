# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the FastAPI code and requirements file into the container
COPY . /app/
COPY requirements.txt /app/

# Install virtualenv and create a virtual environment
RUN pip install --no-cache-dir virtualenv && \
    virtualenv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Expose the port that your FastAPI application will run on
EXPOSE 8000

# Command to run your FastAPI application
CMD ["venv/bin/uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
