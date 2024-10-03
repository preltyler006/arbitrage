import json
import ast

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
        secondary_dict = dictionary["bookmakers"] # create a secondary dictionary from that original dictionary
        # print(secondary_dict)
        j = 0

        for d in secondary_dict: # for every dictionary in secondary dict
            # print(d["markets"])
            tertiary_dict = d["markets"]


            for l in tertiary_dict:
                # print(l["outcomes"])
                bookmaker_name = secondary_dict[j]["title"]
                print("Bookmaker name: " + bookmaker_name)
                j+=1
                for i in range(2):
                    print(l["outcomes"][i])
                print("\n")
                # print(l["outcomes"][0])


        # tertiary_dict = secondary_dict["markets"][0]
        # name_and_odds1 = tertiary_dict["outcomes"][0]
        # name_and_odds2 = tertiary_dict["outcomes"][1]
        # bookmaker = secondary_dict["title"]
        # print("In " + bookmaker + "'s book: \n")
        
        # print(name_and_odds1)
        # print(name_and_odds2)
        # print(i)
        # i+=1


line_and_team()