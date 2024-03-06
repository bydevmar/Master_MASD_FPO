with open("tableMultiplication.txt", "w") as fichier :
    for i in range(2 , 31):
        for j in range(1 , 21):
            ligne = f"{i} x {j} = {i*j}"
            fichier.write(ligne + "\n")
        