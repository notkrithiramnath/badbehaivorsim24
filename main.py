

import random as random
import Simulation
from gov import govl
import people
from virus import virusl
import Stats
import SIM2
import const




#Independent variables
# Name = USA, Population = 100, Initial infected 20, GDP = 0
resultlist =[]



seedlist = [20,200,500,22]

#print(realsim.bubbles)
random.seed(22)#making all results always the same


def run():

    stats2 = Stats.Statsl(0, 0, 0)
    US = govl("USA", const.POPULATIONNUM, const.INITIALINFECTIONS, stats2)
    USsim = SIM2.randomsim1(US.poplist, US, stats2, 0, const.BUBBLESCAPE, const.DEBUG)
    US.makepeople()
    USsim.startsim()

    for i in range(const.NUMBEROFDAYS):
        USsim.runaday(i)
    resultlist.append(USsim.string)
#stats2.calcrvalue(USsim.bubbles)
#print(str(USsim.gov.GDP) +"\t\t" + str(realsim.Stats.deaths)+"\t"+str(stats2.realr)+"\t"+str(realsim.peakday)+"\t"+str(realsim.peak)+"\t"+str(realsim.lastday))
#USsim.prints()
list2 = ["E","F","G","H","I","J","K","L","M","N","O"]
list3 = ["D"]
for letter in list2:
    if letter == "A":
        const.GDPDECREASEPUNISH = 400  # ITALYBASE BASE
        const.AUDITPROB = .07
        const.NUMBEROFFRIENDS = 7  # italy - 7 #US - 11 #DK - 9
        const.SELFINFECT = .52
        const.BCONT = const.SELFINFECT
        const.PCONT = (1.0 - const.SELFINFECT) * .05
        const.VCONT = const.PCONT;
        run();

    elif letter == "B":
        const.GDPDECREASEPUNISH = 480  # US BASE
        const.AUDITPROB = .0038
        const.NUMBEROFFRIENDS = 11  # italy - 7 #US - 11 #DK - 9
        const.SELFINFECT = .45
        const.BCONT = const.SELFINFECT
        const.PCONT = (1.0 - const.SELFINFECT) * .05  # gdpdecrase/1000
        const.VCONT = const.PCONT;
        run();
    elif letter == "C":
        const.GDPDECREASEPUNISH = 600  # DK BASE
        const.AUDITPROB = .042
        const.NUMBEROFFRIENDS = 9  # italy - 7 #US - 11 #DK - 9
        const.SELFINFECT = .12
        const.BCONT = const.SELFINFECT
        const.PCONT = (1.0 - const.SELFINFECT) * .05
        const.VCONT = const.PCONT;
        run();
    elif letter == "D":#extra studies base
        const.GDPDECREASEPUNISH = 400  *4 #ITALYBASE BASE
        const.AUDITPROB = .07
        const.NUMBEROFFRIENDS = 7  # italy - 7 #US - 11 #DK - 9
        const.SELFINFECT = .52
        const.BCONT = const.SELFINFECT
        const.PCONT = ((1.0 - const.SELFINFECT) * .05)*4
        const.VCONT = const.PCONT;
        run();
    elif letter == "E":
        const.GDPDECREASEPUNISH = 400*.05 # ITALYBASE BASE
        const.AUDITPROB = .00001
        const.NUMBEROFFRIENDS = 7  # italy - 7 #US - 11 #DK - 9
        const.SELFINFECT = .52
        const.BCONT = const.SELFINFECT
        const.PCONT = ((1.0 - const.SELFINFECT) * .05) * .05
        const.VCONT = const.PCONT;
        run();
    elif letter == "F":
        const.GDPDECREASEPUNISH = 400*.05  # ITALYBASE BASE
        const.AUDITPROB = .0001
        const.NUMBEROFFRIENDS = 7  # italy - 7 #US - 11 #DK - 9
        const.SELFINFECT = .52
        const.BCONT = const.SELFINFECT
        const.PCONT = ((1.0 - const.SELFINFECT) * .05) * .05
        const.VCONT = const.PCONT;
        run();
    elif letter == "G":
        const.GDPDECREASEPUNISH = 400*.05  # ITALYBASE BASE
        const.AUDITPROB = .00025
        const.NUMBEROFFRIENDS = 7  # italy - 7 #US - 11 #DK - 9
        const.SELFINFECT = .52
        const.BCONT = const.SELFINFECT
        const.PCONT = ((1.0 - const.SELFINFECT) * .05) * .05
        const.VCONT = const.PCONT;
        run();
    elif letter == "H":
        const.GDPDECREASEPUNISH = 400*.05  # ITALYBASE BASE
        const.AUDITPROB = .0004
        const.NUMBEROFFRIENDS = 7  # italy - 7 #US - 11 #DK - 9
        const.SELFINFECT = .52
        const.BCONT = const.SELFINFECT
        const.PCONT = ((1.0 - const.SELFINFECT) * .05) * .05
        const.VCONT = const.PCONT;
        run();
    elif letter == "I":
        const.GDPDECREASEPUNISH = 400*.05  # ITALYBASE BASE
        const.AUDITPROB = .0007
        const.NUMBEROFFRIENDS = 7  # italy - 7 #US - 11 #DK - 9
        const.SELFINFECT = .52
        const.BCONT = const.SELFINFECT
        const.PCONT = ((1.0 - const.SELFINFECT) * .05) * .05
        const.VCONT = const.PCONT;
        run();
    elif letter == "J":
        const.GDPDECREASEPUNISH = 400*.05 # ITALYBASE BASE
        const.AUDITPROB = .001
        const.NUMBEROFFRIENDS = 7  # italy - 7 #US - 11 #DK - 9
        const.SELFINFECT = .52
        const.BCONT = const.SELFINFECT
        const.PCONT = ((1.0 - const.SELFINFECT) * .05) * .05
        const.VCONT = const.PCONT;
        run();
    elif letter == "K":
        const.GDPDECREASEPUNISH = 400*.05  # ITALYBASE BASE
        const.AUDITPROB = .05
        const.NUMBEROFFRIENDS = 7  # italy - 7 #US - 11 #DK - 9
        const.SELFINFECT = .52
        const.BCONT = const.SELFINFECT
        const.PCONT = ((1.0 - const.SELFINFECT) * .05) * .05
        const.VCONT = const.PCONT;
        run();
    elif letter == "L":
        const.GDPDECREASEPUNISH = 400*.05  # ITALYBASE BASE
        const.AUDITPROB = .1
        const.NUMBEROFFRIENDS = 7  # italy - 7 #US - 11 #DK - 9
        const.SELFINFECT = .52
        const.BCONT = const.SELFINFECT
        const.PCONT = ((1.0 - const.SELFINFECT) * .05) * .05
        const.VCONT = const.PCONT;
        run();

    elif letter == "N":
        const.GDPDECREASEPUNISH = 400*.05 # ITALYBASE BASE
        const.AUDITPROB = .15
        const.NUMBEROFFRIENDS = 7  # italy - 7 #US - 11 #DK - 9
        const.SELFINFECT = .52
        const.BCONT = const.SELFINFECT
        const.PCONT = ((1.0 - const.SELFINFECT) * .05) * .05
        const.VCONT = const.PCONT;
        run();
    elif letter == "O":
        const.GDPDECREASEPUNISH = 400 * .05  # ITALYBASE BASE
        const.AUDITPROB = .07
        const.NUMBEROFFRIENDS = 7  # italy - 7 #US - 11 #DK - 9
        const.SELFINFECT = .52
        const.BCONT = const.SELFINFECT
        const.PCONT = ((1.0 - const.SELFINFECT) * .05) * .05
        const.VCONT = const.PCONT;
        run();

for item in resultlist:
    print(item)