# Use an official lightweight Python image
FROM python:3.9-slim

# Force Python to print immediately (Unbuffered)
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# By default, run the ingestion script
CMD ["python", "src/ingestion/ingest_bicimad.py"]