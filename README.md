# Tuple Out Dice Game 

## Description

Tuple Out is a dice rolling game where players earn points by rolling the dice. The first player to score 50 points wins the game.

## Rules and how to play

If two dice match, those matching dice are frozen, and only the remaining die can be re-rolled.
Players can re-roll the unfixed dice as many times as they like or stop and add up their points.
 If all three dice show the same number you "tuple out" and score 0 points for that turn.
Winner is when 50 points reached. 

## Code Explanation 

- The code begins with print statements that welcome players to the game and explain the rules.
- The code asks how many players are playing. After getting the number of players, it then asks for each player's name.
- Then each score is set to 0 and the winning point is 50 

## The Loop for Rolling the Dice
The function roll_dice() is used to roll three dice by generating random numbers between 1 and 6.
When it's a player's turn, the game rolls the dice and shows the results.

## Checking for Tuple Out

If all three dice show the same number, the player "tuples out." The turn ends, and they get 0 points.

## Freezing and Re-Rolling

If two dice show the same number, they are "fixed_frozen" (frozen) and can't be rolled again.
The player gets to decide if they want to roll the unfixed dice again.
This keeps going until the player either stops or "tuples out."

## Scoring and Winning

When a player stops rolling, their dice are added to their score. Scores are shown after each turn. The first player to reach 50 points wins, and the game ends with a "Game Over" message and a thank you for playing.


