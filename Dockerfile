# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Install Chrome and Chrome WebDriver
RUN apt-get update && apt-get install -y chromium-driver chromium
RUN ln -s /usr/lib/chromium-browser/chromedriver /usr/local/bin/chromedriver

# Run your script when the container launches
CMD ["python", "scrape.py"]
