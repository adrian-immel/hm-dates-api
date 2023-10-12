# syntax=docker/dockerfile:1

FROM python:3.12-slim


# Add files
ADD ./ ./
# pip install
RUN pip install -r ./requirements.txt
#run python file
CMD python ./src/main.py docker-mode
