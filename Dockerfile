# Use official Python image
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy dependency files
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the full project into the container
COPY . .

# Set environment variable for Flask app
ENV FLASK_APP=app/main.py

# Expose Flask's default port
EXPOSE 5000

# Start the Flask app
CMD ["python", "-m", "app.main"]
