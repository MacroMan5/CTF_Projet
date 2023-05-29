# Utiliser une image Ubuntu de base
FROM ubuntu:20.04

# Mettre à jour le système et installer les dépendances
RUN apt-get update && \
    apt-get install -y rsyslog python3 openssh-server

# Copier le script de génération de logs dans le conteneur
COPY generate_logs.py /generate_logs.py

# Configurer SSH
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/#\?PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#\?PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN echo "ClientAliveInterval 60" >> /etc/ssh/sshd_config

# Ajouter un utilisateur nommé 01253 avec des privilèges limités
#RUN useradd -m CTFuser && \
    #echo 'CTFuser:user' | chpasswd && \
    #mkdir /home/CTFuser/files && \
    #chown -R CTFuser:user /home/CTFuser/files && \
    #usermod -aG adm CTFuser && \
   
# Créer l'utilisateur CTFuser avec un répertoire personnel
RUN useradd -m CTFuser && \
    echo 'CTFuser:user' | chpasswd && \
    mkdir /home/CTFuser/files && \
    chown -R CTFuser:CTFuser /home/CTFuser/files

# Créer le groupe user s'il n'existe pas déjà
RUN getent group user || groupadd user

# Ajouter l'utilisateur CTFuser aux groupes user et adm
RUN usermod -aG user,adm CTFuser


    
# Exposer le port SSH
EXPOSE 22

# Modifier les autorisations des fichiers de journal et créer un utilisateur non privilégié pour exécuter rsyslogd
RUN touch /var/log/syslog && \
    chown syslog:adm /var/log/syslog && \
    chmod 640 /var/log/syslog

# Exécuter le script pour générer les logs et démarrer les services
CMD python3 /generate_logs.py && service ssh start && rsyslogd -n -u syslog

