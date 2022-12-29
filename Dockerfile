FROM python:3.9


COPY . /app
WORKDIR /app
RUN chmod 777 /app

RUN pip3 install --no-cache-dir -r requirements.txt


CMD ["python3","-u","muxbot.py"]
