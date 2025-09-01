FROM python:3.11-slim

WORKDIR /app

# Optimiza caché
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Prepara BD de ejemplo en build/run (opción: hazlo en entrypoint)
RUN python src/init_sqlite.py

# DO/Heroku-like PaaS inyectan $PORT; nuestro server lo lee en runtime
CMD ["python", "src/servidor_bd.py"]
