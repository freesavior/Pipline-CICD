# Utilisez une image de base appropriée
FROM python:3.9

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers de votre application dans le conteneur
COPY . /app

# Installez les dépendances nécessaires
RUN pip install -r requirements.txt

# Définissez la commande pour exécuter votre application
CMD [ "python", "main.py" ]

