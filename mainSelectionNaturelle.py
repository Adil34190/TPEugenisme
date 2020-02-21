from Eugenisme_phrase import EugenismePhrase
from Eugenisme_itineraire import EugenismeItineraire
import matplotlib.pyplot as plt
import string

def phrase(l_cible, nb_population, taux_selection):
    cible = l_cible
    eug = EugenismePhrase(nb_population,len(cible))
    population = eug.get_population()
    indivtri = eug.Tri(cible,population)
    
    while indivtri[0][1] != 1:
        eug.Selection(cible, (taux_selection/100))
        eug.Crossover()
        population = eug.get_population()
        indivtri = eug.Tri(cible,population)
        print(indivtri[0][0])


def itineraire( nb_population, taux_selection, nb_villes = 30):
    eug = EugenismeItineraire(nb_population, nb_villes)
    fig = plt.gcf()
    fig.show()
    fig.canvas.draw()
    i = 0
    while 1:
        i += 1
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
        fitness = eug.Fitness(Itinéraires[0])

            # Set chart title.
        plt.title("fitness : " + str(fitness) + " nb essais: " + str(i) )

        fig.canvas.draw()

        eug.Selection((taux_selection/100))
        eug.Crossover()

mode = str((input("Sélectionnez le mode: Phrase/Itinéraire: ")))

if mode in ["Phrase","phrase"]:
    cible = str((input("Sélectionnez une cible(caractères accéptés: ' ; é ; majuscules ; minuscules): ")))
    taux = input("Sélectionnez un taux (maximun 100, minimum 10): ")
    while str.isnumeric(taux) == False:
        print("taux incorrect")
        taux = input("Sélectionnez un taux (maximun 100, minimum 10): ")
    while int(taux) > 100 or int(taux) < 10:
        print("taux incorrect")
        taux = input("Sélectionnez un taux (maximun 100, minimum 10): ")
    nombre = input("Sélectionnez un nombre de population à gnérer (maximun 1000, minimum 50): ")
    while str.isnumeric(nombre) == False:
        print("nombre incorrect")
        nombre = input("Sélectionnez un nombre de population à gnérer (maximun 1000, minimum 50): ")
    while int(nombre) > 1000 or int(nombre) < 50:
        print("nombre incorrect")
        nombre = input("Sélectionnez un nombre de population à gnérer (maximun 1000, minimum 50): ")
    phrase(cible,int(nombre),int(taux))
elif mode in ['Itinéraire','itinéraire','Itineraire','itineraire','Itinéraires','itinéraires','Itineraires','itineraires']:
    taux = input("Sélectionnez un taux (maximun 100, minimum 10)(Optimal = 10): ")
    while str.isnumeric(taux) == False:
        print("taux incorrect")
        taux = input("Sélectionnez un taux (maximun 100, minimum 10): ")
    while int(taux) > 100 or int(taux) < 10:
        print("taux incorrect")
        taux = input("Sélectionnez un taux (maximun 100, minimum 10): ")
    nombre = input("Sélectionnez un nombre de population à gnérer (maximun 1000, minimum 50): ")
    while str.isnumeric(nombre) == False:
        print("nombre incorrect")
        nombre = input("Sélectionnez un nombre de population à gnérer (maximun 1000, minimum 50): ")
    while int(nombre) > 1000 or int(nombre) < 50:
        print("nombre incorrect")
        nombre = input("Sélectionnez un nombre de population à gnérer (maximun 1000, minimum 50): ")
    itineraire(int(nombre),int(taux))