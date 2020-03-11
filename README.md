# immo-tools

lancer les tests :

````shell script
pytest
````

avec le coverage :

````shell script
pytest --cov
````

lancer les tests avec nox : (attention, c'est super long !):

````shell scripts
nox -r
````

Permet de lancer les tests sur plusieurs versions de python et de manière isollée.
Nox crée son propre environnement virtuel et y install les dépendances.
L'option ``-r`` permet déviter de recréer tout l'environnement virtuel à chaque fois.

## build

une seule commande :

````shell script
poetry build
````

pypi-AgEIcHlwaS5vcmcCJGQ2NmU2MjFlLWE5MmYtNGJlNi04OWZhLTk0ZGU4MzcxNTdmMwACJXsicGVybWlzc2lvbnMiOiAidXNlciIsICJ2ZXJzaW9uIjogMX0AAAYgB5rHYLVVP6pgg3gpWEjvq31ONfYvXD4YzA4WsNdrI1E