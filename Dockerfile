FROM python:3.9

WORKDIR /code
ADD /example_package /code
ADD requirements.txt /code

RUN pip install -r requirements.txt

EXPOSE 8080

# command to run on container start
CMD [ "python", "app.py" ]