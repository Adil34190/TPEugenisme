import random
import string

class IndividuPhrase:

    def __init__(self,taillePhrase = 14):
        self.taillePhrase = taillePhrase
        self.genes = ''.join([random.choice(string.ascii_letters + ' ') for n in range(self.taillePhrase)])#generation de mots
    
    def AfficherIndividu(self):
        return self.genes
