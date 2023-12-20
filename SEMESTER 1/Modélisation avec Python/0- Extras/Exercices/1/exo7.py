# Auteur : BOUHLALI Abdelfattah - [ BYDEVMAR ]

# Chaîne à recopier
chaine_originale = "masd"

# Initialisation de la nouvelle chaîne avec le premier caractère de la chaîne originale
nouvelle_chaine = chaine_originale[0]

# Boucle pour parcourir les caractères de la chaîne originale à partir du deuxième
for caractere in chaine_originale[1:]:
    # Ajout de l'astérisque et du caractère à la nouvelle chaîne
    nouvelle_chaine += f"*{caractere}"

# Affichage du résultat
print(f"Ancienne chaîne : {chaine_originale}")
print(f"Nouvelle chaîne : {nouvelle_chaine}")
