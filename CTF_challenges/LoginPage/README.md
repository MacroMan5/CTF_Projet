
# Challenge CTF : LoginPage

Ce challenge consiste à réussir à accéder à une page protégée par un système de mot de passe. Le défi est de trouver le mot de passe correct en comprenant le fonctionnement du code JavaScript. 

## Description du challenge

- L'utilisateur est présenté avec une page de connexion contenant un champ de mot de passe et un bouton "Submit".
- L'utilisateur doit saisir le mot de passe correct dans le champ de mot de passe pour obtenir le flag

## Instructions

1. Ouvrez le lien donné par le site du CTF dans un navigateur.
2. Analysez le code JavaScript dans le fichier `script.js` pour comprendre comment le mot de passe est généré.
3. Utilisez vos connaissances du code pour déterminer le mot de passe correct.
5. Saisissez le mot de passe dans le champ de mot de passe et cliquez sur "Submit".
6. Si le mot de passe est correct, vous serez redirigé vers la page où vous trouverez le flag.

 
## Indice 
- Observez attentivement le code JavaScript pour comprendre les étapes de génération du mot de passe.
- Utilisez la console du navigateur pour afficher l'heure actuelle et effectuer des tests pendant le défi.
- Pensez à la façon dont les valeurs existantes sont combinées avec l'heure pour obtenir le mot de passe.

## Flag

Le flag à trouver est : `01253{Flag_here}`

## Implémentation
1. Modifier le port et l'adresse que nous souhaitons utiliser pour accéder à la page web
2. Création de l'image docker `docker build -t loginpage .`
3. Lancement du container docker `docker run -d -p 8080:80 loginpage` (le port 8080 est celui que nous avons choisi)
4. Une fois le container lancé, la page web sera disponible 

- Utilisation de docker compose pour lancer le container : `docker-compose up -d`
- Exemple de fichier docker-compose.yml :

```
loginpage:
    build:
      context: .\myapp\CTF_challenges\LoginPage
      dockerfile: Dockerfile
    ports:
      - 80:80
    
```



Bonne chance et amusez-vous bien !
