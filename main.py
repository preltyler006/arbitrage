import os
from arbitrageCalculator import *
from jsonReaderV2 import line_and_team
from apiGet import *
import time

start_time = time.perf_counter()


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
print("\n")


# line_and_team is the main function that takes in the data from apiCallData.txt 
# prints a message for the user based on the bet they want, which is the one argument
# needed to be inputted as an integer
print(line_and_team(100))
end_time = time.perf_counter()

elapsed_time = end_time - start_time

print("\n\n\nElapsed Time: " + str(elapsed_time) + " seconds\n\n\n")