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
- Go: 1.827%
- Mediterranean Avenue: 1.318%
- Community Chest: 1.404%
- Baltic Avenue: 1.481%
- Income Tax: 1.683%
- Reading Railroad: 2.273%
- Central Avenue: 1.77%
- Chance: 1.906%
- Vermont Avenue: 1.853%
- Connecticut Avenue: 1.824%
- Jail: 11.478%
- St. Charles Place: 2.266%
- Electric Company: 4.033%
- States Avenue: 1.634%
- Virginia Avenue: 3.846%
- Pennsylvania Railroad: 1.826%
- St. James Place: 4.223%
- Community Chest: 1.753%
- Tennessee Avenue: 4.561%
- New York Avenue: 2.081%
- Free Parking: 4.856%
- Kentucky Avenue: 1.754%
- Chance: 5.124%
- Indiana Avenue: 1.732%
- Illinois Avenue: 3.815%
- B. & O. Railroad: 1.979%
- Atlantic Avenue: 2.967%
- Ventnor Avenue: 1.658%
- Water Works: 2.724%
- Marvin Gardens: 1.614%
- Go To Jail: 2.347%
- Pacific Avenue: 1.665%
- North Carolina Avenue: 2.031%
- Community Chest: 1.648%
- Pennsylvania Avenue: 1.661%
- Short Line: 1.48%
- Chance: 1.408%
- Park Place: 1.338%
- Luxury Tax: 1.32%
- Board Walk: 1.841%

##### Types:
- Go: 1.827%
- Brown: 2.799%
- Tax: 1.683%
- Railroad: 7.559%
- Light Blue 5.446%
- Chance: 8.437%
- Jail: 11.478%
- Pink: 7.745%
- Utility: 6.756%
- Orange: 10.865%
- Community Chest: 4.804%
- Free Parking 4.856%
- Red: 7.301%
- Yellow: 6.24%
- Go To Jail: 2.347%
- Green: 5.357%
- Dark Blue: 4.499%

## Conclusion
Based on the results, the Jail square (both in jail and visiting jail) is the most
visited square at 11.478%. As for housing types, Orange is the most landed on at 
10.865% followed by Pink and Red.

It makes sense the Orange would be the most visited type given that Jail is the most
visited square. The average roll of two dice will be 7 and Orange is 6 to 9 squares away.

Pink accounts for the rolls from Jail that are low and Red accounts for the rolls 
from Jail that are high.