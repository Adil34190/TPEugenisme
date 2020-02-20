import random
import string

class IndividuPhrase:

    def __init__(self,taillePhrase = 14):
        self.taillePhrase = taillePhrase
        self.genes = ''.join([random.choice(string.ascii_letters + ' é' + "'") for n in range(self.taillePhrase)])#generation de mots
    
    def get_Individu(self):
        return self.genes
