import requests
import os

API_KEY = os.getenv("api_key")

SPORT = 'upcoming' # use the sport_key from the /sports endpoint below, or use 'upcoming' to see the next 8 games across all sports

REGIONS = 'us' # uk | us | eu | au. Multiple can be specified if comma delimited

MARKETS = 'h2h,spreads' # h2h | spreads | totals. Multiple can be specified if comma delimited

ODDS_FORMAT = 'american' # decimal | american

DATE_FORMAT = 'unix' # iso | iso or unix - mm/dd/yyyy


sports_response = requests.get(
    'https://api.the-odds-api.com/v4/sports', 
    params={
        'api_key': '2da3a631afd1f7b9a83b4d202bb19c59'
    }
)

if sports_response.status_code != 200: # Client/Server Request error
    print(f'Failed to get sports: status_code {sports_response.status_code}, response body {sports_response.text}')

else:
    print('List of in season sports:', sports_response.json())

