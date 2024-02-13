# MANIPULATION DES FICHIERS AVEC PYTHON

Bienvenue dans ce cours sur la manipulation des fichiers avec Python. Dans ce cours, nous explorerons les différentes façons de travailler avec des fichiers en utilisant le langage de programmation Python.

## Qu'est-ce qu'un Fichier ?

Avant de plonger dans la manipulation des fichiers en Python, comprenons d'abord ce qu'est un fichier. Un fichier est un ensemble continu d'octets utilisé pour stocker des données. Ces données peuvent prendre la forme d'un simple fichier texte ou d'un programme exécutable plus complexe. Les fichiers sont organisés en trois parties principales : l'en-tête, les données réelles et la fin de fichier (EOF).



Dans ce cours, nous nous concentrerons principalement sur les fichiers texte avec les extensions .txt ou .csv.

## Chemins de Fichiers

Lorsque vous travaillez avec des fichiers en Python, vous avez besoin d'un chemin de fichier. Ce chemin est une chaîne de caractères qui représente l'emplacement du fichier sur le système de fichiers. Il se compose du chemin du dossier, du nom du fichier et de l'extension.

## Ouverture et Fermeture d'un Fichier en Python

La première étape pour travailler avec un fichier est de l'ouvrir. Cela se fait en utilisant la fonction intégrée `open()`. Assurez-vous toujours de fermer le fichier après son utilisation.

```python
# Exemple d'ouverture et de fermeture d'un fichier
file = open('cars.txt')
file.close()

# Utilisation de 'with' pour une fermeture automatique
with open('cars.txt') as reader:
    print(reader)
    # Traitement du fichier va ici
```

Il est également important de spécifier le mode d'ouverture du fichier (lecture, écriture, ajout, etc.).

## Lecture des Fichiers

Une fois le fichier ouvert, plusieurs méthodes sont disponibles pour la lecture, comme `read()`, `readline()`, et `readlines()`. Vous pouvez itérer sur chaque ligne du fichier en utilisant une boucle.

```python
with open('cars.txt', 'r') as reader:
    # Exemple de lecture du fichier entier
    print(reader.read())

    # Exemple de lecture de 5 caractères de chaque ligne
    print(reader.readline(5))

    # Exemple d'itération sur chaque ligne du fichier
    for line in reader:
        print(line, end='')
```

## Écriture des Fichiers

Pour écrire dans un fichier, utilisez les méthodes `write()` et `writelines()`. N'oubliez pas de spécifier le mode d'ouverture en écriture ('w').

```python
with open('output.txt', 'w') as text_writer:
    text_writer.write("Hello, this is a text file.")

lines_to_write = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('output_lines.txt', 'w') as lines_writer:
    lines_writer.writelines(lines_to_write)
```

## Extras

### Écriture de fichiers binaires

Ajoutons une section sur l'écriture et la lecture de fichiers binaires.

```python
with open('binary_file.bin', 'wb') as binary_writer:
    binary_writer.write(b'Master MASD')

with open('binary_file.bin', 'rb') as binary_reader:
    binary_data = binary_reader.read()
    print(binary_data)
```

### Lecture de fichiers JSON, XML et CSV

Ajoutons une section sur la lecture de fichiers JSON, XML et CSV.

```python
# Lecture de JSON
import json
with open('data.json', 'r') as json_file:
    data = json.load(json_file)
    print(data)

# Lecture de XML
import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()
for element in root:
    print(element.tag, element.text)

# Lecture de CSV
import csv
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)
```

Ce cours couvre les bases de la manipulation des fichiers en Python, y compris l'ouverture, la lecture, l'écriture et la fermeture. N'hésitez pas à explorer davantage et à contribuer à son amélioration !

## Contributeurs
- BOUHLALI Abdelfattah
- Gajja Nour Eddin
- Driss Abatour