from __future__ import print_function
# Les boucles en Python - For, While et Boucles imbriquées
# Le langage de programmation Python propose deux types de boucles - la boucle For et la boucle While - pour gérer les besoins de bouclage.
# Python offre trois façons d'exécuter les boucles.

# Boucle While en Python
# Une boucle While est utilisée pour exécuter un bloc d'instructions de manière répétée jusqu'à ce qu'une condition donnée soit satisfaite.
# Lorsque la condition devient fausse, la ligne immédiatement après la boucle dans le programme est exécutée.

# Syntaxe de la boucle While :
# while expression:
#     instruction(s)

# Exemple de boucle While en Python :
# Le code suivant utilise une boucle 'while' pour imprimer "Hello Geek" trois fois en incrémentant une variable appelée 'count' de 1 à 3.

count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")

# Sortie :
# Hello Geek
# Hello Geek
# Hello Geek

# Utilisation de l'instruction else avec la boucle While en Python
# La clause else est uniquement exécutée lorsque votre condition 'while' devient fausse.
# Si vous sortez de la boucle ou si une exception est levée, elle ne sera pas exécutée.

# Syntaxe de la boucle While avec l'instruction else :
# while condition:
#     # exécuter ces instructions
# else:
#     # exécuter ces instructions

# Exemple de boucle While avec l'instruction else en Python :
# Le code imprime "Hello Geek" trois fois à l'aide d'une boucle 'while' et, après la boucle, il imprime "In Else Block"
# car il y a un bloc "else" associé à la boucle 'while'.

count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")
else:
    print("In Else Block")

# Sortie :
# Hello Geek
# Hello Geek
# Hello Geek
# In Else Block

# Boucle While infinie en Python
# Si nous voulons qu'un bloc de code s'exécute un nombre infini de fois, nous pouvons utiliser la boucle 'while' en Python.

# Le code utilise une boucle 'while' avec la condition (count == 0). Cette boucle ne s'exécutera que tant que count est égal à 0.
# Comme count est initialement défini à 0, la boucle s'exécutera indéfiniment car la condition est toujours vraie.

count = 0
while (count == 0):
    print("Hello Geek")

# Remarque : Il est déconseillé d'utiliser ce type de boucle car il s'agit d'une boucle infinie sans fin où la condition est toujours vraie,
# et vous devez arrêter le compilateur de force.

# Boucle For en Python
# Les boucles For sont utilisées pour la traversée séquentielle, par exemple : la traversée d'une liste, d'une chaîne de caractères, d'un tableau, etc.
# En Python, il y a la boucle "for in" qui est similaire à la boucle foreach dans d'autres langages.

# Syntaxe de la boucle For :
# for variable_iteratrice in séquence:
#     instructions(s)

# Exemple de boucle For en Python :
# Le code utilise une boucle 'for' Python qui itère sur les valeurs de 0 à 3 (non inclus), comme spécifié par la construction range(0, n).
# Il affichera les valeurs de 'i' à chaque itération de la boucle.

n = 4
for i in range(0, n):
    print(i)

# Sortie :
# 0
# 1
# 2
# 3

# Exemple avec itération de listes, tuples, chaînes de caractères et dictionnaires à l'aide de boucles For en Python :
# Nous pouvons utiliser une boucle 'for' pour itérer sur des listes, des tuples, des chaînes de caractères et des dictionnaires en Python.

# Le code présente différentes façons d'itérer sur diverses structures de données en Python.
# Il démontre l'itération sur des listes, des tuples, des chaînes de caractères, des dictionnaires et des ensembles, en affichant leurs éléments ou paires clé-valeur.

# La sortie affiche le contenu de chaque structure de données au fur et à mesure de son itération.

print("Itération sur la liste")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

print("\nItération sur le tuple")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

print("\nItération sur la chaîne de caractères")
s = "Geeks"
for i in s:
    print(i)

print("\nItération sur le dictionnaire")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s  %d" % (i, d[i]))

print("\nItération sur l'ensemble")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i)

# Sortie :
# Itération sur la liste
# geeks
# for
# geeks
#
# Itération sur le tuple
# geeks
# for
# geeks
#
# Itération sur la chaîne de caractères
# G
# e
# e
# k
# s
#
# Itération sur le dictionnaire
# xyz  123
# abc  345
#
# Itération sur l'ensemble
# 1
# 2
# 3
# 4
# 5
# 6

# Itération par l'index des séquences
# Nous pouvons également utiliser l'index des éléments dans la séquence pour itérer.
# L'idée principale est de calculer d'abord la longueur de la liste et d'itérer sur la séquence dans la plage de cette longueur.

# Exemple : Ce code utilise une boucle 'for' pour itérer sur une liste et imprimer chaque élément.
# Il itère à travers la liste en fonction de l'index de chaque élément, obtenu à l'aide de 'range(len(list))'.
# Le résultat est qu'il imprime chaque élément de la liste sur des lignes séparées.

list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])

# Sortie :
# geeks
# for
# geeks

# Utilisation de l'instruction else avec la boucle For en Python
# Nous pouvons également combiner l'instruction else avec la boucle for comme dans la boucle while.
# Cependant, comme il n'y a pas de condition dans la boucle for sur laquelle l'exécution se terminera, le bloc else sera exécuté immédiatement après l'exécution du bloc for.

# Dans ce code, la boucle 'for' itère sur une liste et imprime chaque élément, tout comme dans l'exemple précédent.
# Cependant, après la boucle, le bloc "else" est exécuté. Ainsi, dans ce cas, il imprime "Inside Else Block" une fois la boucle terminée.

list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])
else:
    print("Inside Else Block")

# Sortie :
# geeks
# for
# geeks
# Inside Else Block

# Boucles imbriquées
# Le langage de programmation Python permet d'utiliser une boucle à l'intérieur d'une autre boucle, appelée boucle imbriquée.
# La section suivante montre quelques exemples pour illustrer le concept.

# Syntaxe des boucles imbriquées :
# for variable_iteratrice in séquence:
#    for variable_iteratrice in séquence:
#        instructions(s)
#    instructions(s)

# La syntaxe d'une boucle while imbriquée dans le langage de programmation Python est la suivante :
# while expression:
#    while expression: 
#        instruction(s)
#    instruction(s)

# À noter sur l'imbrication de boucles est que nous pouvons mettre n'importe quel type de boucle à l'intérieur de n'importe quel autre type de boucle.
# Par exemple, une boucle for peut être à l'intérieur d'une boucle while ou vice versa.

# Exemple : Ce code Python utilise des boucles 'for' imbriquées pour créer un motif triangulaire de nombres.
# Il itère de 1 à 4 et, à chaque itération, imprime le nombre actuel plusieurs fois en fonction du numéro d'itération.
# Le résultat est un motif de nombres en forme de pyramide.


for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()

# Sortie :
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 

# Instructions de contrôle de boucle
# Les instructions de contrôle de boucle modifient l'exécution de la séquence normale.
# Lorsque l'exécution quitte une portée, tous les objets automatiques créés dans cette portée sont détruits. Python prend en charge les instructions de contrôle suivantes.

# Instruction Continue
# L'instruction continue en Python renvoie le contrôle au début de la boucle.

# Exemple : Ce code Python itère à travers les caractères de la chaîne 'geeksforgeeks'.
# Lorsqu'il rencontre les caractères 'e' ou 's', il utilise l'instruction continue pour sauter l'itération en cours et continuer avec le caractère suivant.
# Pour tous les autres caractères, il imprime "Current Letter :" suivi du caractère. Ainsi, la sortie affichera tous les caractères sauf 'e' et 's', chacun sur une ligne séparée.

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)

# Sortie :
# Current Letter : g
# Current Letter : k
# Current Letter : f
# Current Letter : o
# Current Letter : r
# Current Letter : g
# Current Letter : k

# Instruction Break
# L'instruction break en Python fait sortir le contrôle de la boucle.

# Exemple : Dans ce code Python, il itère à travers les caractères de la chaîne 'geeksforgeeks'.
# Lorsqu'il rencontre les caractères 'e' ou 's', il utilise l'instruction break pour sortir de la boucle.
# Après la terminaison de la boucle, il imprime "Current Letter :" suivi du dernier caractère rencontré dans la boucle (soit 'e' soit 's').
# Ainsi, la sortie affichera "Current Letter :" suivi de la première occurrence de 'e' ou 's' dans la chaîne.

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break

print('Current Letter :', letter)

# Sortie :
# Current Letter : e

# Instruction Pass
# Nous utilisons l'instruction pass en Python pour écrire des boucles vides.
# Pass est également utilisé pour des instructions de contrôle vides, des fonctions et des classes.

# Exemple : Ce code Python itère à travers les caractères de la chaîne 'geeksforgeeks' à l'aide d'une boucle 'for'.
# Cependant, il n'effectue aucune action spécifique dans la boucle, et l'instruction 'pass' est utilisée.
# Après la boucle, il imprime "Last Letter :" suivi du dernier caractère dans la chaîne, qui est 's'.

for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)

# Sortie :
# Last Letter : s

# Comment fonctionne la boucle For en Python en interne ?
# Avant de passer à cette section, vous devriez avoir une compréhension préalable des itérateurs Python.

# Tout d'abord, voyons à quoi ressemble une simple boucle 'for'.

# Exemple : Ce code Python itère à travers une liste appelée fruits, contenant "pomme", "orange" et "kiwi".
# Il imprime chaque nom de fruit sur une ligne séparée, les affichant dans l'ordre où ils apparaissent dans la liste.

fruits = ["pomme", "orange", "kiwi"]
 
for fruit in fruits:
    print(fruit)

# Sortie :
# pomme
# orange
# kiwi
    

# Ici, nous pouvons voir que la boucle 'for' itère sur l'objet itérable fruit qui est une liste.
# Les listes, ensembles, dictionnaires sont quelques-uns des objets itérables tandis qu'un objet entier n'est pas un objet itérable.
# Les boucles 'for' peuvent itérer sur l'un de ces objets itérables.

# Ce code Python itère manuellement à travers une liste de fruits en utilisant un itérateur.
