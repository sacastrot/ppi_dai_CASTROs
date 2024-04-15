FROM python:3.9

RUN mkdir /code

WORKDIR /codes

COPY requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]