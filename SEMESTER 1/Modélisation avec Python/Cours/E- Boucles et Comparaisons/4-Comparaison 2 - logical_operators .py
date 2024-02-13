
# Opérateurs logiques en Python
# Les opérateurs logiques en Python sont utilisés pour former des expressions booléennes composées. Chaque opérande pour ces opérateurs logiques est lui-même une expression booléenne. Par exemple,

# age > 16 and marks > 80
# percentage < 50 or attendance < 75

# Avec le mot-clé False, Python interprète None, zéro numérique de tous les types et les séquences vides (chaînes, tuples, listes), les dictionnaires vides et les ensembles vides comme False. Toutes les autres valeurs sont traitées comme True.

# Il existe trois opérateurs logiques en Python. Ce sont "and", "or" et "not". Ils doivent être en minuscules.

# L'opérateur "and"
# Pour que l'expression booléenne composée soit vraie, les deux opérandes doivent être vrais. Si l'un ou les deux opérandes s'évaluent à False, l'expression retourne False. Le tableau suivant montre les scénarios.

# a    b    a and b
# F    F    F
# F    T    F
# T    F    F
# T    T    T

# L'opérateur "or"
# En revanche, l'opérateur or retourne True si l'un des opérandes est True. Pour que l'expression booléenne composée soit False, les deux opérandes doivent être False, comme le montre le tableau suivant −

# a    b    a or b
# F    F    F
# F    T    T
# T    F    F
# T    T    T

# L'opérateur "not"
# Il s'agit d'un opérateur unaire. L'état de l'opérande booléen qui suit est inversé. Par conséquent, not True devient False et not False devient True.

# a    not (a)
# F    T
# T    F

# Comment l'interpréteur Python évalue-t-il les opérateurs logiques ?
# L'expression "x and y" évalue d'abord "x". Si "x" est faux, sa valeur est renvoyée; sinon, "y" est évalué et la valeur résultante est renvoyée.

# L'expression "x or y" évalue d'abord "x"; si "x" est vrai, sa valeur est renvoyée; sinon, "y" est évalué et la valeur résultante est renvoyée.

# Certains cas d'utilisation des opérateurs logiques sont donnés ci-dessous −

x = 10
y = 20
print("x > 0 and x < 10:", x > 0 and x < 10)
print("x > 0 and y > 10:", x > 0 and y > 10)
print("x > 10 or y > 10:", x > 10 or y > 10)
print("x%2 == 0 and y%2 == 0:", x % 2 == 0 and y % 2 == 0)
print("not (x+y>15):", not (x+y) > 15)

# Produira la sortie suivante −

# x > 0 and x < 10: False
# x > 0 and y > 10: True
# x > 10 or y > 10: True
# x%2 == 0 and y%2 == 0: True
# not (x+y>15): False

# Nous pouvons utiliser des opérandes non booléens avec des opérateurs logiques. Ici, nous devons noter que tous les nombres non nuls et les séquences non vides sont évalués à True. Par conséquent, les mêmes tables de vérité des opérateurs logiques s'appliquent.

# Dans l'exemple suivant, des opérandes numériques sont utilisés pour des opérateurs logiques. Les variables "x", "y" sont évaluées à True, "z" est False

x = 10
y = 20
z = 0
print("x and y:", x and y)
print("x or y:", x or y)
print("z or x:", z or x)
print("y or z:", y or z)

# Produira la sortie suivante −

# x and y: 20
# x or y: 10
# z or x: 10
# y or z: 20

# La variable de chaîne est traitée comme True et un tuple vide comme False dans l'exemple suivant −

a = "Hello"
b = tuple()
print("a and b:", a and b)
print("b or a:", b or a)

# Produira la sortie suivante −

# a and b: ()
# b or a: Hello

# Enfin, deux objets de liste ci-dessous ne sont pas vides. Par conséquent, x et y renvoient ce dernier, et x or y renvoie le premier.

x = [1, 2, 3]
y = [10, 20, 30]
print("x and y:", x and y)
print("x or y:", x or y)

# Produira la sortie suivante −

# x and y: [10, 20, 30]
# x or y: [1, 2, 3]
