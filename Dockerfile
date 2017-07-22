FROM python:3.4-alpine
ADD . /web
WORKDIR /web
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
