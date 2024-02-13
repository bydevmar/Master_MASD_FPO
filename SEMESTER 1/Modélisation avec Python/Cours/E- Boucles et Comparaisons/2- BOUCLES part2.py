from __future__ import print_function
# Boucles et instructions de contrôle (continue, break et pass) en Python

# Boucle While en Python
# Jusqu'à ce qu'un critère spécifié soit vrai, un bloc d'instructions sera exécuté en continu dans une boucle while Python.
# Et la ligne dans le programme qui suit la boucle est exécutée lorsque la condition devient fausse.

# Syntaxe de While en Python
# while expression:
#     statement(s)
# En Python, toutes les instructions indentées par le même nombre d'espaces après une construction de programme
# sont considérées comme faisant partie d'un seul bloc de code. Python utilise l'indentation comme méthode de regroupement des instructions.

# imprime Bonjour Geek 3 fois
compteur = 0
while (compteur < 3):
    compteur = compteur + 1
    print("Bonjour Geek")
# Sortie :
# Bonjour Geek
# Bonjour Geek
# Bonjour Geek
# Voir ceci pour un exemple où une boucle while est utilisée pour les itérateurs.
# Comme mentionné dans l'article, il n'est pas recommandé d'utiliser une boucle while pour les itérateurs en python.

# Boucle For en Python
# En Python, il n'y a pas de boucle for de style C, c'est-à-dire for (i=0; i<n; i++).
# Il y a une boucle "for in" qui est similaire à la boucle for each dans d'autres langages.

# Syntaxe de For en Python
# for variable_itérateur in séquence:
#     instructions(s)
# Il peut être utilisé pour itérer sur des itérateurs et une plage.

# Itération sur une liste
print("Itération sur la liste")
liste = ["geeks", "pour", "geeks"]
for elem in liste:
    print(elem)

# Itération sur un tuple (immuable)
print("\nItération sur le tuple")
tup = ("geeks", "pour", "geeks")
for elem in tup:
    print(elem)

# Itération sur une chaîne de caractères
print("\nItération sur la chaîne de caractères")
chaine = "Geeks"
for elem in chaine:
    print(elem)

# Itération sur un dictionnaire
print("\nItération sur le dictionnaire")
dico = dict()
dico['xyz'] = 123
dico['abc'] = 345
for cle in dico:
    print("%s %d" % (cle, dico[cle]))
# Sortie :
# Itération sur la liste
# geeks
# pour
# geeks

# Itération sur le tuple
# geeks
# pour
# geeks

# Itération sur la chaîne de caractères
# G
# e
# e
# k
# s

# Itération sur le dictionnaire
# xyz  123
# abc  345
# Complexité temporelle : O(n), où n est le nombre d'éléments de l'itérable (liste, tuple, chaîne ou dictionnaire).
# Espace auxiliaire : O(1), car l'espace utilisé par le programme ne dépend pas de la taille de l'itérable.

# Nous pouvons utiliser une boucle for-in pour les itérateurs définis par l'utilisateur. Voir ceci pour un exemple.

# Boucles imbriquées en Python
# Le langage de programmation Python permet d'utiliser une boucle à l'intérieur d'une autre boucle.
# La section suivante montre quelques exemples pour illustrer le concept.

# Syntaxe de la boucle for imbriquée en Python
# La syntaxe d'une instruction de boucle for imbriquée en langage de programmation Python est la suivante :
# for variable_itérateur in séquence:
#     for variable_itérateur in séquence:
#         instructions(s)
#         instructions(s)
# Syntaxe de la boucle while imbriquée en Python
# La syntaxe d'une instruction de boucle while imbriquée en langage de programmation Python est la suivante :
# while expression:
#     while expression:
#         instructions(s)
#         instructions(s)
# Une note finale sur l'imbrication des boucles est que nous pouvons mettre n'importe quel type de boucle à l'intérieur de n'importe quel autre type de boucle.
# Par exemple, une boucle for peut être à l'intérieur d'une boucle while ou vice versa.


for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()
# Sortie :
# 1
# 2 2
# 3 3 3
# 4 4 4 4

# Instructions de contrôle de boucle en Python
# Les instructions de contrôle de boucle modifient l'exécution de leur séquence normale.
# Lorsque l'exécution quitte une portée, tous les objets automatiques créés dans cette portée sont détruits.
# Python prend en charge les instructions de contrôle suivantes.

# Python Continue
# Il renvoie le contrôle au début de la boucle.

# Imprime toutes les lettres sauf 'e' et 's'
for lettre in 'geeksforgeeks':
    if lettre == 'e' or lettre == 's':
        continue
    print('Lettre actuelle :', lettre)
# Sortie :
# Lettre actuelle : g
# Lettre actuelle : k
# Lettre actuelle : f
# Lettre actuelle : o
# Lettre actuelle : r
# Lettre actuelle : g
# Lettre actuelle : k

# Python Break
# Il sort du bloc de la boucle.

for lettre in 'geeksforgeeks':

    # sortir de la boucle dès qu'elle voit 'e'
    # ou 's'
    if lettre == 'e' or lettre == 's':
        break
print('Lettre actuelle :', lettre)
# Sortie :
# Lettre actuelle : e

# Python Pass
# Nous utilisons des instructions pass pour écrire des boucles vides. Pass est également utilisé pour des instructions de contrôle, des fonctions et des classes vides.

# Une boucle vide
for lettre in 'geeksforgeeks':
    pass
print('Dernière lettre :', lettre)
# Sortie :
# Dernière lettre : s

# Exercice : Comment imprimer une liste dans l'ordre inverse (du dernier au premier élément) en utilisant des boucles while et for-in.
