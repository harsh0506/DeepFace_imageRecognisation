## Part 1: Creating Flask API

### Overview:
This section involves creating a Python web application using Flask. The application will have functionalities for face registration and recognition using the DeepFace library. Here, we'll document the main components of the Flask application and how it works.

#### File Structure:
- `app.py`: Main Flask application script containing route definitions and logic.
- `Dockerfile`: Instructions for building a Docker image of the application.

#### Main Components:

1. **Flask Application (`app.py`):**
   - Import necessary libraries and modules (Flask, render_template, request, jsonify, etc.).
   - Define routes (`/`, `/compare1`, `/register`, `/compare`, `/recognize`) and their associated functions.
   - Implement functionality to handle image registration and recognition using the DeepFace library.
   - Use PIL (Python Imaging Library) to manipulate images.
   - Run the Flask app using `app.run(debug=True)`.

2. **Dockerfile:**
   - Use the official Python 3.8-slim-buster image as the base image.
   - Set the working directory to `/app`.
   - Copy the contents of the current directory to the container's `/app` directory.
   - Install required packages specified in the `RUN` command using `pip`.
   - Expose port 5000 for the Flask app to run.
   - Set the command to run the Flask app using Gunicorn.

## Part 2: Containerization using Docker

### Overview:
In this section, you'll learn about containerization using Docker. Docker allows you to package your application and its dependencies into a single container, ensuring consistent behavior across different environments.

#### File Structure:
- `Dockerfile`: The Dockerfile you provided.

#### Steps:

1. **Base Image:**
   Use the official Python 3.8-slim-buster image as the base image for your Docker container.

2. **Working Directory:**
   Set the working directory inside the container to `/app`.

3. **Copying Files:**
   Copy the contents of your current directory (including your Flask application files) into the `/app` directory of the container.

4. **Installing Dependencies:**
   Use the `RUN` command to install required packages using `pip`, including TensorFlow, DeepFace, asyncio, NumPy, Pillow, and Flask.

5. **Exposing Port:**
   Use the `EXPOSE` command to expose port 5000, which is the port your Flask app will run on.

6. **Running the App:**
   Use the `CMD` command to specify how to run your Flask app. In this case, you're using Gunicorn to run the app and bind it to `0.0.0.0:5000`.

## Part 3: Deployment on AWS ECS

### Overview:
This section outlines the deployment process of your containerized Flask application on AWS ECS (Elastic Container Service).

#### Steps:

1. **Amazon ECR Repository:**
   - Create an Amazon ECR repository using the `aws ecr create-repository` command.

2. **Building and Pushing Docker Image:**
   - Build the Docker image using `docker build -t face-recognise .`.
   - Push the Docker image to your Amazon ECR repository using `docker push`.

3. **Creating ECS Cluster:**
   - Create an ECS cluster using the `aws ecs create-cluster` command.

4. **Deploying the App on ECS:**
   - Tag the Docker image using `docker tag`.
   - Retrieve login credentials for Amazon ECR using `aws ecr get-login-password` and log in to your ECR repository using `docker login`.
   - Push the tagged Docker image to ECR using `docker push`.


Important Note:
As of now, the project is not deployed on AWS due to potential associated costs. Deploying applications on AWS, especially with resources like ECS, can result in charges for the usage of resources like compute instances, storage, data transfer, etc. Therefore, the provided project documentation is meant for educational and learning purposes.

Please be cautious and mindful of potential costs if you decide to proceed with deploying the application on AWS or any other cloud service. Always consider your budget and needs before deploying any application in a production environment.