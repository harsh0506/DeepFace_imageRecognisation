# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir tensorflow deepface asyncio numpy pillow flask 

# Expose port 5000 for the Flask app to run on
EXPOSE 5000

# Run the Flask app
CMD ["gunicorn" , "app:app" ,"--bind" , "0.0.0.0:5000"]

