# Challenge CTF : "Multiple encodings"

Bienvenue dans le challenge CTF "XOR64". Dans ce défi, votre tâche est de décoder un message qui a été encodé la clé XOR que vous avez trouvé vous aidera a décoder le message.

## Description du challenge

- On vous donnera un fichier nommé `cipher.txt` qui contient un message.
- Le message a été encodé avec plusieurs chiffrements.
- Vous devez décoder le message pour trouver le flag.

## Instructions
Il faut éxécuter xor_encoder.py pour généré le message chiffré `cipher.txt`.

1. Téléchargez le fichier cipher.txt qui contient le message encodé.
2. Découvrez les chiffrements utilisés pour chiffrer le message.
3. Continuez à décoder le message jusqu'à ce que vous obteniez le message chiffré avec XOR.
4. Utilisez la clé XOR trouvée précédemment pour déchiffrer le message XOR.
5. Déchiffrez le flag à partir du message décodé.
6. Soumettez le flag pour terminer le défi.

## Conseils

- La bibliothèque base64 et binascii en Python peuvent être utile pour déchiffrer le message.
- Pour le chiffrement XOR, souvenez-vous que chaque caractère du message est chiffré en utilisant la clé XOR obtenu à l'étape précédente.
- Une boucle peut être nécessaire pour déchiffrer le message complètement.
- Faites attention aux erreurs de décodage qui peuvent se produire si vous essayez de déchiffrer trop de fois.

## Réponse 

- Le fichier decoder.py est un exemple qui fonctionne pour dechiffrer le message.
 
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
  xorwith64:
    build: .\CTF_challenges\ChiffrementRépété
    volumes:
      - data-volume:/app
```
## Acces au fichier `cipherV2.txt` sur le container
Les fichiers qui se trouvent dans le volume Docker partagé (data-volume dans notre exemple) seront disponibles pour tous les services qui y sont connectés.
Il faut configuer le serveur web en conséquence pour que les participants puissent télécharger le fichier `cipherV2.txt` sur le site du CTF. 

Bonne chance et amusez-vous bien !
