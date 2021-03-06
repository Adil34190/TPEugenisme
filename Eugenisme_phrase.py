from Individu_phrase import IndividuPhrase
from Eugenisme import Eugenisme
import random
import string

class EugenismePhrase(Eugenisme):

    def __init__(self, nb_individu = 100, taille_individu = 12):
        self.population = []
        self.tri_individu = {}
        self.selection = []
        self.nb_individu = nb_individu
        for i in range(self.nb_individu):
            ind = IndividuPhrase(taille_individu)
            self.population.append(ind.get_Individu())
        
    
    @staticmethod
    def Fitness(str, cible = "Sans Rigoler"):        
        count = 0
        i = 0
        for letter in str:
            if cible[i] == letter:
                count += 1
            i += 1
        return (count/len(cible))

    def Tri(self,cible,population):
        triIndiv = {}
        for str in population:
            fitness = self.Fitness(str, cible)
            triIndiv[str] = fitness
        triIndiv = list(sorted(triIndiv.items(), key=lambda x: x[1], reverse=True))
        return triIndiv


    def Selection(self, cible, taux = 0.3):
        self.selection = []
        self.tri_individu = self.Tri(cible,self.population)
        i = 1
        for items in self.tri_individu:            
            self.selection.append(items[0])
            if i == (taux * self.nb_individu):
                break
            i += 1
    
    def Crossover(self):
        self.population = []
        for i in range(1,self.nb_individu):
            taille = 0
            parent1 = self.selection[random.randrange(len(self.selection))]
            parent2 = self.selection[random.randrange(len(self.selection))]
            while parent2 == parent1:
                parent2 = self.selection[random.randrange(len(self.selection))]
            taille = random.randrange(len(parent1))
            enfant = parent1[0:taille] + parent2[taille:]
            enfant = self.Mutation(enfant)
            self.population.append(enfant)
        
            
    def Mutation(self,enfant):
        index = random.randrange(len(enfant))
        lettre = random.choice(string.ascii_letters + ' é' +"'")
        enfant = list(enfant)
        enfant[index] = lettre
        enfant = "".join(enfant)
        return enfant
    
    def get_population(self):
        return self.population

    def get_individuTries(self):
        return self.tri_individu
