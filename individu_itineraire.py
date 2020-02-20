import random
import string

class IndividuItineraire:

    def __init__(self, nb_villes = 10):
        self._villes = list()
        self._villes_noms = dict()
        for i in range (0,nb_villes):
            coordonnées = list()
            coordonnées.append(random.randrange(100))
            coordonnées.append(random.randrange(100))
            self._villes.append(coordonnées)
            self._villes_noms['Ville'+ str(i)] = coordonnées
            
    
    def getItinéraire(self):
        return self._villes

    def get_villes_et_noms(self):
        return self._villes_noms