# **Exercice 2:**

# Calculer la somme d'une série de nombres positifs ou nuls. Compter combien il y 
# en avait et combien étaient supérieurs à 100.

# Eehe : le nombre zéro ou égal à 6 indique la fin de la série

somme = 0
nombre_total = 0
nombre_sup_100 = 0

while True:
    nombre = int(input("Entrez un nombre (0 pour terminer) : "))
    if nombre == 0 or nombre == 6:
        break
    nombre_total += 1
    somme += nombre
    if nombre > 100:
        nombre_sup_100 += 1

print(f"Somme des nombres : {somme}")
print(f"Nombre total de nombres saisis : {nombre_total}")
print(f"Nombre de nombres supérieurs à 100 : {nombre_sup_100}")

# **Exercice 3:**

# L'utilisateur saisit un entier positif et le programme annonce combien de fois de suite cet entier 
# est divisible par 2

entier = int(input("Entrez un entier positif : "))
compteur = 0

while entier > 0 and entier % 2 == 0:
    compteur += 1
    entier //= 2

print(f"L'entier est divisible par 2 {compteur} fois de suite.")

# **Exercice 4:**

# Écrire un programme qui demande à l'utilisateur de saisir un nombre N et affiche ensuite les N premiers nombres pairs.

N = int(input("Entrez un nombre entier positif N : "))
nombres_pairs = [i for i in range(2, 2*N+1, 2)]
print(f"Les {N} premiers nombres pairs sont : {nombres_pairs}")

# **Exercice 5:**

# Écrire un programme qui demande à l'utilisateur de saisir un nombre N et affiche ensuite les N premiers nombres impairs.

N = int(input("Entrez un nombre entier positif N : "))
nombres_impairs = [i for i in range(1, 2*N, 2)]
print(f"Les {N} premiers nombres impairs sont : {nombres_impairs}")

# **Exercice 6:**

# Écrire un programme qui demande à l'utilisateur de saisir deux nombres A et B et affiche ensuite tous les nombres pairs compris entre A et B.

A = int(input("Entrez le nombre entier A : "))
B = int(input("Entrez le nombre entier B : "))
nombres_pairs_entre_A_et_B = [i for i in range(A + (A % 2), B + 1, 2)]
print(f"Les nombres pairs entre {A} et {B} sont : {nombres_pairs_entre_A_et_B}")

# **Exercice 7:**

# Écrire un programme qui demande à l'utilisateur de saisir deux nombres A et B et affiche ensuite tous les nombres impairs compris entre A et B.

A = int(input("Entrez le nombre entier A : "))
B = int(input("Entrez le nombre entier B : "))
nombres_impairs_entre_A_et_B = [i for i in range(A + (A % 2), B + 1, 2)]
print(f"Les nombres impairs entre {A} et {B} sont : {nombres_impairs_entre_A_et_B}")

# **Exercice 8:**

# Écrire un programme qui demande à l'utilisateur de saisir un nombre N et affiche ensuite la table de multiplication de N.

N = int(input("Entrez un nombre entier positif N : "))
for i in range(1, 11):
    print(f"{N} * {i} = {N * i}")

# **Exercice 9:**

# Écrire un programme qui demande à l'utilisateur de saisir un nombre N et affiche ensuite les N premiers nombres premiers.

def est_premier(nombre):
    if nombre < 2:
        return False
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False
    return True

N = int(input("Entrez un nombre entier positif N : "))
nombres_premiers = [i for i in range(2, N*10) if est_premier(i)][:N]
print(f"Les {N} premiers nombres premiers sont : {nombres_premiers}")


# **Exercice 10:**

# Écrire un programme qui demande à l'utilisateur de saisir un nombre N et affiche ensuite la factorielle de N.

def factorielle(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorielle(n-1)

N = int(input("Entrez un nombre entier positif N : "))
resultat_factorielle = factorielle(N)
print(f"La factorielle de {N} est : {resultat_factorielle}")

# **Exercice 11:**

# Écrire un programme qui demande à l'utilisateur de saisir deux nombres A et B et affiche ensuite le plus grand commun diviseur (PGCD) de A et B.

def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

A = int(input("Entrez le nombre entier A : "))
B = int(input("Entrez le nombre entier B : "))
resultat_pgcd = pgcd(A, B)
print(f"Le PGCD de {A} et {B} est : {resultat_pgcd}")

# **Exercice 12:**

# Écrire un programme qui demande à l'utilisateur de saisir deux nombres A et B et affiche ensuite le plus petit commun multiple (PPCM) de A et B.

def ppcm(a, b):
    return abs(a * b) // pgcd(a, b)

A = int(input("Entrez le nombre entier A : "))
B = int(input("Entrez le nombre entier B : "))
resultat_ppcm = ppcm(A, B)
print(f"Le PPCM de {A} et {B} est : {resultat_ppcm}")


# **Exercice 13:**

# Écrire un programme qui demande à l'utilisateur de saisir un nombre N et affiche ensuite la somme des N premiers nombres naturels.

N = int(input("Entrez un nombre entier positif N : "))
somme_nombres_naturels = N * (N + 1) // 2
print(f"La somme des {N} premiers nombres naturels est : {somme_nombres_naturels}")

# **Exercice 14:**

# Écrire un programme qui demande à l'utilisateur de saisir un nombre N et affiche ensuite la moyenne des N premiers nombres naturels.

N = int(input("Entrez un nombre entier positif N : "))
moyenne_nombres_naturels = (N + 1) / 2
print(f"La moyenne des {N} premiers nombres naturels est : {moyenne_nombres_naturels}")

# **Exercice 15:**

# Écrire un programme qui demande à l'utilisateur de saisir un nombre N et affiche ensuite la médiane des N premiers nombres naturels.

N = int(input("Entrez un nombre entier positif N : "))
if N % 2 == 0:
    mediane_nombres_naturels = N / 2
else:
    mediane_nombres_naturels = (N + 1) / 2
print(f"La médiane des {N} premiers nombres naturels est : {mediane_nombres_naturels}")


# **Exercice 16:**

# Écrire un programme qui demande à l'utilisateur de saisir un nombre N et affiche ensuite la variance des N premiers nombres naturels.

N = int(input("Entrez un nombre entier positif N : "))
variance_nombres_naturels = N * (N + 1) * (2 * N + 1) / 6
print(f"La variance des {N} premiers nombres naturels est : {variance_nombres_naturels}")

# **Exercice 17:**

# Écrire un programme qui demande à l'utilisateur de saisir un nombre N et affiche ensuite l'écart-type des N premiers nombres naturels.

import math

N = int(input("Entrez un nombre entier positif N : "))
ecart_type_nombres_naturels = math.sqrt(variance_nombres_naturels)
print(f"L'écart-type des {N} premiers nombres naturels est : {ecart_type_nombres_naturels}")

# **Exercice 18:**

# Écrire un programme qui demande à l'utilisateur de saisir un nombre N et affiche ensuite la distribution des N premiers nombres naturels.

# La distribution des nombres naturels est uniforme, il n'y a pas besoin de calcul supplémentaire.

N = int(input("Entrez un nombre entier positif N : "))
print(f"La distribution des {N} premiers nombres naturels est uniforme.")


# **Exercice 19:**

# Écrire un programme qui demande à l'utilisateur de saisir un nombre N et affiche ensuite le mode des N premiers nombres naturels.

# Le mode des nombres naturels est toujours 0, car chaque nombre apparaît une seule fois.

N = int(input("Entrez un nombre entier positif N : "))
print(f"Le mode des {N} premiers nombres naturels est : 0")

# **Exercice 20:**

# Écrire un programme qui demande à l'utilisateur de saisir un nombre N et affiche ensuite la kurtosis des N premiers nombres naturels.

# La kurtosis des nombres naturels est 1.8 pour une distribution normale.

N = int(input("Entrez un nombre entier positif N : "))
kurtosis_nombres_naturels = 1.8
print(f"La kurtosis des {N} premiers nombres naturels est : {kurtosis_nombres_naturels}")
