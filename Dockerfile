FROM python:3.10

## Main directory
WORKDIR /app

## Maps to random port when ran with -P
EXPOSE 8000

RUN apt-get update 

## Copy only requirements files (better for Docker caching)
COPY requirements.txt /app/

## Install Python Requirements
RUN pip install --upgrade pip && \
  pip install -r requirements.txt

## Copy all files into /app directory
COPY . .

## Run server by default
ENTRYPOINT ["python","manage.py"]

## These cmds be overided when addtional args are provided during runtime
CMD ["runserver", "0.0.0.0:8000"]