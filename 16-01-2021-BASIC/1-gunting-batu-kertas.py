import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors?\n ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print("komputer memilih " + computer)
        return "It\' s a tie" #hasilnya sama

    if is_win(user, computer):
        print("komputer memilih " + computer)
        return "you won!"
    
    return "komputer memilih " + computer + "\nYou lost!"

def is_win(player, opponent):
    # return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True 

print(play())