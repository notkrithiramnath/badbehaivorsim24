import people
import const
import random
import SIM2
class govl:

    def __init__(self, name, populationnum,badinitialinf,Stats):
        self.name = name

        self.populationnum = populationnum
        self.badinitialinf = badinitialinf
        self.GDP = 0

        self.poplist = []

        self.rep = 0

        self.Stats = Stats
        #self.populationlist = []
        self.GDPday = 0

    def calcGDP(self,population,Stats):

        for i in population:

            self.GDP+=1
        self.GDP -= Stats.bstats
    def makepeople(self):
        for i in range(self.populationnum):
            person = people.Citizen(i,const.NUMBEROFFRIENDS,self,self.Stats)
            self.poplist.append(person)
    def randaudit(self,simulation,daynum):

        for person in (self.poplist):

            if random.uniform(0.0, 1.00) <= const.AUDITPROB:
                if(simulation.badvirus in person.viruslist):
                    if(random.uniform(0.0, 1.00) <= const.AUDITCATCH):
                        self.GDP-=const.GDPDECREASEPUNISH
                        self.rep+=1
                        person.infectedme = -40

                        person.removeillness(simulation.badvirus)

                        person.makeill(simulation.fearofpvirus, daynum)
                else:
                    self.GDP -=1
                    self.rep -=1

                    person.makeill(simulation.fearofvvirus,daynum)






#
#     def whoami(self):
#         print("I AM AMERICA")
#
# class wakanda(gov):
#     def __init__(self,name,lockdown,mask,population,initialinf,GDP):
#         super(USAgov, self).__init__(name, population, initialinf,GDP)

