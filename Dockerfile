# FROM python:3.12-slim

# WORKDIR /app
# COPY . /app

# RUN apt-get update && apt-get install -y --no-install-recommends \
#     awscli \
#     && pip install --no-cache-dir -r requirements.txt \
#     && rm -rf /var/lib/apt/lists/*

# CMD ["python3", "app.py"]

# Stage 1: build dependencies
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# Stage 2: final image
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . /app
CMD ["python3", "app.py"]
