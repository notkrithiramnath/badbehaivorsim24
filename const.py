
#INDEPENDENT VARIABLES
#SIMULATION VARIABLES0
POPULATIONNUM = 1000
INITIALINFECTIONS = .3#probability someone will be initially infected
NUMBEROFDAYS =365 #number of days the simulation is run
DEBUG = False
#GOV VARIABKES
AUDITCATCH = .3
AUDITPROB = 0.0038
GDPDECREASEPUNISH = 480


#universal/country constants
NUMBEROFFRIENDS = 11 #italy - 7 #US - 11 #DK - 9
BUBBLESCAPE = 0.01#chance somoene will escape bubble 0.01 default
SELFINFECT = .4
BCONT = .4
PCONT = .1 #gdpdecrase/1000
PSYMP = 25#gdpdec/4
VCONT = .05;

#symtoms lenght

VSYMP = 10
BSYMP = 10000




#virus pramaters
#def __init__(self, name,symptoms, contagiousness):
#contagiosuness





def printconstants():
    mystr = ("\tP contagiousness\t"+str(PCONT))
    mystr += ("\tV contagoousness\t" + str(VCONT))
    mystr+= ("\tB contagiousness \t" + str(BCONT))
    mystr+= ("\tP  symptom length\t" + str(PSYMP))
    mystr+= ("\tV  symptom length\t" + str(VSYMP))
    mystr +=("\tB  symptom length\t" + str(BSYMP))
    mystr += ("\tAUDIT PROB\t" + str(AUDITPROB))
    mystr += ("\tGDP DECREASE PUNISHED\t" + str(GDPDECREASEPUNISH))
    mystr += ("\tSELF INFECT\t" + str(SELFINFECT))
    mystr += ("\tNUMBER OF FRIENDS\t" + str(NUMBEROFFRIENDS))
    return(mystr)