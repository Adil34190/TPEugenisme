from Individu_phrase import IndividuPhrase
from individu_itineraire import IndividuItineraire
from Eugenisme_phrase import EugenismePhrase

<<<<<<< HEAD
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
=======
############Individu##################
# cible = "La marche du vertueux"
# eug = EugenismePhrase(100,len(cible))
# population = eug.get_population()
# indivtri = eug.triIndividu(cible,population)

# while indivtri[0][1] != 1:
#     eug.Selection(cible, 0.5)
#     eug.Crossover()
#     population = eug.get_population()
#     indivtri = eug.triIndividu(cible,population)
#     print(indivtri[0][0])

itinairaire = IndividuItineraire()
print(itinairaire.getItinéraire())
>>>>>>> 0b830f438fb4e735cc7a6ffdbc8ef15131b91088
    