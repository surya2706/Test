#This is a Container for Cisco-Test

# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory to /app
WORKDIR /app/main

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Define environment variable
ENV FLASK_APP main.py

EXPOSE 5000
# Run main.py when the container launches
ENTRYPOINT ["python"]
CMD ["main.py"]