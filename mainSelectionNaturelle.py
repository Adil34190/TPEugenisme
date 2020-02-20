from Individu_phrase import IndividuPhrase
from individu_itineraire import IndividuItineraire
from Eugenisme_phrase import EugenismePhrase
from Eugenisme_itineraire import EugenismeItineraire
import matplotlib.pyplot as plt

""" cible = "La marche des vertueux est semée d'obstacles qui sont les entreprises égoistes que fait sans fin surgir l'oeuvre du Malin"
eug = EugenismePhrase(100,len(cible))
population = eug.get_population()
indivtri = eug.triIndividu(cible,population)

while indivtri[0][1] != 1:
    eug.Selection(cible, 0.1)
    eug.Crossover()
    population = eug.get_population()
    indivtri = eug.triIndividu(cible,population)
    print(indivtri[0][0]) """
""" ind = IndividuItineraire(30)
coordonnéeslist = ind.getItinéraire()
x_list = list()
y_list = list()

for coordonnées in coordonnéeslist:
    x_list.append(coordonnées[0])
    y_list.append(coordonnées[1])

# Draw point based on above x, y axis values.
plt.scatter(x_list, y_list, s=10)
plt.plot(x_list, y_list, linewidth=1)

    # Set chart title.
plt.title("Villes")

plt.show() """

""" ind = IndividuItineraire(30)
coordonneesdict = ind.get_villes_et_noms()
coordonnéeslist = ind.getItinéraire() """

eug = EugenismeItineraire(100)
fig = plt.gcf()
fig.show()
fig.canvas.draw()

for i in range(100):
    plt.clf()
    listevilles = eug.get_liste()
    triIti = eug.Tri(listevilles)
    x_list = list()
    y_list = list()
    Itinéraires = list(triIti.values())
    for coordonnées in Itinéraires[0]:
        x_list.append(coordonnées[0])
        y_list.append(coordonnées[1])

    # Draw point based on above x, y axis values.
    plt.scatter(x_list, y_list, s=10)
    plt.plot(x_list, y_list, linewidth=1)

        # Set chart title.
    plt.title("Villes")

    fig.canvas.draw()
    
    

    
    """ for key, value in triIti.items():    
        print('Itinéraire: ')
        print(value)
        print('Fitness: ' + str(key) + '\n') """
        
    eug.Selection(0.2)
    eug.Crossover()
    