
# Installations et lancement des challenges sur un serveur web 

## Étapes d'installation 
1. Configuration de Docker Compose : Créez un fichier docker-compose.yml pour chaque challenge. Chaque fichier décrirait le ou les containers nécessaires pour ce challenge spécifique.

2. Serveur Web : Créez un serveur web qui présente les 6 challenges. Chaque challenge aurait un bouton ou un lien pour le démarrer.

3. Code côté serveur : Lorsqu'un utilisateur clique sur le bouton pour commencer un challenge, votre serveur web devrait exécuter une commande pour démarrer le service Docker Compose correspondant. Vous pouvez faire cela en exécutant une commande shell à partir de votre code serveur. Par exemple, si vous utilisez Node.js, vous pouvez utiliser le module child_process pour exécuter des commandes shell.

4. Code côté client : Lorsqu'un utilisateur clique sur le bouton pour commencer un challenge, votre serveur web devrait également envoyer un message à votre code client pour démarrer le défi. Vous pouvez utiliser Socket.io pour envoyer des messages entre le serveur et le client.


## Création serveur web host
1. Installation de Node.js et npm : Node.js est un environnement d'exécution JavaScript qui nous permet de créer des serveurs web. npm (Node Package Manager) est utilisé pour gérer les dépendances de notre projet. Vous pouvez télécharger et installer Node.js et npm à partir de leur site web officiel : https://nodejs.org/

2. Création d'un nouveau projet Node.js : Créez un nouveau dossier pour votre projet, naviguez vers ce dossier dans votre terminal, puis initialisez un nouveau projet Node.js en exécutant npm init -y.

3. Installation d'Express : Express est un framework pour construire des serveurs web en Node.js. Vous pouvez l'installer en exécutant npm install express. 

4. Création d'un serveur web pour hoster les challenges. 
    - Créez serveur web with node et express
    - Création d'un dossier public pour stocker les fichiers statiques (css, js, images, etc.)
    - Création d'un fichier index.html dans le dossier public pour afficher la page d'accueil de notre site web

5. La prochaine étape est de mettre en place la fonctionnalité pour lancer un challenge spécifique. Cela impliquera probablement de démarrer un container Docker spécifique lorsque cette route est executer.
