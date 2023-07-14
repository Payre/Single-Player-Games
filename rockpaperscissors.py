import random as ra

def get_user_input():
    user = int(input('''1 for paper
2 for scissor
3 for rock
Press any other key to quit
:'''))
    opt = {1:'paper', 2:'scissor', 3:'rock'}
    return opt[user]

def get_npc():
    opt = {1:'paper', 2:'scissor', 3:'rock'}
    z = ra.randint(1,3)
    out = opt[z]
    return out

def get_result(user_pick, computer_pick):
    if computer_pick == user_pick:
        return 'draw'
    elif user_pick == 'paper' and computer_pick == 'rock':
        return 'win'
    elif user_pick == 'rock' and computer_pick == 'scissors':
        return 'win'
    elif user_pick == 'scissors' and computer_pick == 'paper':
        return 'win'
    else:
        return 'lose'

p1 = get_user_input()
p2 = get_npc()
result = get_result(p1, p2)

print(f"Computer's pick: {p2}")
print(f"Your pick: {p1}")
print(f"You {result}")
test