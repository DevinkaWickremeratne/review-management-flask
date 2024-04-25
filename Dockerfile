# Use the official Python image for Python 3.11 as a base image
FROM python:3.11-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt /app/

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . /app/

# Create a new user to run the application
RUN addgroup --gid 10014 choreo && \
    adduser  --disabled-password  --no-create-home --uid 10014 --ingroup choreo choreouser
USER 10014

# Expose port 5000 to the outside world
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
