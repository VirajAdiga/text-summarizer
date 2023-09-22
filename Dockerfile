# Use a Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application into the container at /app
COPY . /app/

# Trigger model download and caching during build
RUN python -c "from transformers import BartTokenizer, BartForConditionalGeneration; \
    BartTokenizer.from_pretrained('facebook/bart-large-cnn'); \
    BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')"

# Expose the port your application runs on
EXPOSE 5000

# Command to run your application
CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:5000", "main:app"]
