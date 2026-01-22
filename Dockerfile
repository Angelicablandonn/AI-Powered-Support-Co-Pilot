# Imagen base ligera y estable
FROM python:3.11-slim

# Evita que Python genere .pyc y buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Dependencias del sistema (necesarias para algunas libs de IA)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiamos requirements primero (mejora el cache)
COPY requirements.txt .

# Instalamos dependencias de Python
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código de la app
COPY . .

# Puerto expuesto (Render usa el que indiquemos)
EXPOSE 8000

# Comando de arranque
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
