"""
Exercice : 
Écrivez un script qui génère automatiquement un fichier texte contenant les tables 
de multiplication de 2 à 30 (chacune d'entre elles incluant 20 termes seulement).

Sol : 
"""

# Fonction pour générer la table de multiplication
def generer_table_multiplication(nombre, limite):
    table = [f"{nombre} x {i} = {nombre * i}" for i in range(1, limite + 1)]
    return table

# Fonction pour écrire dans un fichier
def ecrire_dans_fichier(chemin, contenu):
    with open(chemin, 'w') as fichier:
        for ligne in contenu:
            fichier.write(f"{ligne}\n")

# Générer les tables de multiplication de 2 à 30 avec 20 termes chacune
tables_multiplication = {}
for i in range(2, 31):
    tables_multiplication[i] = generer_table_multiplication(i, 20)

# Écrire les tables dans un fichier texte
chemin_fichier = "tables_multiplication.txt"
with open(chemin_fichier, 'w') as fichier:
    for nombre, table in tables_multiplication.items():
        fichier.write(f"Table de multiplication de {nombre} :\n")
        fichier.write('\n'.join(table))
        fichier.write("\n\n")

print(f"Les tables de multiplication ont été générées avec succès dans le fichier : {chemin_fichier}")
