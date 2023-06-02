from python:3.11-alpine

# Set working directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Create database directory
RUN mkdir -p /usr/src/app/database

# Copy app
COPY . .

# Run app
CMD [ "python", "main.py" ]