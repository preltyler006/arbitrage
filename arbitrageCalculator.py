from isThereArbitrage import *



def arbitrageBetCalculator(bet, o1, o2):
    '''
    1st parameter, input total amount wanted to wager
    o1, o2 input as string ex: "+130"
    '''

    if(isThereArbitrage(o1, o2)[0]): #valid Arbitrage
        print("Arbitrage is possible with a " + str(round((100-(isThereArbitrage(o1, o2)[1])), 2)) + "% profit margin\n")
        #put $100 on underdog, and reverse engineer amount needed to get same payout on favorite line
        if (o1[:1] == "+" and o2[:1] == "+"): #if 1st and 2nd line are underdog
            profitLine1 = float(calculateMoneyLineProfitV2("team", o1, bet))
            betForLine2 = round(reversePayoutCalculator(profitLine1, o2, bet), 2) #calculates money needed to equal payout for favorite line
            profitLine2 = float(calculateMoneyLineProfitV2("team", o2, betForLine2))

            print("Betting $" + str(bet) + " on " + o1  + " results in " + str(profitLine1 + bet) + " payout.")
            print("Betting $" + str(betForLine2) + " on " + o2 + " results in " + str(profitLine2 + betForLine2) + " payout.")
            print("\nYour profit will be $" + str(round(((profitLine1 + bet) - (bet + betForLine2)), 2)) + "\n")

        
        elif (o1[:1] == "-" and o2[:1] == "+"): #if 1st line is favorite and 2nd line is underdog
            profitLine2 = float(calculateMoneyLineProfitV2("team", o2, bet))
            betForLine1 = round(reversePayoutCalculator(profitLine2, o1, bet), 2)
            profitLine1 = round(float(calculateMoneyLineProfitV2("team", o1, betForLine1)), 2)
            
            print("bet $" + str(bet) + " on the " + o2 + " line to get " + str(profitLine2 + bet) + " payout for underdog")
            print("bet $" + str(betForLine1) + " on the " + o1 + " line to get " + str(betForLine1 + profitLine1) + " payout for favorite")
            print("\nYour profit will be $" + str(round(((profitLine2 + bet) - (bet + betForLine1)), 2)) + "\n")

        elif (o1[:1] == "+" and o2[:1] == "-"): #if 1st line is underdog and 2nd line is favorite
            profitLine1 = float(calculateMoneyLineProfitV2("team", o1, bet))
            betForLine2 = round(reversePayoutCalculator(profitLine1, o2, bet), 2)
            profitLine2 = round(float(calculateMoneyLineProfitV2("team", o2, betForLine2)), 2)
            
            print("\nbet $" + str(bet) + " on the " + o1 + " line to get " + str(profitLine1 + bet) + " payout for underdog")
            print("bet $" + str(betForLine2) + " on the " + o2 + " line to get " + str(betForLine2 + profitLine2) + " payout for favorite")
            print("\nYour profit will be $" + str(round(((profitLine1 + bet) - (bet + betForLine2)), 2)) + "\n")

        
    else:
        print(isThereArbitrage(o1, o2))
        return "Arbitrage Not Possible"

print("\n")
