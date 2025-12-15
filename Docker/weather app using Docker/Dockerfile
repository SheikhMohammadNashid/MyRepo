# 1. Base Image
FROM ubuntu:24.04

# 2. Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=app.py \
    FLASK_ENV=production

# 3. Install System Dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    git \
    ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 4. Create Virtual Environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# 5. Repo URL
ARG REPO_URL=https://github.com/SheikhMohammadNashid/weather-app.git

# 6. Clone Repository
RUN git clone $REPO_URL /app

# 7. Set Working Directory
WORKDIR /app

# 8. Install Python Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 9. Expose Port
EXPOSE 5001

# 10. Run Flask App
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
