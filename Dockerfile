FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    xvfb \
    x11vnc \
    x11-xkb-utils \
    xfonts-100dpi \
    xfonts-75dpi \
    xfonts-scalable \
    xfonts-cyrillic \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Set up virtual display
ENV DISPLAY=:99

# Create and set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script
COPY test_pyautogui.py .

# Create a script to run Xvfb and the Python script
RUN echo '#!/bin/bash\nXvfb :99 -screen 0 1024x768x16 &\nsleep 1\npython test_pyautogui.py' > /app/run.sh \
    && chmod +x /app/run.sh

# Command to run the script
CMD ["/app/run.sh"] 