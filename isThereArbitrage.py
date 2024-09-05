def getMoneyLines():
    '''
    Originally used for calculateMoneyLineProfitV1, not needed anymore as V2 works much better
    '''
    # moneylineOne = input("What is the first team and moneyline? Split with a space: ")
    moneylineOne = "gsw +140"
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






def calculateMoneyLineProfitV2(mt, mo, bet):
    '''
    Function returns profit based on money line and bet
    mt ex: buf
    mo ex: +120
    bet ex: 100
    '''
    team = str(mt)
    moneyLine = str(mo)
    bet = int(bet)
    profit = 0

    if (mo[:1] == "+"): #If moneyline is underdog, +
        profit = float(float(bet)/100.0) * (float(mo[1:]))
    else: #If moneyline is favorite, -
        profit = (float(100/int(mo[1:])) * float(bet))
    
    print("Betting $" + str(bet) + " on " + team + "'s moneyline of " + moneyLine + " equals $" + str(round(profit, 2)) + " profit.") #Print profit
    return profit



def reverseProfitCalculator(profit, line):
    '''
    returns bet needed to equal underdog bet given line and profit from favorite bet
    '''
    if(line[:1] == "+"):
        return 100*(float(profit)/float(line[1:]))
    
    elif(line[:1] == "-"):
        return (float(profit)*float(line[1:]))/100
    

def reversePayoutCalculator(profit, line, bet):
    if(line[:1] == "-"):
        return ((float(profit) + bet))/((100/float(line[1:]))+1)







def calculateMoneyLineProfitV1(m1t, m1o, m2t, m2o): 
    '''
    Function returns profit on 4 parameters
    Too many if/else statements, cluttered code, discarded
    '''
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

    # print("Betting $" + str(bet) + " on " + team + "'s moneyline of " + str(m1o) + " equals $" + str(round(profit, 2)) + " profit.") #Print profit


def isThereArbitrage(o1, o2): #Need combined market margin to be below 100%
    '''
    Input odds1 and odds2 as strings, ex: +130, -300
    Returns True if arbitrage is possible, False if not
    '''

    if (o1[:1] == "+"): #underdog team 1
        decOdds1 = (float(o1[1:])/100.0) + 1
        impliedProb1 = (1/decOdds1) * 100.0
    else: #favorite team 1
        decOdds1 = (100.0/float(o1[1:])) + 1
        impliedProb1 = (1/decOdds1) * 100.0


    if (o2[:1] == "+"): #underdog team 2
        decOdds2 = (float(o2[1:])/100.0) + 1
        impliedProb2 = (1/decOdds2) * 100.0
    else: #favorite team 2
        decOdds2 = (100.0/float(o2[1:])) + 1
        impliedProb2 = (1/decOdds2) * 100.0

    
    if ((impliedProb1 + impliedProb2) < 100.0):
        print(impliedProb1 + impliedProb2)
        return True, o1, o2
    else:
        print(impliedProb1 + impliedProb2)
        return False, o1, o2
    


# calculateMoneyLineProfitV1(*getMoneyLines()) # Math works for this one, used as testing for V2
# calculateMoneyLineProfitV2("gsw", "-140", 100) # Input team name, line, and bet manually
# print(isThereArbitrage("+120", "-102"))
# print(isThereArbitrage("+120", "-230"))


