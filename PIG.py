import random

def roll():
    roll_dice = random.randint(1,6)
    return roll_dice

while True:
    numof_players = input("How many players will play (2-4)? ")
    if numof_players.isdigit() and 1< int(numof_players) <5:
        numof_players = int(numof_players)
        break
    else:
        print("Invalid input.Please try again.")

players_scores = [0 for _ in range(numof_players)]
try:
    max_score = int(input("Enter the winning boundary (number): "))
except ValueError:
    print("Invalid input.The number must be greater than 0.")
    quit()

while max_score > max(players_scores):
    for player_idx in range(numof_players):
            print(f"\nPlayer {player_idx+1}'s turn.")
            current_score = 0
            while True:
                user_response = input("\nTo roll enter (y).Type Here: ").strip().lower()
                
                if user_response != "y":
                    print("Invalid,Please try again.")
                    continue
                rolled = roll()

                if rolled == 1:
                    print(f"You rolled a {rolled}.\nYour turn is over.\nNew score is 0.")
                    current_score = 0
                    players_scores[player_idx] = 0
                    break

                print(f"\nYou rolled a {rolled}.")
                current_score += rolled
                players_scores[player_idx] = current_score
                print(f"Your current score: {players_scores[player_idx]}")

                if current_score > max_score:
                    break    
                
    
winner = max(players_scores)
winner_idx = players_scores.index(winner)
print(f"\nPlayer {winner_idx+1} won the game.")
