import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of player (2-4) : ")
    if players.isdigit():
        players = int(players)
        if 2<=players <=4:
           break
        else:
            print('Must be between 2-4 players.')
    else:
        print("try again enter number")

    
max_score = 50
player_score = [0 for _ in range(players)]


while max(player_score) < max_score:
    for player_idx in range(players):
        print('\n player',player_idx +1 , 'turn had started')
        print('plyer total score is: ',player_score[player_idx],'\n')
        current_score = 0

        while True:
            should_roll = input("would you like to roll (y)? : " )
            if should_roll.lower() != "y":
                break
            else:
                value = roll()

            if value == 1:
                print("you rolled 1 you done by")
                current_score = 0
                break
            else:
                current_score += value
                print("you rolled a ", value)


        player_score[player_idx] += current_score


max_score = max(player_score)
winning_idx = player_score.index(max_score)
print('Player ' ,winning_idx + 1, 'with score of ' , max_score)




