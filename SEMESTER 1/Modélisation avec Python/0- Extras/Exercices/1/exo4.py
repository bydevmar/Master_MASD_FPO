# Auteur : BOUHLALI Abdelfattah - [ BYDEVMAR ]

# Fonction de conversion des secondes en années, mois, jours, minutes et secondes
def convertir_secondes(secondes):
    # Nombre de secondes dans une minute, une heure, un jour et un an
    secondes_par_minute = 60
    secondes_par_heure = 60 * secondes_par_minute
    secondes_par_jour = 24 * secondes_par_heure
    secondes_par_an = 365 * secondes_par_jour

    # Calcul des années, mois, jours, minutes et secondes
    ans = secondes // secondes_par_an
    reste = secondes % secondes_par_an
    mois = reste // (30 * secondes_par_jour)  # Estimation de 30 jours par mois
    reste %= 30 * secondes_par_jour
    jours = reste // secondes_par_jour
    reste %= secondes_par_jour
    heures = reste // secondes_par_heure
    reste %= secondes_par_heure
    minutes = reste // secondes_par_minute
    reste %= secondes_par_minute
    secondes = reste

    # Affichage du résultat
    print(f"{ans} an(s), {mois} mois, {jours} jour(s), {heures} heure(s), {minutes} minute(s), {secondes} seconde(s)")

# Exemple d'utilisation avec un nombre de secondes
nombre_secondes = 123456789
convertir_secondes(nombre_secondes)
