# Use the latest version of Python as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
# This should include Django and other dependencies
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project code to the working directory in the container
COPY . .

# Expose the port that Django will run on (default is 8000)
EXPOSE 8000

# Command to run migrations and start the Django development server
CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
