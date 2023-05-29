# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install the Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code and HTML files to the container
COPY app.py .
COPY error.html .
COPY index.html .
COPY LoginSuccessful.html .

# Expose the port on which the Flask server will run
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]
