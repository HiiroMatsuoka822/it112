FROM python:3.13-slim

# Set the working directory
WORKDIR /app
# Copy the requirements file into the container
COPY requirements.txt requirements.txt
# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application code into the container
COPY . .
# Expose the port the app runs on
EXPOSE 5000     
# Set the environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_APP_HOST=0.0.0.0
# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
# Use the following command to build the Docker image