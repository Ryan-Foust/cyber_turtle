FROM python:3.8-slim
LABEL authors="ryan-foust"

# Set the working directory to /cyber_turtle
WORKDIR /cyber_turtle

# COPY . /cyber_turtle

COPY requirements.txt .
COPY ./src ./src

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD ["python", "src/trial_3_chat_gpt.py"]