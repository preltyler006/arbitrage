import os
from arbitrageCalculator import *

try:
    os.system("clear")
except:
    os.system("cls")

#Run arbitrageBetCalculator function:
    #1st argument is bet size for 1st line, integer
    #2nd argument is 1st line, string with + or - in front
    #3rd argument is 2nd line, string with + or - in front
arbitrageBetCalculator(100, "-285", "+320")
# arbitrageBetCalculator(100, "-130", "+110")
# arbitrageBetCalculator(100, "+100", "-120")