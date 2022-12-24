FROM python:3.11.0

RUN apt update
RUN apt install python3 -y

WORKDIR /usr/app/src

COPY main.py ./
COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python3", "./main.py"]
