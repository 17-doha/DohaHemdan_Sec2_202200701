#this is the base image that i can start with that has the basic dependicies for the language that i am using
FROM python:3.9-alpine
#The directory that contains my work
WORKDIR /app
#command to copy the work to the docker file
COPY . .
#extra command as i am using flask framework
RUN pip install     flask
RUN pip install     flask_swagger_ui
#the local host that i am using
EXPOSE 5000
#command to run deciding the language e.g python and the main running file
CMD ["python", "app.py"]