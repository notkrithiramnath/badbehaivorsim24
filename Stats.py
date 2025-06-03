class Statsl:
    def __init__(self,meetings,infections,rvalue):
        #self.totalmeet =
        self.infections = infections
        self.meetings = meetings
        self.rvalue = rvalue
        self.peoplesick = 0
        self.deaths = 0
        self.totalr = 0
        self.realr = 0
        self.pstats= 0
        self.vstats = 0
        self.bstats = 0
        self.bavg = 0
        self.vavg = 0
        self.pavg = 0
        self.gdpavg = 0
        self.repavg = 0
        self.sum = 0.0
        self.bpeakday = 0
        self.bpeakval = 0
        self.vpeakday = 0
        self.vpeakval = 0
        self.ppeakday = 0
        self.ppeakval = 0



    # def calcinfectedtoday(self,population,gov):
    #     self.infections = 0
    #     for i in population:
    #         if i.infected == True:
    #             self.infections += 1

    def calcrvalue(self,bubblelist):

        for bubble in bubblelist:
            for person in bubble:
                self.totalr +=person.rvalue
        self.realr = self.totalr/(len(bubblelist)*len(bubblelist[1]))
    def printstats(self,daynum,gov):
        if daynum == 0:
            print("DAY:  BADVIRUS TODAY   FPVIRUS TODAY  FVVIRUS TODAY  GDP   REPUTATION")
            print(
                str(daynum) + "               " + str(self.bstats) + "             " + str(
                    self.pstats) + "             " + str(self.vstats) + "          " + str(
                    gov.GDP) + "         " + str(gov.rep))
        else:
            print(
                str(daynum) + "               " + str(self.bstats) + "             " + str(self.pstats) + "             " + str(self.vstats) + "          " + str(
                    gov.GDP) + "         " + str(gov.rep))
    def calcavg(self,daynum,gov):
        if daynum >=265:
            self.vavg += self.vstats
            self.pavg += self.pstats
            self.bavg += self.bstats
            self.gdpavg += gov.GDP
            self.repavg += gov.rep
        if daynum == 364:
            self.vavg = self.vavg/100
            self.bavg = self.bavg / 100
            self.pavg = self.pavg / 100
            self.repavg = self.repavg/100
            self.gdpavg = self.gdpavg/100
    def calcpeak(self,day):
        if self.vstats > self.vpeakval:
            self.vpeakval = self.vstats
            self.vpeakday = day
        if self.pstats > self.ppeakval:
            self.ppeakval = self.pstats
            self.ppeakday = day
        if self.bstats > self.bpeakval:
            self.bpeakval = self.bstats
            self.bpeakday = day