# Use official Python runtime
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose port
EXPOSE 5000

# Environment variables for Flask
ENV FLASK_APP=hello4.py
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1

# Run Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
