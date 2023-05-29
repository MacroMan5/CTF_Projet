# Utiliser une image de base. Pour python, on utilise généralement python:3.x-alpine pour une image légère
FROM python:3.8-alpine

# Créer un répertoire de travail
WORKDIR /app

# Copier le fichier de script python dans l'image Docker
COPY xor_encoder.py .
COPY config.py .

# Exécuter le script python
CMD ["python", "-u", "xor_encoder.py"]
