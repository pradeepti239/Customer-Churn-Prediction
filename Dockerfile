FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python customerchurnprediction.py

CMD [ "mlflow","ui" ]