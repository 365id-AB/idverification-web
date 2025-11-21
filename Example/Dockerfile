# ======================
# Builder stage
# ======================
FROM python:3.14-alpine AS builder

WORKDIR /app

# Install Node + npm (for 365id-web-sdk)
RUN apk add --no-cache nodejs npm

# Create Python virtualenv for app deps
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install latest 365id-web-sdk via npm
#RUN npm init -y \
#    && npm install @365id/id-verification:latest
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc \
    npm install "@365id/id-verification"
# ======================
# Final runtime stage
# ======================
FROM python:3.14-alpine

# Use venv from builder
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# Copy Python venv from builder
COPY --from=builder /opt/venv /opt/venv

# Copy npm artifacts (365id-web-sdk + its deps)
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package*.json ./

# Copy your app source
COPY . .

# Expose Flask port
EXPOSE 5001

CMD ["python", "sample_app.py"]
