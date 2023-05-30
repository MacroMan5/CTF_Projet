# Challenge CTF : "Automatisation is key"

Bienvenue dans le challenge CTF "Automatisation is key". Dans ce défi, votre tâche est de décoder un message qui a été encodé.


## Description du challenge

- On vous donnera un fichier nommé `cipher.txt` qui contient un message.


## Instructions

1. Téléchargez le fichier `cipher.txt` qui contient le message.
2. Découvrez combien de fois le message a été encodé.
3. Décodez le message pour obtenir le flag.
4. Soumettez le flag pour terminer le défi.
5. La réponse vous aidera pour le prochain défi.

## Conseils

- La bibliothèque base64 en Python peut être utile pour déchiffrer le message.
- Une boucle peut être nécessaire pour déchiffrer le message complètement.
- Faites attention aux erreurs de décodage qui peuvent se produire si vous essayez de déchiffrer trop de fois.


## Indice 

- Le fichier decoder.py est un exemple de script qui peut vous aider à résoudre le défi.
- Le but est de décoder le message en base64 mais on se rend compte que même en le décodant c'est encore du Base64
- Le but du CTF est de créer un script pour faire un boucle pour décoder le message N fois. 

## Flag

Le flag à trouver est de format : `01253{Flag_ici}`

## Implémentation 
Fichier statique, éxecuter le script pour généré le fichier à remettre au utilisateur. 
Sinon avec docker : 
1. Création image docker - `docker build -t xorwith64 .`
2. Lancement du container - `docker run -it xorwith64`
(Utilisation d'un docker compose est aussi envisageable pour lancer le container)
3. Le container se lance et le fichier `cipher.txt` est présent dans le container 
4. Utilisation de la commande docker cp pour copier le fichier `cipher.txt` sur la machine hôte - `docker cp <containerId>:/cipher.txt /host/path/target`
5. Mettre un lien téléchargeable vers le fichier `cipher.txt` sur le site du CTF pour que les participants puissent le télécharger
6. Les participants doivent télécharger le fichier `cipher.txt` et le décoder pour obtenir le flag

- Exemple fichier avec implémentation avec un docker-compose.yml :
```
  automatisationiskey:
    build: .\CTF_challenges\ChiffrementRépété
    volumes:
      - data-volume:/app
```
## Acces au fichier `cipher.txt` sur le container
Les fichiers qui se trouvent dans le volume Docker partagé (data-volume dans notre exemple) seront disponibles pour tous les services qui y sont connectés.
Il faut configuer le serveur web en conséquence pour que les participants puissent télécharger le fichier `cipher.txt` sur le site du CTF. 


Bonne chance et amusez-vous bien !
