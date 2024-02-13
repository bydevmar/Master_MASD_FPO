"""
Exo 4 :
À partir de deux fichiers préexistants A et B, construisez un fichier C qui contienne alternativement un élément de A, un élément de B, un élément de A... et ainsi de suite jusqu'à atteindre la fin de l'un des deux fichiers originaux. Complétez ensuite C avec les éléments restant sur l'autre.

Solution : 
"""

def construire_fichier_c(fichier_a, fichier_b, fichier_c):
    try:
        with open(fichier_a, 'r') as a, open(fichier_b, 'r') as b:
            lignes_a = a.readlines()
            lignes_b = b.readlines()

            min_len = min(len(lignes_a), len(lignes_b))

            with open(fichier_c, 'w') as c:
                for i in range(min_len):
                    c.write(lignes_a[i])
                    c.write(lignes_b[i])

                # Compléter avec les éléments restants du fichier A
                c.writelines(lignes_a[min_len:])

                # Compléter avec les éléments restants du fichier B
                c.writelines(lignes_b[min_len:])

            print(f"Le fichier {fichier_c} a été créé avec succès.")

    except FileNotFoundError:
        print("L'un des fichiers n'a pas été trouvé.")

if __name__ == "__main__":
    fichier_a = input("Entrez le nom du premier fichier (A) : ")
    fichier_b = input("Entrez le nom du deuxième fichier (B) : ")
    fichier_c = input("Entrez le nom du fichier résultant (C) : ")

    construire_fichier_c(fichier_a, fichier_b, fichier_c)
