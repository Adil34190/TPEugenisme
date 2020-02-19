import random
import string

class IndividuItineraire:

    def __init__(self):
        self._itinéraire = dict()
        for i in range (0,11):
            coordonnées = list()
            ville = random.choice('ADBCDEFGHIJK')
            while ville in self._itinéraire.keys():
                ville = random.choice('ADBCDEFGHIJK')
            x = random.randrange(100)
            y = random.randrange(100)
            coordonnées.append(x)
            coordonnées.append(y)
            self._itinéraire[ville] = coordonnées
    
    def getItinéraire(self):
        return self._itinéraire