from virus import virusl
import random
class illnessl:
    def __init__(self,viruss,daynum):
        self.viruss = viruss
        self.dayssincesick = 0
        self.symptomslen = random.uniform(0, self.viruss.maxsymptoms)
        self.dayigotsick = daynum
        self.immunitydays = 0
        self.dayssick = 0
        self.daycured = -5
        self.daydying = -5


    def amisick(self,sickness):
        if self.viruss == sickness:
            return True
        else:
            return False

    def canibecured(self, daynum):
        if daynum - self.dayigotsick >= self.symptomslen:
            return True
