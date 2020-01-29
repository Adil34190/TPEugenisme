from Individu import Individu
from Eugenisme import Eugenisme

cible = "Paul le gros KING BODERL"
eug = Eugenisme(100,len(cible))
population = eug.get_population()
indivtri = eug.triIndividu(cible,population)

while indivtri[0][1] != 1:
    eug.Selection(cible, 0.5)
    eug.Crossover()
    population = eug.get_population()
    indivtri = eug.triIndividu(cible,population)
    print(indivtri[0][0])
    