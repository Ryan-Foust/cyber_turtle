FROM python:3.8-slim
LABEL authors="ryan-foust"

# Set the working directory to /cyber_turtle
WORKDIR /cyber_turtle

# COPY . /cyber_turtle

COPY requirements.txt .
COPY ./src ./src

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Set environment variables
ENV DISCORD_TOKEN your_bot_token_here

# Run app.py when the container launches
CMD ["python", "trial_3_chat_gpt.py"]