# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port for the Streamlit app (default is 8501)
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]
