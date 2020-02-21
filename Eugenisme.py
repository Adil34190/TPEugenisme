from abc import ABC, abstractmethod

class Eugenisme(ABC):

    @abstractmethod
    def Crossover(self):
        pass
    
    @abstractmethod
    def Selection(self, taux = 0.3):
        pass
    
    @abstractmethod
    def Mutation(self, enfant):
        pass
    
    @abstractmethod
    def Tri(self, population):
        pass
