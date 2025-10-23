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


FROM python:3.12-slim AS builder
WORKDIR /app

# Copy only requirements first
COPY requirements.txt . 

# Install build tools and Python deps
RUN apt-get update && apt-get install -y --no-install-recommends gcc g++ make \
    && pip install --no-cache-dir -r requirements.txt

# Then copy the rest of the app
COPY . /app
