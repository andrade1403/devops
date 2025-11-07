# Dockerfile (para la API Flask)
FROM python:3.11-slim

# Evita buffering en logs
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copia requirements y los instala
# Ajusta la ruta si tu requirements.txt está en otra carpeta
COPY blacklist_app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copia el código de la app
COPY blacklist_app /app/blacklist_app

# Variables por defecto (puedes sobreescribir con docker-compose/env)
ENV FLASK_APP=blacklist_app
ENV FLASK_ENV=production

# Puerto que usa la app
EXPOSE 5000

# Comando por defecto: Gunicorn sirviendo la app
CMD ["python3", "blacklist_app/application.py"]