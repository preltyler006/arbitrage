import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()
API_KEY = os.getenv("api_key")
# print(API_KEY) # Test to see api key working

SPORT = 'upcoming' # use the sport_key from the /sports endpoint below, or use 'upcoming' to see the next 8 games across all sports

GROUP = 'group'

REGIONS = 'us' # uk | us | eu | au. Multiple can be specified if comma delimited

MARKETS = 'h2h' # h2h moneyline | spreads points handicaps | totals over/under. Multiple can be specified if comma delimited

ODDS_FORMAT = 'american' # decimal | american

DATE_FORMAT = 'iso' # iso | iso - mm/dd/yyyy or unix 


def writeToDataFile(fileName):
    '''
    This function calls the sportsodds api and makes a request to get all the specified data above,
    and writes all of this to a text file

    Args:
        fileName: The full filepath, ex: './apiCallData.txt'
    
    Returns:
        None; Instead, prints a success or failure message to screen, along with number of API calls left
    '''

    odds_response = requests.get(
        f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds',
        params={
            'api_key': API_KEY,
            'regions': REGIONS,
            'markets': MARKETS,
            'group' : GROUP,
            'oddsFormat': ODDS_FORMAT,
            'dateFormat': DATE_FORMAT,
        }
    )

    if odds_response.status_code != 200: # If status code is not valid, usually client side if any errors
        print(f'Failed to get odds: status_code {odds_response.status_code}, response body {odds_response.text}')

    else:
        odds_json = odds_response.json()

        # Writes every line in json file to text file for later use
        with open(fileName, 'w') as doc:
            for line in odds_json:
                doc.write(f"{line}\n")

        # Check the usage quota
        print('Remaining requests', odds_response.headers['x-requests-remaining'])
        print('Used requests', odds_response.headers['x-requests-used'])
