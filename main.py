import os
from arbitrageCalculator import *
from jsonReader import line_and_team

try:
    os.system("clear")
except:
    os.system("cls")

#Run arbitrageBetCalculator function:
    #1st argument is bet size for 1st line, integer
    #2nd argument is 1st line, string with + or - in front
    #3rd argument is 2nd line, string with + or - in front
# arbitrageBetCalculator(100, "+240", "-305")
# arbitrageBetCalculator(100, "-165", "+240")
# arbitrageBetCalculator(100, "+100", "-120")

line_and_team()