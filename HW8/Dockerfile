FROM python:3.13-slim
# Set the working directory
WORKDIR /app
# Copy the requirements file into the container
COPY requirements.txt requirements.txt
# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application code into the container
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0000:8000"]

