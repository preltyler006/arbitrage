def calculateMoneyLineProfitV2(mt, mo, bet):
    '''
    This functions tells you the profit you can make based on the money line and the bet
    
    Args:
        mt: not used
        mo: Moneyline, ex "+120"
        bet: Bet size, ex 100

    Returns:
        The profit from moneyline and bet
    '''
    
    bet = int(bet)
    profit = 0

    if (mo[:1] == "+"): #If moneyline is underdog, +
        profit = float(float(bet)/100.0) * (float(mo[1:]))
    else: #If moneyline is favorite, -
        profit = (float(100/int(mo[1:])) * float(bet))
    
    return profit

    

def reversePayoutCalculator(profit, line, bet):
    '''
    This function is used to calculate the amount needed to bet on a line to equal the payout 
    of the first bet, so arbitrage is profitable
    
    ex:

    Bills: -300 to win
    $322.50 bet = $430 payout 

    Jets: +330 to win
    $100 bet = $430 payout

    Both have same payout, and total bet size is less than payout, meaning profit

    Args:
        profit: Profit from first line, ex: 231.60
        line: Second line odds, ex: "+203"
        bet: Bet size, ex: 100
    '''
    if(line[:1] == "+"):
        return ((float(profit + bet))/((float(line[1:])/100)+1))
    
    elif(line[:1] == "-"):
        return ((float(profit) + bet))/((100/float(line[1:]))+1)
    

def isThereArbitrage(o1, o2): #Need combined market margin to be below 100%
    '''
    This function tells you if an arbitrage is possible or not

    Args:
        o1: Odds of line 1, ex: +130
        o2: Odds of line 2, ex: -300

    Returns:
        True if arbitrage is possible, False if not
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
        return True, impliedProb1 + impliedProb2
    else:
        return False, impliedProb1 + impliedProb2
    


# def getMoneyLines():
#     '''
#     Originally used for calculateMoneyLineProfitV1, not needed anymore as V2 works much better
#     '''
#     # moneylineOne = input("What is the first team and moneyline? Split with a space: ")
#     moneylineOne = "gsw +140"
#     # moneylineTwo = input("What is the second team and moneyline? Split with a space: ")
#     moneylineTwo = "lal -120"

#     moneylineOne = moneylineOne.split(" ")
#     moneylineOneTeam = moneylineOne[0]
#     moneylineOneOdds = moneylineOne[1]
#     print(moneylineOneTeam + " has a moneyline of " + moneylineOneOdds)


#     moneylineTwo = moneylineTwo.split(" ")
#     moneylineTwoTeam = moneylineTwo[0]
#     moneylineTwoOdds = moneylineTwo[1]
#     print(moneylineTwoTeam + " has a moneyline of " + moneylineTwoOdds)

#     return moneylineOneTeam, moneylineOneOdds, moneylineTwoTeam, moneylineTwoOdds



# def calculateMoneyLineProfitV1(m1t, m1o, m2t, m2o): 
#     '''
#     Function returns profit on 4 parameters
#     Too many if/else statements, cluttered code, discarded
#     '''
#     teamAndBet = input("What is your bet on which team? Seperate with space, (ex: 100 buf) ")
#     team = teamAndBet[teamAndBet.index(" ") + 1: ]
#     bet = teamAndBet[:teamAndBet.index(" ")]
#     profit = 0

#     print(type(m1o), type(m2o))
#     print(m1o, m2o)


#     if (team == (m1t)):
#         if (m1o[:1] == "+"): #If moneyline is underdog
#             profit = float(float(bet)/100.0) * (float(m1o[1:])) - float(bet) #Calculate profit
#         else: #If moneyline is favorite
#             profit = (float(100/int(m1o[1:])) * float(bet)) #Calculate profit
#         team = m1t

#     elif (team == (m2t)): 
#         if (m2o[:1] == "+"): #If moneyline is underdog
#             profit = float(float(bet)/100.0) * (float(m2o[1:])) - float(bet) #Calculate profit
#         else: #If moneyline is favorite
#             profit = (float(100/int(m2o[1:])) * float(bet)) #Calculate profit
#         team = m2t
#     else:
#         print("bad")

#     # print("Betting $" + str(bet) + " on " + team + "'s moneyline of " + str(m1o) + " equals $" + str(round(profit, 2)) + " profit.") #Print profit

    


# calculateMoneyLineProfitV1(*getMoneyLines()) # Math works for this one, used as testing for V2
# calculateMoneyLineProfitV2("gsw", "-140", 100) # Input team name, line, and bet manually
# print(isThereArbitrage("+120", "-102"))
# print(isThereArbitrage("+120", "-230"))


