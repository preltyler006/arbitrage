import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()
API_KEY = os.getenv("api_key")
# print(API_KEY) # Test to see api key working

SPORT = 'upcoming' # use the sport_key from the /sports endpoint below, or use 'upcoming' to see the next 8 games across all sports

REGIONS = 'us' # uk | us | eu | au. Multiple can be specified if comma delimited

MARKETS = 'h2h' # h2h moneyline | spreads points handicaps | totals over/under. Multiple can be specified if comma delimited

ODDS_FORMAT = 'american' # decimal | american

DATE_FORMAT = 'unix' # iso | iso or unix - mm/dd/yyyy


sports_response = requests.get(
    'https://api.the-odds-api.com/v4/sports', 
    params={
        'api_key': API_KEY
    }
)

if sports_response.status_code != 200: # Client/Server Request error
    print(f'Failed to get sports: status_code {sports_response.status_code}, response body {sports_response.text}')

else:
    print('List of in season sports:', sports_response.json())



# odds_response = requests.get(
#     f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds',
#     params={
#         'api_key': API_KEY,
#         'regions': REGIONS,
#         'markets': MARKETS,
#         'oddsFormat': ODDS_FORMAT,
#         'dateFormat': DATE_FORMAT,
#     }
# )

# if odds_response.status_code != 200:
#     print(f'Failed to get odds: status_code {odds_response.status_code}, response body {odds_response.text}')

# else:
#     odds_json = odds_response.json()
#     print('Number of events:', len(odds_json))
#     print(odds_json)
#     with open('./data.txt', 'w') as doc:
#         for line in odds_json:
#             doc.write(f"{line}\n")

#     # Check the usage quota
#     print('Remaining requests', odds_response.headers['x-requests-remaining'])
#     print('Used requests', odds_response.headers['x-requests-used'])
