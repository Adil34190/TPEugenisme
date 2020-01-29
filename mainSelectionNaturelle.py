from Individu_phrase import IndividuPhrase
from Eugenisme_phrase import EugenismePhrase

cible = "La marche du vertueux"
eug = EugenismePhrase(50,len(cible))
population = eug.get_population()
indivtri = eug.triIndividu(cible,population)

while indivtri[0][1] != 1:
    eug.Selection(cible, 0.2)
    eug.Crossover()
    population = eug.get_population()
    indivtri = eug.triIndividu(cible,population)
    print(indivtri[0][0])
    