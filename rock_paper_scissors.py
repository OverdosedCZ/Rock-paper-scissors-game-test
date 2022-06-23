import random

def play():
    user = input("What's your choice?:'r' for rock, 'p' for paper and 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if computer == user:
        return 'It is a tie'
    

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    #s > p, r > s, p > r
    #returt true if the player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    

print(play())