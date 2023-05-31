# Challenge CTF : Login Page2

Ce challenge consiste à réussir à accéder à une page protégée par un système de mot de passe. Le défi est de trouver le mot de passe correct en comprenant le fonctionnement du code JavaScript. Le mot de passe est généré dynamiquement en fonction de l'heure actuelle et de valeurs existantes. Le mot de passe doit être saisi dans le champ de mot de passe pour valider l'accès à la page protégée.

## Description du challenge

- L'utilisateur est présenté avec une page de connexion contenant un champ de mot de passe et un bouton "Submit".
- Le mot de passe requis pour accéder à la page protégée est généré de manière dynamique en utilisant un algorithme basé sur l'heure actuelle   et des valeurs existantes encodé en base 64 correspodant à 10,20,30,40.
- L'heure actuelle est utilisée pour calculer une combinaison unique de l'heure et des valeurs existantes afin de générer le mot de passe.
- L'utilisateur doit saisir le mot de passe correct dans le champ de mot de passe pour valider son accès.
- Il sera important lors de l'implémentation que le server et le client soit synchronisé sur la même heure sinon les mots de passe ne seront jamais identique.

## Instructions

1. Ouvrez la page de connexion `index.html` dans un navigateur.
2. Remarquez que le mot de passe change en temps réel en fonction de l'heure actuelle (chaque minute).
3. Analysez le code JavaScript dans le fichier `script.js` pour comprendre comment le mot de passe est généré.
4. Utilisez vos connaissances du code et l'heure actuelle pour déterminer le mot de passe correct.
5. Saisissez le mot de passe dans le champ de mot de passe et cliquez sur "Submit".
6. Si le mot de passe est correct, vous serez redirigé vers la page où vous trouverez le flag.
7. Si le mot de passe est incorrect, vous serez redirigé vers la page `error.html`.

 

- Observez attentivement le code JavaScript pour comprendre les étapes de génération du mot de passe.
- Utilisez la console du navigateur pour afficher l'heure actuelle et effectuer des tests pendant le défi.
- Pensez à la façon dont les valeurs existantes sont combinées avec l'heure pour obtenir le mot de passe.

## Flag

Le flag à trouver est : `01253{Flag_here}`


## Implémentation
1. Modifier le port et l'adresse que nous souhaitons utiliser pour accéder à la page web
2. Création de l'image docker `docker build -t loginpage2 .`
3. Lancement du container docker `docker run -d -p 8080:80 loginpage2` (le port 8080 est celui que nous avons choisi)
4. Une fois le container lancé, la page web sera disponible 

- Utilisation de docker compose pour lancer le container : `docker-compose up -d`
- Exemple de fichier docker-compose.yml :

```
loginpage2:
    build:
      context: .\myapp\CTF_challenges\LoginPage2
      dockerfile: Dockerfile
    ports:
      - 8081:80
    volumes:
      - ./app.py:/app/app.py
      - ./index.html:/usr/share/nginx/html/index.html
      - ./error.html:/usr/share/nginx/html/error.html
      - ./LoginSuccessful.html:/usr/share/nginx/html/LoginSuccessful.html

```


Bonne chance et amusez-vous bien !
