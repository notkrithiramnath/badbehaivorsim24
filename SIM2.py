import random

import const
from virus import virusl

class basesim:
    def __init__(self, pop, gov, Stats, escapeprobability,bubbleescape,debug):
        self.Population = pop
        self.gov = gov
        self.badvirus = virusl("bad virus",const.BSYMP,const.BCONT)
        self.fearofpvirus = virusl("fear of punishment virus",const.PSYMP,const.PCONT)
        self.fearofvvirus = virusl("fear of verification",const.VSYMP,const.VCONT)
        self.Stats = Stats
        self.escape = escapeprobability
        self.bubbles = []
        self.clnbubbles = []
        self.numsickpeople = 0
        self.bubblescape = bubbleescape
        self.peak = -5
        self.peakday = -5
        self.debug = debug
        self.lastday = 365
        self.string =""
    def printeveryone(self):
        for i in self.Population:
            #print(str(i.name)+" "+str(i.infected))
            i.printme()
            #print(i.friendslist)

            for virus in i.viruslist:
                print("VIRUSLIST "+virus.name)

            for ill in i.illnesslist:
                print("illnesslist "+ill.viruss.name)

    def calcpeak(self,daynum):
        temp = self.Stats.infections
        if temp > self.peak:
            self.peak = temp
            self.peakday = daynum
    def startsim(self):
        for i in self.Population:
            i.friendmake(self.Population,self.bubbles)

        self.makesick()

    def printday(self,day):
        if not self.debug:
            if day == 0:
                 print("day\tmeetings\tinfections\tGDP\tlockdown?\tDeaths\tPopulation\tcleanbubble")
            #print(str(day) + "\t "+ str(self.Stats.meetings) + "\t" + str(self.Stats.infections) +"\t" + str(self.gov.GDP)+"\t"+str(self.gov.lockdown)+"\t"+str(self.Stats.deaths)+"\t"+(str(len(self.Population)))+"\t"+str(len(self.clnbubbles)))




    def kill(self,person):
        if person.dayssick ==person.daydying: #FIX MAKE SURE THAT WE SEE IF THEYLL DIE OR NOT THEN CHOOSE A RANDOM DAY
             person.infected = False
             person.caninfect = False
             person.cangetsick = False
             self.Population.remove(person)
             self.Stats.deaths +=1



    # def cleanbubbles(self):
    #
    #     self.clnbubbles = []
    #     for i in self.bubbles:
    #         clean = 0
    #         for person in i:
    #             if len(person.viruslist) == 0:
    #                 clean+=1
    #         if clean == len(i):
    #             self.clnbubbles.append(i)






class randomsim1(basesim):
    def makesick(self):


        for i in self.Population:
            if random.uniform(0.0, 1.00) <= self.gov.badinitialinf:#if the number is less than the initial infection point
                i.infectedme = -5
                i.makeill(self.badvirus,0)

    def runaday(self, daynum):
        self.Stats.bstats = 0
        self.Stats.vstats = 0
        self.Stats.pstats = 0
        self.gov.GDP = 0
        self.gov.rep = 0
        self.gov.randaudit(self,daynum)
        self.calcpeak(daynum)
        for i in self.Population:

            i.infect(self,daynum)
        for i in self.Population:
            i.cure(daynum,self)
        for person in self.Population:#today
            if self.fearofpvirus in person.viruslist:
                self.Stats.pstats +=1
            if self.fearofvvirus in person.viruslist:
                self.Stats.vstats +=1
            if self.badvirus in person.viruslist:
                self.Stats.bstats +=1
        self.gov.calcGDP(self.Population,self.Stats)
        self.Stats.calcpeak(daynum)
        if const.DEBUG:
            print("day  "+str(daynum))
            self.printeveryone()
            self.printday(daynum)
            print((" NUMBER OF BADS: "+str(self.Stats.bstats)))
            print((" NUMBER OF FEAR OF PUNISHES: " + str(self.Stats.pstats)))
            print((" NUMBER OF FEAR OF VERIFIES: " + str(self.Stats.vstats)))
        else:
            self.Stats.printstats(daynum,self.gov)
        self.Stats.calcavg(daynum,self.gov)
        if daynum == 364:
            self.string = ("\tfear of verification avg\t"+str(self.Stats.vavg))
            self.string+=(
                "\tf verification PEAK VAL\t" + str(self.Stats.vpeakval) + "\tf verification PEAK DAY\t" + str(self.Stats.vpeakday))
            self.string+=("\tfear of punishment avg\t" + str(self.Stats.pavg))
            self.string+=(
                "\tf punishment PEAK VAL\t" + str(self.Stats.ppeakval) + "\tf punishment PEAK DAY\t" + str(self.Stats.ppeakday))
            self.string+=("\tbad virus avg\t" + str(self.Stats.bavg))
            self.string+=("\tbad virus PEAK VAL\t" + str(self.Stats.bpeakval)+ "\tbad virus PEAK DAY\t"+str(self.Stats.bpeakday))
            self.string+=("\tGDP avg\t" + str(self.Stats.gdpavg))
            self.string+=("\tREP avg\t" + str(self.Stats.repavg))

            self.string += const.printconstants()
            print(self.string)






class detsim(basesim):


    def runaday(self, daynum, Stats):
        Stats.calcinfectedtoday(self.Population,self.gov)
        self.gov.lockdowntoday(Stats)
        for i in self.Population:
            i.cure()
            i.daysick()
        if not self.gov.lockdown:
            for i in self.Population:
                i.infect()
                Stats.meetings += len(i.friendsmeetingtoday)
        else:
            num = random.randint(1,self.escape)
            if num == 1:
                i.infect()
        print("running day " + str(daynum) + " with " + str(Stats.meetings) + " meetings " + " infections: "+str(Stats.infections)+" "+"GDP loss: "+str(self.gov.GDP)+" "+str(self.gov.lockdown))



