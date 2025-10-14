# Stage 1: Build stage (uses a full image to install dependencies)
FROM python:3.10-slim AS builder

# Set working directory
WORKDIR /app

# Install build dependencies (e.g., for compiling some Python dependencies)
RUN apt-get update && apt-get install -y build-essential

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production stage (final minimal image)
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install only necessary runtime dependencies (if any are needed)
# We can skip this if we don't need any system dependencies in the final image

# Copy the installed Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10

# Copy app source code and templates (excluding unnecessary files)
COPY . .

# Expose the Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]




# # Use official Python image as base
# FROM python:3.10-slim

# # Set working directory
# WORKDIR /app

# # Copy requirements and install
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy all app source code and templates
# COPY . .

# # Expose the Flask port
# EXPOSE 5000

# # Run the Flask app
# CMD ["python", "app.py"]

