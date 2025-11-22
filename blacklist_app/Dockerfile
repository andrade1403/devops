FROM public.ecr.aws/docker/library/python:3.11-slim

# Crear y usar el directorio de trabajo
WORKDIR /app

# Copiar e instalar dependencias
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del codigo
COPY . .

# Asegurar que el directorio de trabajo esta en PYTHONPATH
ENV PYTHONPATH=/app

# Puerto que usa la app
EXPOSE 5000

# Comando por defecto: Gunicorn sirviendo la app
CMD ["python3", "application.py"]

# Configuracion de New Relic
ENV NEW_RELIC_APP_NAME="blacklist_app"
ENV NEW_RELIC_LOG=stdout
ENV NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
ENV NEW_RELIC_LICENSE_KEY=7bf89b628402942fc508a1808fc54b85FFFFNRAL
ENV NEW_RELIC_LOG_LEVEL=info

ENTRYPOINT [ "newrelic-admin", "run-program" ]
