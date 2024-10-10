import ast
from arbitrageCalculator import arbitrageBetCalculator

'''
To preserve the api requests/calls, we transfer data from one point in time to a text file,
and move data over to a variable here to easily manipulate and gain information from it
'''

def text_file_to_list(text_file):

    '''
    This function takes data from apiCallData.txt and makes it into a python list

    Args:
        text_file: filepath of text file

    Returns:
        A python list of all the data in the text file
    '''
    data_list = []

    with open (text_file, 'r') as file:
        #Reads text file into a list of lines
        for line in file:
            if line.strip(): # checking string is not empty space
                data_list.append(ast.literal_eval(line.strip())) # as.literal_eval converts string of python code to actual python code

    return data_list



def line_and_team(BET):

    '''
    This function takes in the data from our text file, and by calling other functions from other files created,
    uses an algorithm to search for the best possible profit across all sports games happening, if possible

    Args:
        BET: Bet size wanted for 1st line, is not total amount of money needed to make profit
    
    Returns:
        DOES NOT RETURN A VALUE
        Prints a string containing information to the user how much to bet on which line.

    '''


    list_data = text_file_to_list('./apiCallData.txt')
    allProfits = ""
    for sport_game in list_data: # for every dictionary in list_data, so every sport game happening
        
        currentBestProfit = 0
        key = sport_game["sport_key"]
        bestProfitPerGame = "" 
        #setting global variables for returned print statement

        listOfSports = ("americanfootball_nfl", "americanfootball_ncaaf", "baseball_mlb", "icehockey_nhl", "basketball_nba_preseason")

        if key in listOfSports: # we only want american sports, so filter for these
            bookmakers = sport_game["bookmakers"]

            for bookmaker in bookmakers: # for every bookmaker
                
                bestMatchup1 = {"bookmaker": "", "name": "", "line": ""}
                bestMatchup2 = {"bookmaker": "", "name": "", "line": ""}
                #setting global variables for accessibility reasons 

                
                bookmaker1 = bookmaker["title"]
                team1 = bookmaker["markets"][0]["outcomes"][0]["name"]
                line1 = bookmaker["markets"][0]["outcomes"][0]["price"]

                if (line1 > 0): # if odds are underdog, ex +240
                        
                    line1 = "+" + str(line1) 
                        # add + in front of int and change type to str
                        # to make input work with arbitrageBetCalculator() function
                else:
                    line1 = str(line1) 
                        #can leave line1 unchanged as a string as we don't need to add a negative sign
                        #in front like + sign because line is negative already


                for bm in bookmakers: # Looping through every other bookmaker's set of lines to compare against line1 made above
                    bookmaker2 = bm["title"]
                    team2 = bm["markets"][0]["outcomes"][1]["name"]
                    line2 = bm["markets"][0]["outcomes"][1]["price"]

                    if (line2 > 0): # if odds are underdog, ex +240
                        
                        line2 = "+" + str(line2) 
                            # add + in front of int and change type to str
                            # to make input work with arbitrageBetCalculator() function
                    else:
                        line2 = str(line2)


                    arbitrage = arbitrageBetCalculator(BET, line1, line2) # calling arbitrageBetCalculator with values obtained from text file

                    if (arbitrage[0] == False): #If arbitrage returns only boolean, meaning false
                        pass
                    else:
                        pass
                        arbitrageProfit = arbitrage[0] # First return value is the profit

                        if (arbitrageProfit > currentBestProfit): # Checking if current profit value is better than last best
                            currentBestProfit = arbitrageProfit # Keeps track of best profit for particular game

                            bestMatchup1["bookmaker"] = bookmaker1
                            bestMatchup1["name"] = team1
                            bestMatchup1["line"] = line1
                                #so the user knows what to bet on which line

                            bestMatchup2["bookmaker"] = bookmaker2
                            bestMatchup2["name"] = team2
                            bestMatchup2["line"] = line2

                            bestProfitPerGame = "------------------------------------------------------------------------------\n"
                            bestProfitPerGame += bestMatchup1["bookmaker"] + ", " + bestMatchup1["name"] + ", " + bestMatchup1["line"] + ".\n"
                            bestProfitPerGame += bestMatchup2["bookmaker"] + ", " + bestMatchup2["name"] + ", " + bestMatchup2["line"] + ".\n"
                            bestProfitPerGame += str(arbitrage[1])
                            # ^^ saving current best profit print statement to variable defined above for global accesibility reasons
                    
        allProfits += bestProfitPerGame

    return(allProfits)
