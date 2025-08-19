FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . /app

EXPOSE 8000
# --proxy-headers
CMD ["fastapi", "run", "main.py", "--port", "8000"]