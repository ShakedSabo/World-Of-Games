FROM python:3.8-slim

RUN pip install flask
WORKDIR /app
COPY *.py /app/
EXPOSE 5000

CMD python3 MainScores.py