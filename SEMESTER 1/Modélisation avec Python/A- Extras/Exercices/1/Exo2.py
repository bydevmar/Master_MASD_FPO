# Auteur : BOUHLALI Abdelfattah - [ BYDEVMAR ]

# Initialisation de la première somme en euros
somme_euros = 1

# Boucle pour itérer jusqu'à ce que la somme atteigne ou dépasse 16384 euros
while somme_euros <= 16384:
    # Conversion de la somme en dollars canadiens (taux de change fixe)
    somme_dollars = somme_euros * 1.65
    
    # Affichage de la conversion
    print(f"{somme_euros} euro(s) = {somme_dollars:.2f} dollar(s)")
    
    # Doublement de la somme en euros pour la progression géométrique
    somme_euros *= 2

# Fin du programme
