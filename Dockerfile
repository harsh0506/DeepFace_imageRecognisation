# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir tensorflow==2.10.0 keras==2.10.0 deepface==0.0.79 asyncio numpy pillow flask==2.1.1 opencv-python
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Expose port 5000 for the Flask app to run on
EXPOSE 5000

# Run the Flask app
CMD ["gunicorn" , "app:app" ,"--bind" , "0.0.0.0:5000"]

