# Project Arbitrage
Arbitrage is a rare event that can be used in sports betting in order to place bets on both sides of a match to guarantee profit. This calculator tells you if two lines have the possibility to create this arbitrage.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following libraries
```bash
pip install certifi
pip install idna
pip install python-dotenv
pip install requests
python -m pip install urllib3urllib3
```

## API Setup
In order to use this program to its fullest extent, you need to create a free account and obtain an API key from [the-odds-api.com](the-odds-api.com). This will allow you to access all of the sportsbooks and their available games automatically. The free account as of writing this gives you 500 requests.

After you have obtained this key, you want to create file named ```.env``` in the main folder of your project, and place your key in this file like so:
```env
api_key=examplekey1234
```
Now you are ready to use the program!

## Usage
In the ```main.py``` file, there are two functions at the bottom of the page with comments describing what they do. ```writeToDataFile()``` will use your api key and access all of the necessary data, copying it into a text file (default is ```apiCallData.txt```), with the data type being key-value pairs. ```line_and_team()``` will use the data in the aforementioned text file to determine if a betting arbitrage is possible using equations gathered from the articles listed below. The inline comments and given docstring outlines how to use this function as well.

## Problems/Other Things to Note
* This API used in this program is either very slow and/or very inconsistent as the data given in the text files are sometimes off by a few hundred points, which defeats the purpose of this program.
	* However, the point of this program was not to create a consistent and foolproof way to exploit the gambling industry, but rather to show that theoretically it was possible, and it is!
		* This was where I got the idea for the program: [oddsjam.com](https://oddsjam.com/betting-tools/arbitrage)
		
* The sports leagues which are available to use in this program are limited to major American sports leagues, as those odds were the ones I researched on how to calculate. You can add more of these sports, but be advised that some of these sports may not work yet:
	* In the ```jsonReaderV2.py``` file, on line 57, update the variable ```listOfSports```, which is a tuple containing the names of the sports organizations that you want. You can find the rest of these sports official names on [the-odds-api.com](https://stackedit.io/the-odds-api.com) offical documentation, or if you see a game in the text file that you want to add under ```'sport_key'``` in the ```apiCallData.txt``` file.