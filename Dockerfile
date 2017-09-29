FROM ubuntu:latest

RUN apt-get update 
RUN apt-get upgrade -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential libmysqlclient-dev

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["python3"]
CMD ["main.py"]
