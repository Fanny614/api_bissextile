# API Bissextile
Cette API permet de retourner si une année est bissextile ou non, 
ou d'avoir toutes les années bissextiles comprises entre deux dates 
et enregistre le tout dans une base de données.

## Installation
Pour fonctionner, l'API a besoin de [python 3.12.7](https://www.python.org/downloads/).

### Installation du projet 
Pour plus d'information sur [poetry](https://python-poetry.org/).
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Pour activer l'environnement virtuel avec poetry :
```bash
poetry shell
```

```bash
poetry install
```

## Base de données
Pour créer la base de données, il faut creer un fichier avec pour nom `db.sqlite3` 
puis faire les migrations nécessaires à l'aide de :
```bash
python manage.py makemigations
```
puis de :
```bash
python manage.py migrate
```

## Usage
Pour lancer le serveur :
```bash
python manage.py runserver
```

### Premier endpoint
Cet endpoint permet de retnrer une année en entrée et retourne si celle si est bissextile ou non.

Pour accéder au premier endpoint, utiliser l'adresse `bissextile/single/`
et donner en entrée un fichier JSON contenant l'année à tester. 

Par exemple :
```json
{"annee": 2024}
```

### Deuxième endpoint
Cet endpoint permet de rentrer un intervalle d'année et retourne toutes les années bissextiles comprises entre ces deux années.

Pour accéder au deuxième endpoint, utiliser l'adresse `bissextile/range/`
et donner en entrée un fichier JSON contenant l'intervalle d'année souhaité. 

Par exmple 
```json
{"annee_debut": 1995, "annee_fin": 2004}
```

### Troisième endpoint
Cet endpoint retourne l'historique de toutes les requêtes avec leurs résultats.

Pour accéder au troisième endpoint, utiliser l'adresse `bissextile/history/`