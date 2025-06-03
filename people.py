
import random
from virus import virusl
from illness import illnessl
import const
class Citizen:
    def __init__(self, name, friends,mygov,Stats):
        self.name = name
        self.friends = friends
        self.friendslist = []
        self.friendsmeetingtoday = []
        self.mygov = mygov
        self.Stats = Stats

        self.rvalue = 0
        self.infectedme = -1
        self.illnesslist= []
        self.viruslist = []







    def printme(self):
        realfriends = []
        for i in self.friendslist:
            realfriends.append(i.name)
        print(str(self.name)+" "+str(realfriends)+" who infectedme: "+str(self.infectedme))



    def friendmake(self, Persons,bubblelst):
        if self.name % self.friends == 0:
            #for i in range(self.friends-1):#of fiends -1
            #if person is evenly split
            for friendnum in range(self.name+1,self.name+self.friends):

                if friendnum < len(Persons):#make sure its less than the #of ppl
                    try:
                        self.friendslist.append(Persons[friendnum])#adding to the persons friends
                        Persons[friendnum].friendslist.append(self)
                    except:
                        print("EROROROROROROORORR")
            bubble1 = self.friendslist.copy()
            bubble1.append(self)
            bubblelst.append(bubble1)
        else:
            i = self.friendslist[0]#swapping friends so that anchor friendlist = everyone else
            for friend in i.friendslist:
                if friend.name != self.name:
                    self.friendslist.append(friend)









    def goodillness(self,friend,daynum,SIM):
        for i in friend.viruslist:
            if i not in self.viruslist and i.name != "bad virus":
                willinfect = random.uniform(0.0, 1.0)
                if willinfect <= i.contagiousness:
                    self.makeill(i,daynum)
                    if (SIM.badvirus in self.viruslist):#people would already be infected wiht bad and then get the rest
                        self.removeillness(SIM.badvirus)


    def makeill(self,virus,daynum):
        if(virus not in self.viruslist):
            self.viruslist.append(virus)
            ill = illnessl(virus,daynum)


            self.illnesslist.append(ill)

            if len(self.illnesslist) >=3 or len(self.viruslist) >=3 or len(self.illnesslist) !=len(self.viruslist):
                print("ERROR LIST DISCREPENCY")
    def cure(self,daynum,SIM):
        for sick in self.illnesslist:

            if(sick.canibecured(daynum)):

                self.removeillness(sick.viruss)
                if len(self.illnesslist) >=3 or len(self.viruslist) >=3 or len(self.illnesslist) !=len(self.viruslist):
                    print("ERROR LIST DISCREPENCY")
    def removeillness(self,virus):
        self.viruslist.remove(virus)
        for sick in self.illnesslist:
            if sick.viruss == virus:
                self.illnesslist.remove(sick)

    def allillness(self,friend,SIM,daynum):
        self.goodillness(friend,daynum,SIM)
        if SIM.badvirus in friend.viruslist and (SIM.fearofpvirus not in self.viruslist and SIM.fearofvvirus not in self.viruslist) and SIM.badvirus not in self.viruslist:
            willinfect = random.uniform(0.0, 1.0)
            if willinfect <= SIM.badvirus.contagiousness:
                self.makeill(SIM.badvirus,daynum)

    def findfriendsmeetingtoday(self):
        self.friendsmeetingtoday = []
        for friend in self.friendslist:
            chance = random.uniform(0.0,1.0)
            if chance <= .5:
                self.friendsmeetingtoday.append(friend)

    def infect(self,Sim,daynum):
        self.findfriendsmeetingtoday()
        for i in range(self.friends):
            chance = random.uniform(0.0, 1.0)

            if chance <= Sim.bubblescape  :#bubbkescape
                person = self.name

                while person == self.name:

                    person = random.randint(1, len(Sim.Population)-1)

                victm = Sim.Population[person]
                self.allillness(victm,Sim,daynum)

                victm.allillness(self,Sim,daynum)

                self.Stats.meetings +=1
                self.mygov.GDP +=1
        for i in self.friendsmeetingtoday:

            self.allillness(i, Sim,daynum)
            i.allillness(self, Sim,daynum)

        self.Stats.meetings += len(self.friendsmeetingtoday)
        if len(self.viruslist) == 0:#self infect
            chance = random.uniform(0,1.0)
            if chance <= const.SELFINFECT:
                self.makeill(Sim.badvirus,daynum)




# def meetfriends():
# def friendmake(i, pop):
#     return None
