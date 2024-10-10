import os
from arbitrageCalculator import *
from jsonReaderV2 import line_and_team
from apiGet import *


# Clear screen
try:
    os.system("clear")
except:
    os.system("cls")



# This function calls the API to get the data to a text file
try:
    writeToDataFile('./apiCallData.txt')
except:
    print("API error")


# line_and_team is the main function that takes in the data from apiCallData.txt 
# prints a message for the user based on the bet they want, which is the one argument
# needed to be inputted as an integer
print(line_and_team(100))