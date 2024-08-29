def getMoneyLines():
    # moneylineOne = input("What is the first team and moneyline? Split with a space: ")
    moneylineOne = "gsw -140"
    # moneylineTwo = input("What is the second team and moneyline? Split with a space: ")
    moneylineTwo = "lal -120"

    moneylineOne = moneylineOne.split(" ")
    moneylineOneTeam = moneylineOne[0]
    moneylineOneOdds = moneylineOne[1]
    print(moneylineOneTeam + " has a moneyline of " + moneylineOneOdds)


    moneylineTwo = moneylineTwo.split(" ")
    moneylineTwoTeam = moneylineTwo[0]
    moneylineTwoOdds = moneylineTwo[1]
    print(moneylineTwoTeam + " has a moneyline of " + moneylineTwoOdds)

    return moneylineOneTeam, moneylineOneOdds, moneylineTwoTeam, moneylineTwoOdds


def calculateMoneyLineProfit(m1t, m1o, m2t, m2o):
    teamAndBet = input("What is your bet on which team? Seperate with space, (ex: 100 buf) ")
    team = teamAndBet[teamAndBet.index(" ") + 1: ]
    bet = teamAndBet[:teamAndBet.index(" ")]
    profit = 0

    print(type(m1o), type(m2o))
    print(m1o, m2o)


    if (team == (m1t)):
        if (m1o[:1] == "+"): #If moneyline is underdog
            profit = float(float(bet)/100.0) * (float(m1o[1:])) - float(bet) #Calculate profit
        else: #If moneyline is favorite
            profit = (float(100/int(m1o[1:])) * float(bet)) #Calculate profit
        team = m1t

    elif (team == (m2t)): 
        if (m2o[:1] == "+"): #If moneyline is underdog
            profit = float(float(bet)/100.0) * (float(m2o[1:])) - float(bet) #Calculate profit
        else: #If moneyline is favorite
            profit = (float(100/int(m2o[1:])) * float(bet)) #Calculate profit
        team = m2t
    else:
        print("bad")

    print("Betting $" + str(bet) + " on " + team + "'s moneyline of " + str(m1o) + " equals $" + str(round(profit, 2)) + " profit.") #Print profit


calculateMoneyLineProfit(*getMoneyLines())


