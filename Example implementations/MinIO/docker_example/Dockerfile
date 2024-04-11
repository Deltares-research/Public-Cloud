# Use the official Python image
FROM python:3.8-slim

# Set working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY upload_file_to_minio.py .
COPY dataset.json .

# Install Boto3 library
RUN pip install boto3

# Run the Python script when the container starts
CMD ["python", "upload_file_to_minio.py"]
