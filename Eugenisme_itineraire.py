from Eugenisme import Eugenisme
from individu_itineraire import IndividuItineraire
from random import sample
import random
import math
from itertools import islice

class EugenismeItineraire(Eugenisme):
    
    def __init__(self, nb_population = 50, nb_villes = 20):
        self._liste_ville = []
        self._liste_itineraire = []
        self._itineraires_tries = {}
        self._itineraires_selectionnes = {}
        self._nb_itineraires = nb_population
        ind = IndividuItineraire(nb_villes)
        self._liste_ville = ind.getItinéraire()
        for i in range(0, nb_population):
            self._liste_itineraire.append(sample(self._liste_ville,len(self._liste_ville)))
        
    def Tri(self, population):
        Itis = dict()
        triIti = dict()
        for villes in population:
            fitness = self.Fitness(villes)
            Itis[fitness] = villes
        for key in sorted(Itis.keys()):
            triIti[key] = Itis.get(key)
        #print("Liste triée: \n" + str(triIti)) 
        return triIti
    
    def Fitness(self, villes):
        somme = 0
        for i in range(0, len(villes) - 1):
            if i != len(villes) - 1:
                ville1 = villes[i]
                ville2 = villes[i + 1]
                distance = math.sqrt((ville1[0] - ville2[0])**2 + (ville1[1] - ville2[1])**2)
                somme += distance
        return somme

    def Selection(self, taux = 0.3):
        self._itineraires_selectionnes = {}  
        self._itineraires_tries = self.Tri(self._liste_itineraire)
        """ i = 1
        for villes in self._itineraires_tries.values():            
            self._itineraires_selectionnes.append(villes)
            if i == (taux * self._nb_itineraires):
                break
            i += 1 """
        self._itineraires_selectionnes = dict(islice(self._itineraires_tries.items(), round(taux * self._nb_itineraires)))
        #print("Liste Séléctionnée: \n" + str(self._itineraires_selectionnes))

    def Crossover(self):
        self._liste_itineraire = []        
        for i in range(1,self._nb_itineraires):
            enfant = list()
            parent1 = list(self._itineraires_selectionnes.values())[random.randrange(len(self._itineraires_selectionnes))].copy()
            parent2 = list(self._itineraires_selectionnes.values())[random.randrange(len(self._itineraires_selectionnes))].copy()
            while parent2 == parent1:
                parent2 = list(self._itineraires_selectionnes.values())[random.randrange(len(self._itineraires_selectionnes))].copy()
            taille = round((len(parent1)/2))
            enfant = parent1[(taille - 2):(taille + 2)]
            enfant_temporaire = parent2.copy()

            for j in range(0,len(enfant)):
                enfant_temporaire.remove(enfant[j])

            taille = round((len(parent2)/2))        
            enfant_temporaire[taille:taille] = enfant
            enfant = enfant_temporaire.copy()
            #enfant.extend(villes_uniques)
            enfant = self.Mutation(enfant)
            self._liste_itineraire.append(enfant)

    def Mutation(self,enfant):
        a, b = random.randrange(len(enfant)), random.randrange(len(enfant))
        enfant[a], enfant[b] = enfant[b], enfant[a]
        return enfant

    def get_liste(self):
        return self._liste_itineraire