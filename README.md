# monopyly
A Monopoly Board Game Simulator

## Goals
The goal of this script was to simulate a single player moving around a Monopoly board.

I wanted to know the average percentage chance of landing on any given square 
and any square type.

## Process
The script simulates X rounds over Y iterations to calculate the percentages.

If there were no chance and community chest cards or the Go To Jail spaces, after a few rounds 
I would expect an even distribution of landing on any given square.

However, because a player can be artificially moved around the board, some squares and types
are landed on more than others.

## Results
Running the script for 100 rounds over 1 million iterations, I got these results:

##### Squares:
- &nbsp;&nbsp;&nbsp;&nbsp; Go: 1.827%
- ![#654321](https://placehold.it/15/654321/000000?text=+) Mediterranean Avenue: 1.318%
- &nbsp;&nbsp;&nbsp;&nbsp; Community Chest: 1.404%
- ![#654321](https://placehold.it/15/654321/000000?text=+) Baltic Avenue: 1.481%
- &nbsp;&nbsp;&nbsp;&nbsp; Income Tax: 1.683%
- &nbsp;&nbsp;&nbsp;&nbsp; Reading Railroad: 2.273%
- ![#ADD8E6](https://placehold.it/15/ADD8E6/000000?text=+) Central Avenue: 1.77%
- &nbsp;&nbsp;&nbsp;&nbsp; Chance: 1.906%
- ![#ADD8E6](https://placehold.it/15/ADD8E6/000000?text=+) Vermont Avenue: 1.853%
- ![#ADD8E6](https://placehold.it/15/ADD8E6/000000?text=+) Connecticut Avenue: 1.824%
- &nbsp;&nbsp;&nbsp;&nbsp; **Jail: 11.478%**
- ![#ff69b4](https://placehold.it/15/ff69b4/000000?text=+) St. Charles Place: 2.266%
- &nbsp;&nbsp;&nbsp;&nbsp; Electric Company: 4.033%
- ![#ff69b4](https://placehold.it/15/ff69b4/000000?text=+) States Avenue: 1.634%
- ![#ff69b4](https://placehold.it/15/ff69b4/000000?text=+) Virginia Avenue: 3.846%
- &nbsp;&nbsp;&nbsp;&nbsp; Pennsylvania Railroad: 1.826%
- ![#ffa500](https://placehold.it/15/ffa500/000000?text=+) **St. James Place: 4.223%**
- &nbsp;&nbsp;&nbsp;&nbsp; Community Chest: 1.753%
- ![#ffa500](https://placehold.it/15/ffa500/000000?text=+) **Tennessee Avenue: 4.561%**
- ![#ffa500](https://placehold.it/15/ffa500/000000?text=+) **New York Avenue: 2.081%**
- &nbsp;&nbsp;&nbsp;&nbsp; Free Parking: 4.856%
- ![#ff0000](https://placehold.it/15/ff0000/000000?text=+) Kentucky Avenue: 1.754%
- &nbsp;&nbsp;&nbsp;&nbsp; Chance: 5.124%
- ![#ff0000](https://placehold.it/15/ff0000/000000?text=+) Indiana Avenue: 1.732%
- ![#ff0000](https://placehold.it/15/ff0000/000000?text=+) Illinois Avenue: 3.815%
- &nbsp;&nbsp;&nbsp;&nbsp; B. & O. Railroad: 1.979%
- ![#ffff00](https://placehold.it/15/ffff00/000000?text=+) Atlantic Avenue: 2.967%
- ![#ffff00](https://placehold.it/15/ffff00/000000?text=+) Ventnor Avenue: 1.658%
- &nbsp;&nbsp;&nbsp;&nbsp; Water Works: 2.724%
- ![#ffff00](https://placehold.it/15/ffff00/000000?text=+) Marvin Gardens: 1.614%
- &nbsp;&nbsp;&nbsp;&nbsp; Go To Jail: 2.347%
- ![#006400](https://placehold.it/15/006400/000000?text=+) Pacific Avenue: 1.665%
- ![#006400](https://placehold.it/15/006400/000000?text=+) North Carolina Avenue: 2.031%
- &nbsp;&nbsp;&nbsp;&nbsp; Community Chest: 1.648%
- ![#006400](https://placehold.it/15/006400/000000?text=+) Pennsylvania Avenue: 1.661%
- &nbsp;&nbsp;&nbsp;&nbsp; Short Line: 1.48%
- &nbsp;&nbsp;&nbsp;&nbsp; Chance: 1.408%
- ![#003366](https://placehold.it/15/003366/000000?text=+) Park Place: 1.338%
- &nbsp;&nbsp;&nbsp;&nbsp; Luxury Tax: 1.32%
- ![#003366](https://placehold.it/15/003366/000000?text=+) Board Walk: 1.841%

##### Types:
- &nbsp;&nbsp;&nbsp;&nbsp; Go: 1.827%
- ![#654321](https://placehold.it/15/654321/000000?text=+) Brown: 2.799%
- &nbsp;&nbsp;&nbsp;&nbsp; Tax: 1.683%
- &nbsp;&nbsp;&nbsp;&nbsp; Railroad: 7.559%
- ![#ADD8E6](https://placehold.it/15/ADD8E6/000000?text=+) Light Blue 5.446%
- &nbsp;&nbsp;&nbsp;&nbsp; Chance: 8.437%
- &nbsp;&nbsp;&nbsp;&nbsp; **Jail: 11.478%**
- ![#ff69b4](https://placehold.it/15/ff69b4/000000?text=+) Pink: 7.745%
- &nbsp;&nbsp;&nbsp;&nbsp; Utility: 6.756%
- ![#ffa500](https://placehold.it/15/ffa500/000000?text=+) **Orange: 10.865%**
- &nbsp;&nbsp;&nbsp;&nbsp; Community Chest: 4.804%
- &nbsp;&nbsp;&nbsp;&nbsp; Free Parking 4.856%
- ![#ff0000](https://placehold.it/15/ff0000/000000?text=+) Red: 7.301%
- ![#ffff00](https://placehold.it/15/ffff00/000000?text=+) Yellow: 6.24%
- &nbsp;&nbsp;&nbsp;&nbsp; Go To Jail: 2.347%
- ![#006400](https://placehold.it/15/006400/000000?text=+) Green: 5.357%
- ![#003366](https://placehold.it/15/003366/000000?text=+) Dark Blue: 4.499%

## Conclusion
Based on the results, the Jail square (both in jail and visiting jail) is the most
visited square at 11.478%. As for housing types, Orange is the most landed on at 
10.865% followed by Pink and Red at 7.745% and 7.301% respectively.

It makes sense the Orange would be the most visited type given that Jail is the most
visited square. The average roll of two dice will be 7 and Orange is 6 to 9 squares away.

Pink accounts for the rolls from Jail that are low and Red accounts for the rolls 
from Jail that are high.

## How to Run
1. Via a command line, change to this git repository on your local machine.
2. The `simulate.py` module accepts two positional arguments: `rounds` and `games`.
3. Type `python3 simulate.py rounds games` (changing out rounds and games for the integer values you want)
    - *e.g.,* `python3 simulate.py 100 1000000` for 100 rounds for 1,000,000 games
    
*Note:* This Python script uses Python 3. Make sure to use the appropriate Python call.