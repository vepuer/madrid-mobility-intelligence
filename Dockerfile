# Dockerfile
FROM python:3.9-slim

# Prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV PATH="${PATH}:/root/.local/bin"

# Copy the rest of the application code
COPY . .

# 🛑 GENERIC COMMAND: Just start a shell and wait for instructions
CMD ["bash"]