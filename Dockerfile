# # Stage 1: build dependencies
# FROM python:3.12-slim AS builder
# WORKDIR /app
# COPY . /app
# RUN apt-get update && apt-get install -y --no-install-recommends gcc g++ make \
#     && pip install --no-cache-dir -r requirements.txt

# # Stage 2: final image
# FROM python:3.12-slim
# WORKDIR /app
# COPY --from=builder /usr/local /usr/local
# COPY . /app
# CMD ["python3", "app.py"]


# Stage 1: Build dependencies
FROM python:3.12-slim AS builder

# Set working directory
WORKDIR /app

# Copy only requirements first
COPY requirements.txt .

# Install build tools and Python dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc g++ make \
    && pip install --prefix=/install --no-cache-dir -r requirements.txt \
    && apt-get remove -y gcc g++ make \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Stage 2: Final image
FROM python:3.12-slim

WORKDIR /app

# Copy installed Python packages from builder
COPY --from=builder /install /usr/local

# Copy application code
COPY . /app

# Default command
CMD ["python3", "app.py"]
