# Exo 3 :
# Écrivez un script qui compare les contenus de deux fichiers et signale la première différence rencontrée.

# Solution : 

def comparer_fichiers(nom_fichier1, nom_fichier2):
    try:
        with open(nom_fichier1, 'r') as fichier1, open(nom_fichier2, 'r') as fichier2:
            lignes_fichier1 = fichier1.readlines()
            lignes_fichier2 = fichier2.readlines()

            min_len = min(len(lignes_fichier1), len(lignes_fichier2))

            for i in range(min_len):
                if lignes_fichier1[i] != lignes_fichier2[i]:
                    print(f"Différence détectée à la ligne {i + 1}:")
                    print(f"Contenu fichier 1 : {lignes_fichier1[i].strip()}")
                    print(f"Contenu fichier 2 : {lignes_fichier2[i].strip()}")
                    return

            if len(lignes_fichier1) != len(lignes_fichier2):
                print(f"Les fichiers ont une longueur différente à la ligne {min_len + 1}.")
            else:
                print("Les fichiers sont identiques.")
    
    except FileNotFoundError:
        print("L'un des fichiers n'a pas été trouvé.")

if __name__ == "__main__":
    nom_fichier1 = input("Entrez le nom du premier fichier : ")
    nom_fichier2 = input("Entrez le nom du deuxième fichier : ")

    comparer_fichiers(nom_fichier1, nom_fichier2)


"""
output : 

Entrez le nom du premier fichier : A.txt
Entrez le nom du deuxième fichier : B.txt
Différence détectée à la ligne 2:
Contenu fichier 1 : MASD
Contenu fichier 2 : MA_SD

"""
