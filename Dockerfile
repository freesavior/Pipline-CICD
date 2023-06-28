# Utilisation de l'image Python 3.9 comme base
FROM python:3.9

# Copie des fichiers de l'application dans le conteneur
COPY . /app

# Définition du répertoire de travail
WORKDIR /app

# Installation des dépendances
RUN pip install -r requirements.txt

# Commande pour exécuter l'application
CMD [ "python", "app.py" ]
