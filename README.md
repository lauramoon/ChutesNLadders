# Chutes and Ladders
Analysis of Thousands of Simulations of Chutes and Ladders Games

There are no choices to make in the game of Chutes and Ladders (also known as snakes and ladders or snakes and arrows). Therefore, it is an easy game to simulate. These analyses simplify things further by considering only a single player's journey to square 100. All the code used to produce the figures is in main.py.

## How Many Turns to Win?
Figures 1 and 3 show histograms of two different simulations of 20,000 games. The number of turns to win ranges from 7 to over 300, with the peak around 30. It is clearly not a Gaussian distribution.

Figure 2 examines the statistices of simulations sets more closely. The mean, median, mode, and stadard deviation for number of turns for 5000 simulations was recorded and repeated 100 times. The box plots of Figure 2 show how these statistics differ accross the 100 sets of simulations. It is worth noting that the mean, median, and mode do not overlap at all, as the long tail of long games skews the results. The long games pull the mean up to around 39, while the median number of turns is around 32-33. But the most common number of turns is lower, varying from 15 to 28 across the different simulation sets.

## The Longest Chute
The dreaded space 87 sends the poor player the whole way back to square 24. It seems that the more times one lands on this chute, the longer it takes to complete the game. Figure 4 shows that this intuition is correct. In 100,000 simulations, the longest chute was traversed as many as 11 times, and these games could last hundreds of turns.

Games with many trips down the long chute are rare, however. Figure 5 shows that 0 is by far the most common number of times to land on square 87, while 9, 10, and 11 only occurred a few times in the 100,000 simulations.

Future work may include calculating a model for the relationship between the number of times down the longest slide and the length of game.

## Are All Chutes and Ladders Equally likely to be traveled?
In short, no. Some chutes and ladders are traversed more frequently than others. See Figure 6. The chutes and ladders are labeled by their starting square.
