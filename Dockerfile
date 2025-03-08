# Usa una imagen base con Python
FROM python:3.12

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que correrá Django
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

