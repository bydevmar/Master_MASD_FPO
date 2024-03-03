#Exercice 1

t1 = [31,28,31]
t2 = ['janvier','Fevrier','Mars']
t3 = []

for i in range(len(t1)):
    t3.append(t2[i])
    t3.append(t1[i])

print(t3)