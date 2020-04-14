#This is a Container for Cisco-Test

# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory to /app
WORKDIR /app/main

# Copy the current directory contents into the container at /app
COPY . /app

# Run main.py when the container launches
ENTRYPOINT ["python3", "main.py"]