FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install Flask requests google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client transformers

CMD ["python", "app.py"]
