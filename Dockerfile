FROM python:3.9.19-slim-bullseye

WORKDIR /app

COPY . /app

#RUN apt update -y && apt install awscli -y
    
RUN pip install -r req.txt

EXPOSE 5000


RUN ["python", "main.py"]

CMD ["python", 'app.py']