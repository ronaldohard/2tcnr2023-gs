FROM python:3.6.1-alpine
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install Flask-RESTful
RUN pip install flask-cors
COPY app.py /app.py
CMD ["python","app.py"]