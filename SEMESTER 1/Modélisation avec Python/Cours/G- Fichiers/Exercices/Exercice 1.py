"""
#EXO 1 : 

Écrivez un script qui permette de créer et de relire aisément un fichier texte.
Votre programme demandera d'abord à l'utilisateur d'entrer le nom du fichier. 
Ensuite il lui proposera le choix, soit d'enregistrer de nouvelles lignes de texte,
soit d'afficher le contenu du fichier. L'utilisateur devra pouvoir entrer ses lignes de texte
successives en utilisant simplement la touche <Enter> pour les séparer les unes des autres.
Pour terminer les entrées, il lui suffira d'entrer une ligne vide (c'est-à-dire utiliser 
la touche <Enter> seule). L'affichage du contenu devra montrer les lignes du fichier séparées les
unes des autres de la manière la plus naturelle (les codes de fin de ligne ne doivent pas apparaître).


Sol :
"""

def main():
    # Demander à l'utilisateur d'entrer le nom du fichier
    nom_fichier = input("Nom du fichier : ")
   

    # Boucle principale
    while True:
        # Demander à l'utilisateur ce qu'il souhaite faire
        choix = input("(E)nregistrer | (A)fficher | (Q)uitter : ")

        # Enregistrer des lignes
        if choix == "E":
            # Lire les lignes de texte saisies par l'utilisateur
            lignes = input("Lignes de texte (terminer par une ligne vide) : ")
            with open(nom_fichier, "r+") as fichier :
                # Écrire les lignes dans le fichier
                for ligne in lignes.split("\n"):
                    fichier.write(ligne + "\n")

        # Afficher le contenu du fichier
        elif choix == "A":
            # Lire le contenu du fichier
            with open(nom_fichier, "r+") as fichier:
                lignes = fichier.readlines()

            # Afficher les lignes
            for ligne in lignes:
                print(ligne.rstrip("\n"))

        # Quitter le programme
        elif choix == "Q":
            break

    


if __name__ == "__main__":
    main()
