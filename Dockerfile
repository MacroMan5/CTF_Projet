# Utiliser une image de base. Pour Node.js, on utilise généralement node:14-alpine pour une image légère
FROM node:14-alpine

# Créer un répertoire de travail
WORKDIR /app

# Copier package.json et package-lock.json dans l'image Docker
COPY package*.json ./

# Installer les dépendances
RUN npm install

# Copier le reste des fichiers de l'application dans l'image Docker
COPY . .


# Exposer le port sur lequel votre application s'exécute
EXPOSE 3000

# Démarrer l'application
CMD ["npm", "start"]
