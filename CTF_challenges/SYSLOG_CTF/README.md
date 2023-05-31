# Challenge CTF : "CheckTheLog"

Bienvenue dans le challenge CTF "CheckTheLog". Dans ce défi, votre mission est d'arrêter une attaque de brute force sur un serveur. Le serveur syslog a enregistré les journaux relatifs à cette attaque. Vous devrez vous connecter au serveur syslog, analyser les journaux pour identifier l'attaquant et récupérer le flag caché.

## Description du challenge

- Vous devez vous connecter à un serveur syslog.
- Analysez les journaux pour trouver des indices sur l'attaque de brute force.
- Récupérez le flag caché pour compléter le défi.

## Instructions

1. Connectez-vous au serveur syslog avec l'adresse IP fournie. Utilisez l'identifiant "CTFuser" et le mot de passe "user".
2. Une fois connecté, cherchez les journaux relatifs à l'attaque brute force.
3. Analysez les journaux pour identifier l'attaquant.
4. Récupérez le flag caché.

## Conseils

- Soyez attentif aux détails dans les journaux. Ils peuvent vous donner des indices sur l'attaquant et sa méthode.
- N'oubliez pas que le flag peut ne pas être dans la base que vous pensez.

## Flag

Le flag à trouver est de format : `01253{Flag_ici}`

## Solutions 
- Trouver le fichier ou on retrouve les logs : /var/log/auth.log
- Trouver les logs simulant des auth SSH failed password regarder s'il y des incohérences
- Trouver une le flag encrypté en Base64 dans les logs

## Implémentation
1. Création image docker - `docker build -t syslogSrv .`
2. Lancement du container - `docker run -it syslogSrv`
3. Le container se lance et le serveur syslog est lancé
4. Utilisateur peut se connecter au serveur syslog avec l'identifiant "CTFuser" et le mot de passe "user" en SSH 

- Exemple fichier avec implémentation avec un docker-compose.yml :
```
 checkthelog:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - 2222:22
    volumes:
      - ./logs:/var/log
      - ./CTFuser/files:/home/CTFuser/files
```

Bonne chance et amusez-vous bien !
