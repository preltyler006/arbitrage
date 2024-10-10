from isThereArbitrage import *



def arbitrageBetCalculator(bet, o1, o2):
    '''
    This function tells the user if arbitrage is possible, and what money to bet on which lines

    Args:
        bet: Initial amount wanted to wager on 1st line
        o1, o2: Odds or Lines inputted as string, ex: "+130"

    Returns:
        Returns a tuple of either a float and a string (printed message for user) if possible,
        Or a tuple of a boolean (False) and an empty string if not possible.
    '''

    if(isThereArbitrage(o1, o2)[0]): #valid Arbitrage
        
        # print("Arbitrage is possible with a " + str(round((100-(isThereArbitrage(o1, o2)[1])), 2)) + "% profit margin\n")

        if (o1[:1] == "+" and o2[:1] == "+"): #if 1st and 2nd line are underdog
            profitLine1 = float(calculateMoneyLineProfitV2("team", o1, bet)) #Calculates profit based on original bet for first line
            betForLine2 = round(reversePayoutCalculator(profitLine1, o2, bet), 2) #Calculates bet needed on second line to equal payout for first line
            profitLine2 = float(calculateMoneyLineProfitV2("team", o2, betForLine2)) #Calculates profit for second line

            returnMessage = "\nBetting $" + str(bet) + " on " + o1  + " results in $" + str(profitLine1 + bet) + " payout.\n" + "Betting $" + str(betForLine2) + " on " + o2 + " results in $" + str(profitLine2 + betForLine2) + " payout.\n" + "Your guaranteed profit will be $" + str(round(((profitLine1 + bet) - (bet + betForLine2)), 2)) + "\n------------------------------------------------------------------------------" + "\n\n"
                #prints for user to know what to bet where
            return round(((profitLine1 + bet) - (bet + betForLine2)), 2), returnMessage
        


        elif (o1[:1] == "-" and o2[:1] == "+"): #if 1st line is favorite and 2nd line is underdog
            profitLine2 = float(calculateMoneyLineProfitV2("team", o2, bet))
            betForLine1 = round(reversePayoutCalculator(profitLine2, o1, bet), 2)
            profitLine1 = round(float(calculateMoneyLineProfitV2("team", o1, betForLine1)), 2)
            

            returnMessage = "\nBet $" + str(bet) + " on the " + o2 + " line to get $" + str(profitLine2 + bet) + " payout for underdog\n" + ("Bet $" + str(betForLine1) + " on the " + o1 + " line to get $" + str(betForLine1 + profitLine1) + " payout for favorite \n") + ("Your guaranteed profit will be $" + str(round(((profitLine2 + bet) - (bet + betForLine1)), 2)) + "\n------------------------------------------------------------------------------" + "\n\n")
            return round(((profitLine2 + bet) - (bet + betForLine1)), 2), returnMessage



        elif (o1[:1] == "+" and o2[:1] == "-"): #if 1st line is underdog and 2nd line is favorite
            profitLine1 = float(calculateMoneyLineProfitV2("team", o1, bet))
            betForLine2 = round(reversePayoutCalculator(profitLine1, o2, bet), 2)
            profitLine2 = round(float(calculateMoneyLineProfitV2("team", o2, betForLine2)), 2)
            
            returnMessage = "\nBet $" + str(bet) + " on the " + o1 + " line to get $" + str(profitLine1 + bet) + " payout for underdog\n" + "Bet $" + str(betForLine2) + " on the " + o2 + " line to get $" + str(betForLine2 + profitLine2) + " payout for favorite\n" + "Your guaranteed profit will be $" + str(round(((profitLine1 + bet) - (bet + betForLine2)), 2)) + "\n------------------------------------------------------------------------------" + "\n\n"
            return round(((profitLine1 + bet) - (bet + betForLine2)), 2), returnMessage
        
    else: #No valid Arbitrage
        return False, " "
        # Returns tuple for ease of use in other python files

