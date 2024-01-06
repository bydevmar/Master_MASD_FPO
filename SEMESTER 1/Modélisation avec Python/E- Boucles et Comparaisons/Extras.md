
# Compléments à la Présentation sur les Boucles et les Comparaisons

## Chapitre 1 : Comparaisons

### Opérateurs Logiques
Les opérateurs logiques sont des outils puissants pour combiner des expressions booléennes. Voici quelques-uns des opérateurs couramment utilisés :

| Opérateur   | Description                    | Exemple                          | Résultat  |
|-------------|--------------------------------|----------------------------------|-----------|
| `and`       | ET logique                      | `True and False`                 | `False`   |
| `or`        | OU logique                       | `True or False`                  | `True`    |
| `not`       | NON logique                      | `not True`                      | `False`   |



Exemple :
```python
a = True
b = False
resultat = a and b  # False
```

### Opérateurs de Comparaison

Les opérateurs de comparaison permettent d'évaluer des conditions entre différentes valeurs. Voici quelques exemples :

| Opérateur   | Description                    | Exemple                  | Résultat  |
|-------------|--------------------------------|--------------------------|-----------|
| `==`        | Égal à                         | `5 == 5`                 | `True`    |
| `!=`        | Différent de                    | `5 != 3`                 | `True`    |
| `<`         | Inférieur à                     | `10 < 15`                | `True`    |
| `>`         | Supérieur à                     | `20 > 18`                | `True`    |
| `<=`        | Inférieur ou égal à             | `8 <= 8`                 | `True`    |
| `>=`        | Supérieur ou égal à             | `25 >= 30`               | `False`   |


### Opérateur Ternaire
L'opérateur ternaire est une expression conditionnelle concise qui renvoie une valeur en fonction d'une condition.

Exemple :
```python
age = 20
statut = "Majeur" if age >= 18 else "Mineur"
```

### Correspondance (Match)
L'instruction `match` est utilisée pour effectuer des comparaisons complexes basées sur des modèles.

Exemple :
```python
command = 'Hello, World!'
match command:
    case 'Hello, World!':
        print('Hello to you too!')
    case 'Goodbye, World!':
        print('See you later')
    case other:
        print('No match found')
# Résultat : Hello to you too!
```

## Chapitre 2 : Boucles

### Else dans la Boucle For
L'instruction `else` dans une boucle for est exécutée lorsque la boucle se termine normalement (sans être interrompue par un `break`).

Exemple :
```python
for i in range(5):
    print(i)
else:
    print("Boucle terminée normalement")
```
Résultat
```
 0
 1
 2
 3
 4
 Boucle terminée normalement
```

### Else dans la Boucle While
L'instruction `else` dans une boucle while est exécutée lorsque la condition de la boucle devient fausse.

Exemple :
```python
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("La condition de la boucle while n'est plus vraie")
    
# Résultat
# 0
# 1
# 2
# 3
# 4
# La condition de la boucle while n'est plus vraie
```

### Itération sur une Liste, Tuple, Dictionnaire, Chaîne de Caractères

L'itération est le processus de parcours séquentiel des éléments d'une structure de données. Vous pouvez itérer sur différentes structures de données telles que les listes, les tuples, les dictionnaires et les chaînes de caractères en utilisant des boucles.

#### Itération sur une Liste

**Définition :** L'itération sur une liste consiste à parcourir séquentiellement chaque élément de la liste.

**Exemple :**
```python
ma_liste = [1, 2, 3, 4, 5]
for element in ma_liste:
    print(element)
```

**Résultat :**
```
1
2
3
4
5
```

#### Itération sur un Tuple

**Définition :** L'itération sur un tuple implique le parcours de chaque élément du tuple séquentiellement.

**Exemple :**
```python
mon_tuple = ('a', 'b', 'c')
for element in mon_tuple:
    print(element)
```

**Résultat :**
```
a
b
c
```

#### Itération sur un Dictionnaire

**Définition :** L'itération sur un dictionnaire permet de parcourir les clés, les valeurs ou les paires clé-valeur du dictionnaire.

**Exemple :**
```python
mon_dictionnaire = {'nom': 'John', 'age': 25, 'ville': 'Paris'}
for cle, valeur in mon_dictionnaire.items():
    print(f"{cle}: {valeur}")
```

**Résultat :**
```
nom: John
age: 25
ville: Paris
```

#### Itération sur une Chaîne de Caractères

**Définition :** L'itération sur une chaîne de caractères signifie parcourir chaque caractère de la chaîne.

**Exemple :**
```python
ma_chaine = "Bonjour"
for caractere in ma_chaine:
    print(caractere)
```

**Résultat :**
```
B
o
n
j
o
u
r
```

### Boucles Imbriquées
Les boucles imbriquées sont des boucles situées à l'intérieur d'autres boucles. Cela permet de parcourir des structures de données multidimensionnelles.

Exemple :
```python
for i in range(3):
    for j in range(3):
        print(i, j)
```
Résultat : 
```
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
```
N'oubliez pas de consulter la dernière présentation sur les boucles et comparaisons pour une compréhension plus approfondie de ces concepts.