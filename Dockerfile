# in Docker, it is common to base a new image on a previously-created image
FROM arm64v8/python:3

# Set the working directory in the image
WORKDIR /welcome

# the ADD command is how you add files from your local machine into a Docker image
# Copy the current directory contents into the container at /app
ADD . .

# Run app.py when the container launches
CMD ["python", "welcome.py"]