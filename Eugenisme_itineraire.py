from Eugenisme import Eugenisme
from individu_itineraire import IndividuItineraire
from random import sample
import random
import math

class EugenismeItineraire():
    
    def __init__(self, nb_population = 50):
        self._liste_ville = []
        self._liste_itineraire = []
        self._itineraires_tries = {}
        self._itineraires_selectionnes = []
        self._nb_itineraires = nb_population
        ind = IndividuItineraire(20)
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
        self._itineraires_selectionnes = []  
        self._itineraires_tries = self.Tri(self._liste_itineraire)
        i = 1
        for villes in self._itineraires_tries.values():            
            self._itineraires_selectionnes.append(villes)
            if i == (taux * self._nb_itineraires):
                break
            i += 1

    def Crossover(self):
        self._liste_itineraire = []        
        for i in range(1,self._nb_itineraires):
            enfant = list()
            parent1 = self._itineraires_selectionnes[random.randrange(len(self._itineraires_selectionnes))]
            parent2 = self._itineraires_selectionnes[random.randrange(len(self._itineraires_selectionnes))]
            while parent2 == parent1:
                parent2 = self._itineraires_selectionnes[random.randrange(len(self._itineraires_selectionnes))]
            enfant = parent1[round((len(parent1)/2)) - 2:(round(len(parent1)/2)) + 3]
            enfant_temporaire = parent2

            for j in range(0,len(enfant)):
                enfant_temporaire.remove(enfant[j])
                    
            enfant_temporaire[round(len(enfant_temporaire)/2):round(len(enfant_temporaire)/2)] = enfant
            enfant = enfant_temporaire
            #enfant.extend(villes_uniques)
            enfant = self.Mutation(enfant)
            if enfant not in self._liste_itineraire:
                self._liste_itineraire.append(enfant)
            else:
                i -= 1

    def Mutation(self,enfant):
        a, b = random.randrange(len(enfant)), random.randrange(len(enfant))
        enfant[a], enfant[b] = enfant[b], enfant[a]
        return enfant

    def get_liste(self):
        return self._liste_itineraire