
# Opérateurs de comparaison en Python
# Les opérateurs de comparaison en Python sont très importants dans les instructions conditionnelles (if, else et elif) et les boucles (while et for). Les opérateurs de comparaison sont également appelés opérateurs relationnels. Certains des opérateurs bien connus sont "<" signifiant inférieur à et ">" signifiant opérateur supérieur à.

# Python utilise deux autres opérateurs en combinant le symbole "=" avec ces deux-là. Le symbole "<=" est pour l'opérateur inférieur ou égal et le symbole ">=" est pour l'opérateur supérieur ou égal.

# Python a deux autres opérateurs de comparaison sous la forme de "==" et "!=". Ce sont les opérateurs d'égalité et de non-égalité. Ainsi, il y a six opérateurs de comparaison en Python et ils sont répertoriés ci-dessous dans ce tableau :

# <     Inférieur à             a<b
# >     Supérieur à             a>b
# <=    Inférieur ou égal à     a<=b
# >=    Supérieur ou égal à     a>=b
# ==    Égal à                  a==b
# !=    Différent de             a!=b

# Les opérateurs de comparaison sont binaires en nature, nécessitant deux opérandes. Une expression impliquant un opérateur de comparaison est appelée une expression booléenne et retourne toujours soit True soit False.

# Exemple d'utilisation des opérateurs de comparaison en Python :

# Déclaration des variables
a = 5
b = 7

# Utilisation des opérateurs de comparaison
print(a > b)  # False
print(a < b)  # True

# Les deux opérandes peuvent être des littéraux Python, des variables ou des expressions. Comme Python prend en charge l'arithmétique mixte, vous pouvez avoir des opérandes de n'importe quel type de nombre.

# Exemple d'utilisation des opérateurs de comparaison avec des nombres entiers en Python :
print("Les deux opérandes sont des entiers")
a = 5
b = 7
print("a=", a, "b=", b, "a>b est", a > b)
print("a=", a, "b=", b, "a<b est", a < b)
print("a=", a, "b=", b, "a==b est", a == b)
print("a=", a, "b=", b, "a!=b est", a != b)

# Production de la sortie suivante −

# Les deux opérandes sont des entiers
# a= 5 b= 7 a>b est False
# a= 5 b= 7 a<b est True
# a= 5 b= 7 a==b est False
# a= 5 b= 7 a!=b est True

# Comparaison des nombres à virgule flottante
# Dans l'exemple suivant, un opérande entier et un opérande à virgule flottante sont comparés.

print("Comparaison d'entier et de flottant")
a = 10
b = 10.0
print("a=", a, "b=", b, "a>b est", a > b)
print("a=", a, "b=", b, "a<b est", a < b)
print("a=", a, "b=", b, "a==b est", a == b)
print("a=", a, "b=", b, "a!=b est", a != b)

# Production de la sortie suivante −

# Comparaison d'entier et de flottant
# a= 10 b= 10.0 a>b est False
# a= 10 b= 10.0 a<b est False
# a= 10 b= 10.0 a==b est True
# a= 10 b= 10.0 a!=b est False

# Comparaison des nombres complexes
# Bien que l'objet complexe soit un type de données numériques en Python, son comportement est différent des autres. Python ne prend pas en charge les opérateurs < et >, mais prend en charge les opérateurs d'égalité (==) et de non-égalité (!=).

print("Comparaison de nombres complexes")
a = 10 + 1j
b = 10.0 - 1j
print("a=", a, "b=", b, "a==b est", a == b)
print("a=", a, "b=", b, "a!=b est", a != b)

# Production de la sortie suivante −

# Comparaison de nombres complexes
# a= (10+1j) b= (10-1j) a==b est False
# a= (10+1j) b= (10-1j) a!=b est True

# Vous obtenez une TypeError avec les opérateurs inférieur à ou supérieur à.

print("Comparaison de nombres complexes")
a = 10 + 1j
b = 10.0 - 1j
print("a=", a, "b=", b, "a<b est", a < b)
print("a=", a, "b=", b, "a>b est", a > b)

# Production de la sortie suivante −

# Comparaison de nombres complexes
# Traceback (most recent call last):
#   File "C:\Users\mlath\examples\example.py", line 5, in <module>
#     print("a=", a, "b=", b, "a<b est", a < b)
#                                       ^^^
# TypeError: '<' not supported between instances of 'complex' and 'complex

# Comparaison des booléens
# Les objets booléens en Python sont en réalité des entiers : True est 1 et False est 0. En fait, Python considère tout nombre non nul comme True. En Python, la comparaison des objets booléens est possible. "False < True" est True!

print("Comparaison des booléens")
a = True
b = False
print("a=", a, "b=", b, "a<b est", a < b)
print("a=", a, "b=", b, "a>b est", a > b)
print("a=", a, "b=", b, "a==b est", a == b)
print("a=", a, "b=", b, "a!=b est", a != b)

# Production de la sortie suivante −

# Comparaison des booléens
# a= True b= False a<b est False
# a= True b= False a>b est True
# a= True b= False a==b est False
# a= True b= False a!=

#b est True

# Comparaison des types de séquences
# En Python, la comparaison ne peut être effectuée que sur des objets de séquence similaires. Un objet de chaîne peut être comparé avec une autre chaîne uniquement. Une liste ne peut pas être comparée à un tuple, même si les deux ont les mêmes éléments.

print("Comparaison de types de séquences différents")
a = (1, 2, 3)
b = [1, 2, 3]
print("a=", a, "b=", b, "a<b est", a < b)

# Production de la sortie suivante −

# Comparaison de types de séquences différents
# Traceback (most recent call last):
#   File "C:\Users\mlath\examples\example.py", line 5, in <module>
#     print("a=", a, "b=", b, "a<b est", a < b)
#                                       ^^^
# TypeError: '<' not supported between instances of 'tuple' and 'list'

# Les objets de séquence sont comparés par un mécanisme d'ordonnancement lexicographique. La comparaison commence à partir de l'élément à l'index 0. S'ils sont égaux, la comparaison passe à l'index suivant jusqu'à ce que les éléments à un certain index ne soient pas égaux, ou l'une des séquences est épuisée. Si une séquence est une sous-séquence initiale de l'autre, la séquence la plus courte est considérée comme la plus petite (moins grande).

# Lequel des opérandes est le plus grand dépend de la différence de valeurs des éléments à l'index où ils ne sont pas égaux. Par exemple, 'BAT'>'BAR' est True, car T vient après R dans l'ordre Unicode.

# Si tous les éléments de deux séquences sont égaux, les séquences sont considérées comme égales.

print("Comparaison de chaînes")
a = 'BAT'
b = 'BALL'
print("a=", a, "b=", b, "a<b est", a < b)
print("a=", a, "b=", b, "a>b est", a > b)
print("a=", a, "b=", b, "a==b est", a == b)
print("a=", a, "b=", b, "a!=b est", a != b)

# Production de la sortie suivante −

# Comparaison de chaînes
# a= BAT b= BALL a<b est False
# a= BAT b= BALL a>b est True
# a= BAT b= BALL a==b est False
# a= BAT b= BALL a!=b est True

# Dans l'exemple suivant, deux objets de tuple sont comparés −

print("Comparaison de tuples")
a = (1, 2, 4)
b = (1, 2, 3)
print("a=", a, "b=", b, "a<b est", a < b)
print("a=", a, "b=", b, "a>b est", a > b)
print("a=", a, "b=", b, "a==b est", a == b)
print("a=", a, "b=", b, "a!=b est", a != b)

# Production de la sortie suivante −

# a= (1, 2, 4) b= (1, 2, 3) a<b est False
# a= (1, 2, 4) b= (1, 2, 3) a>b est True
# a= (1, 2, 4) b= (1, 2, 3) a==b est False
# a= (1, 2, 4) b= (1, 2, 3) a!=b est True

# Comparaison des objets de dictionnaire
# L'utilisation des opérateurs "<" et ">" pour le dictionnaire Python n'est pas définie. En cas de ces opérandes, TypeError: '<' not supported between instances of 'dict' and 'dict' est signalée.

# La comparaison d'égalité vérifie si la longueur des éléments de dict est la même. La longueur du dictionnaire est le nombre de paires clé-valeur qu'il contient.

# Les dictionnaires Python sont simplement comparés par longueur. Le dictionnaire avec moins d'éléments est considéré comme inférieur à un dictionnaire avec plus d'éléments.

print("Comparaison d'objets de dictionnaire")
a = {1: 1, 2: 2}
b = {2: 2, 1: 1, 3: 3}
print("a=", a, "b=", b, "a==b est", a == b)
print("a=", a, "b=", b, "a!=b est", a != b)

# Production de la sortie suivante −

# Comparaison d'objets de dictionnaire
# a= {1: 1, 2: 2} b= {2: 2, 1: 1, 3: 3} a==b est False
# a= {1: 1, 2: 2} b= {2: 2, 1: 1, 3: 3} a!=b est True
