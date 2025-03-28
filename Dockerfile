FROM python:3.12.7-slim


WORKDIR /app


COPY requirements.txt /app/


RUN pip install --no-cache-dir -r requirements.txt


COPY . /app/


EXPOSE 5000


CMD ["flask", "run", "--host=0.0.0.0"]

