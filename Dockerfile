
# Use an official Python runtime as a parent imag
FROM python:3.7
# Copy the current directory contents into the container at /app
COPY . /app
# Set the working directory to /app
WORKDIR /app
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
# Make port  available to the world outside this container
EXPOSE $PORT

# Define environment variable &  Define environment variable & 
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app

