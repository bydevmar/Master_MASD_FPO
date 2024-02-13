# Python - Cours sur Listes, Tuples, et Dictionnaires

Bienvenue dans le référentiel du cours sur les listes en Python !

## Auteurs

- **BAISSA Touayba**
- **ERRAJRAJI Meryeme**

## Contributeurs

- **BOUHLALI  Abdelfattah - [ BYDEVMAR ]**

## 1. Listes

### 1.1 Définition

En Python, une liste est une structure de données qui peut contenir plusieurs éléments. Ces éléments peuvent être de différents types tels que des entiers, des chaînes de caractères, ou même d'autres listes. Les listes sont définies en utilisant des crochets `[]`.

**Exemple:**
```python
ma_liste = [1, 2, 3, "quatre", 5.0]
```

### 1.2 Accès aux éléments (Indeçage)

Les éléments d'une liste sont accessibles par leur position, appelée indice. L'indexing en Python commence à 0 pour le premier élément.

**Exemple:**
```python
premier_element = ma_liste[0]
```

### 1.3 Opérations sur les listes

#### 1.3.1 Concaténation
```python
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
resultat = liste1 + liste2
# résultat sera [1, 2, 3, 4, 5, 6]
```

#### 1.3.2 Répétition
```python
liste = [1, 2, 3]
resultat = liste * 3
# résultat sera [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

#### 1.3.3 Longueur d'une liste
```python
longueur = len(liste)
# longueur sera 3
```

#### 1.3.4 Ajout d'éléments
```python
liste.append(4)
# liste devient [1, 2, 3, 4]
```

#### 1.3.5 Insertion d'éléments
```python
liste.insert(1, 5)
# liste devient [1, 5, 2, 3, 4]
```

#### 1.3.6 Suppression d'éléments
```python
del liste[1]
# liste devient [1, 2, 3, 4]
```

#### 1.3.7 Inversion des éléments
```python
liste.reverse()
# liste devient [4, 3, 2, 1]
```

#### 1.3.8 Tri des éléments
```python
liste.sort()
# liste devient [1, 2, 3, 4]
```

#### 1.3.9 Accès négatif
```python
dernier_element = ma_liste[-1]
# dernier_element sera 5.0
```

### 1.4 Minimum, Maximum, Somme
```python
minimum = min(liste)
maximum = max(liste)
somme = sum(liste)
```

## 2. Tuples

### 2.1 Définition

Un tuple est similaire à une liste, mais il est immuable, c'est-à-dire qu'on ne peut pas le modifier après sa création. Les tuples sont définis avec des parenthèses `()`.

**Exemple:**
```python
mon_tuple = (1, 2, 3, "quatre", 5.0)
```

### 2.2 Accès aux éléments

L'accès aux éléments dans un tuple se fait de la même manière que dans une liste.

**Exemple:**
```python
premier_element = mon_tuple[0]
```

### 2.3 Propriétés des Tuples

- Les tuples prennent moins de mémoire que les listes.
- Les opérations sur les tuples sont généralement plus rapides que sur les listes.

## 3. Dictionnaires

### 3.1 Définition

Un dictionnaire est une structure de données associant des paires clé-valeur. Les dictionnaires sont définis avec des accolades `{}`.

**Exemple:**
```python
mon_dictionnaire = {'nom': 'John', 'age': 25, 'ville': 'Paris'}
```

### 3.2 Accès aux éléments

L'accès aux éléments d'un dictionnaire se fait en utilisant les clés.

**Exemple:**
```python
nom_personne = mon_dictionnaire['nom']
```

### 3.3 Opérations sur les dictionnaires

#### 3.3.1 Ajout ou Modification d'éléments
```python
mon_dictionnaire['profession'] = 'Ingénieur'
# mon_dictionnaire devient {'nom': 'John', 'age': 25, 'ville': 'Paris', 'profession': 'Ingénieur'}
```

#### 3.3.2 Suppression d'éléments
```python
del mon_dictionnaire['age']
# mon_dictionnaire devient {'nom': 'John', 'ville': 'Paris', 'profession': 'Ingénieur'}
```

#### 3.3.3 Vérification de l'existence d'une clé
```python
if 'age' in mon_dictionnaire:
    print("La clé 'age' existe.")
```

#### 3.3.4 Accès à toutes les clés et valeurs
```python
cles = mon_dictionnaire.keys()
valeurs = mon_dictionnaire.values()
```

## Conclusion

En résumé, les listes, les tuples et les dictionnaires sont des structures de données importantes en Python, chacune ayant ses propres caractéristiques et utilisations spécifiques. La compréhension de ces structures est cruciale pour le développement d'applications Python efficaces.

## Comment utiliser ce référentiel

1. Clônez ce référentiel sur votre machine locale.
2. Améliorez le cours ! Si vous avez des suggestions d'amélioration, n'hésitez pas à ouvrir une nouvelle demande d'extraction.

Profitez de votre apprentissage des listes et des tuples en Python !


### 🚀 Bon apprentissage ! 📚