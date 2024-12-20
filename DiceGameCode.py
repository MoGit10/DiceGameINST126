import random
import time 
import sys
import pandas as pd

print("Welcome to the 'Tuple Out' Dice Game!")
print("Try to get the highest score without 'tupling out' (rolling three of the same number).")
print("If two dice match, they stay fixed, and you can re-roll the rest.")
print("First player to reach 50 points wins the game!")

#This will get how many players are playing and ensure there is at least 1 player
while True:
    try:
        num_players = int(input("How many players are playing? "))
        if num_players < 1:
            print("You need atleast 1 player to play the game!")
        else: 
            break
    except ValueError:
        print("Please enter a valid number")

# Here we will get the name of the player or players 
player_names = []
for char in range(num_players): 
    name = input(f"Enter the name of player {char + 1}: ")
    player_names.append(name)

# If there is only 1 player, explain the new rule to get the highest score possible
if num_players == 1:
    print("\nYou are playing alone, The goal now is to reach the highest score possible!")
    time.sleep(1)
    

#This is a set up for player scores
player_scores = {}
for name in player_names:
    player_scores[name] = 0

#How many points someone needs to win game 
winning_score = 50

#Here I am using random function to roll dice
def roll_dice():
    return [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

# This is the main game loop, it continues until a player wins or the game ends.
game_over = False
while not game_over:
    for player in player_names:
        print(f"\n{player}'s turn!")
        time.sleep(0.5)
        
        dice = roll_dice()
        print(f"You rolled: {dice}")
        time.sleep(0.5)
        
        #Check if all dice are the same
        if dice[0] == dice[1] == dice[2]:
            print("You 'tupled out' and got 0 points this turn.")
            time.sleep(0.5)
            continue
        
        #This is to ask the player if they want to re-roll
        while True:
            #This is to find fixed dice
            fixed_frozen = []
            for char in dice: 
                if dice.count(char) == 2:
                    fixed_frozen.append(char)
            
            #This is to find unfixed dice
            unfixed = []
            for char in dice: 
                if char not in fixed_frozen:
                    unfixed.append(char)

            #This is to stop if there are no unfixed dice
            if len(unfixed) == 0:
                break

            #This will ask if the player wants to re-roll
            choice = input(f"Fixed dice: {fixed_frozen}. Unfixed dice: {unfixed}. Do you want to roll again? (y/n): ").lower()
            if choice != 'y':
                break

            #This is for re roll the unfixed dice
            for char in range(len(dice)): 
                if dice[char] not in fixed_frozen:
                    dice[char] = random.randint(1, 6)
            
            print(f"You rolled: {dice}")
            time.sleep(0.5)
            
            #In here we check if player has tupled out
            if dice[0] == dice[1] == dice[2]:
                print("You 'tupled out' and got 0 points this turn.")
                time.sleep(0.5)
                break

        #This adds up the points if the player didn't tuple out
        if dice[0] != dice[1] or dice[1] != dice[2]:
            points = sum(dice)
            player_scores[player] += points
            print(f"{player} earned {points} points this turn. Total score: {player_scores[player]}")
        
        #This will check if the current player has reached the target score to win the game.
        if player_scores[player] >= winning_score:
            print(f"\nCongratulations, {player}! You win with {player_scores[player]} points!")
            game_over = True
            break

# Here I am using pandas to display the scoreboard 
print("\nFinal scores: ")
time.sleep(0.5)
scores_df = pd.DataFrame(player_scores.items(), columns=["Player", "Score"])
print(scores_df)

# This is for exit 
print("\nThanks for playing! Game over!") 
time.sleep(0.5)
sys.exit() 
