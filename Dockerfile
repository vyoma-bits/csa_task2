# Step 1: Use an official Python runtime as a parent image
FROM python:3.9-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Step 4: Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of your application code into the container
COPY . /app/

# Step 6: Set environment variables (optional)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Step 7: Expose the port the app runs on (optional, based on your Django configuration)
EXPOSE 8000

# Step 8: Run the Django application (make sure to adjust the command based on your needs)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
