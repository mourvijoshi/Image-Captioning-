# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and the application code to the container
COPY requirements.txt ./
COPY demo.py ./

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Gradio will run on
EXPOSE 7860

# Command to run the Gradio application
CMD ["python", "demo.py"]
