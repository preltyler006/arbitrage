import json
import ast
from arbitrageCalculator import arbitrageBetCalculator

'''
To preserve the api requests/calls, we transfer data from one point in time to a text file,
and move data over to a variable here to easily manipulate and gain information from it
'''
def text_file_to_list(text_file):
    data_list = []

    with open (text_file, 'r') as file:
        #Reads text file into a list of lines
        for line in file:
            if line.strip():
                data_list.append(ast.literal_eval(line.strip()))

    return data_list


def line_and_team():


    list_data = text_file_to_list('./data.txt')
    for dictionary in list_data: # for every dictionary in list_data
        key = dictionary["sport_key"]
        if (key == "americanfootball_nfl" or key == "americanfootball_ncaaf"): # we only want american sports
            secondary_dict = dictionary["bookmakers"] # create a secondary dictionary from that original dictionary to go deeper
            j = 0

            for dict in secondary_dict: # for every dictionary in secondary dict
                tertiary_dict = dict["markets"] # create a third market from the secondary dictionary to go even deeper


                for d in tertiary_dict: # for every dictionary in third dict
                    bookmaker_name = secondary_dict[j]["title"] 
                    # print("Bookmaker name: " + bookmaker_name)
                    j+=1 # increment to the next bookmaker


                    line1 = d["outcomes"][0] # get line1 team and price
                    line1_price = line1["price"] # get just price of line1
                    if (line1_price > 0): # if odds are underdog, ex +240
                        
                        line1_price = "+" + str(line1_price) 
                        # add + in front of int and change type to str
                        # to make input work with arbitrageBetCalculator() function
                    else:
                        line1_price = str(line1_price)


                    line2 = d["outcomes"][1] # get line2
                    line2_price = line2["price"]
                    if (line2_price > 0):

                        line2_price = "+" + str(line2_price)
                    else:
                        line2_price = str(line2_price)


                    # Call arbitrageCalculator.py to see if arbitrage is possible

                    if(arbitrageBetCalculator(100, line1_price, line2_price) == False): # If Arbitrage not possible
                        print("Arbitrage Not Possible For: \n")
                        print(line1)
                        print(line2)
                        pass
                    else: # If Arbitrage Possible
                        pass


                    # print("\n")




# line_and_team()