liste1 = ['A','B','C','D','E','F','G','H']
liste2 = ['B','D','G','C','A','F','E','H']
taille = round(len(liste1)/2)
enfant = liste1[(taille - 1):(taille + 2)]
print(enfant)
for i in range(0, len(enfant)):
    liste2.remove(enfant[i])
print(liste2)
liste2[round(len(liste2)/2):round(len(liste2)/2)] = enfant
print(liste2)