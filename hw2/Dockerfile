FROM python:3.10

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y iputils-ping
RUN chmod +x main.py

CMD ["python3", "main.py", "ya.ru"]