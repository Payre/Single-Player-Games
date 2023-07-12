#necessary modules
import numpy as np
import random as rad

#creating multiplayer
print("\t\t\t\t\t\tTic - x - Tac - o - Toe\n")
print("\t\t\t\t\t\tPress 1 for Single Player\n")
print("\t\t\t\t\t\tPress 2 for Multiplayer \n")
mode = int(input("\t\t\t\t\t\tSelect your mode: "))

#creating a game board

'''initializing an empty board with an order of 3x3'''
board = np.array([[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']])
#print(board)

#the single player of the game
def ai(npc):
    while True:
        npc_r = rad.randint(0,2)
        npc_c = rad.randint(0,2)
        if board[npc_r, npc_c] == ' ':
            board[npc_r, npc_c] = npc
            break
        check_win(board, npc)

#multiplayer
def multi(npc):
    for x in range(5):
        r = int(input("Enter the row: "))
        c = int(input("Enter the column: "))
        r -= 1
        c -= 1
        board[r,c]=npc
        print(board)
        print("ok xa ta")
        check_win(board, npc)
        break
        

def check_win(board, temo):
    #checking if coloumn win or loss
    for r in range(3):
        if all(board[r, c] == temo for c in range(3)):
            return True
    #checking for row
    for c in range(3):
        if all(board[r,c] == temo for r in range(3)):
            return True
    #diagnoal
        if board[0, 0] == board[1, 1] == board[2, 2] == temo or board[0, 2] == board[1, 1] == board[2, 0] == temo:
            return True

#player choose - completed
while True:
    inpu = input("Enter X or O: ").lower() #fucking dumb, forgot to take input again inside the loop.
    if inpu == 'x' or inpu == 'o':
        print(f"Player one is {inpu}")
        break
    else:
        print("Please enter a valid input, only 'X' and 'O'.")
#switch mechanism:
if inpu == "x":
    npc = "o".lower()
else:
    npc = "x".lower()

#position selector
for x in range(5):
    r = int(input("Enter the row: "))
    c = int(input("Enter the column: "))
    r -= 1
    c -= 1
    board[r,c]=inpu
    print(board)
    print("ok xa ta")
    if check_win(board, inpu):
        print(f"Player {inpu} wins!")
        break
    if mode == 1:
        ai(npc)
        print(board)
        if check_win(board, npc):
            print(f"Player {npc} wins!")
            print("GIT GUD!")
            break
    else:
        multi(npc)
        if check_win(board, npc):
            print(f"Player {npc} wins!")
            print(f"GIT GUD! Noob")
            break



#status and to work
'''
1. User input is dominant fix that
2. Add multiplayer
3. Add graphics'''



#taking input from the user.
#choose position - make infinite; switch player; declare winner.
#once the game is functional, release beta 0.0 on github
#try to implement function for alpha release.
#make more user friendly 1.5
#add graphics 2.0
#end project

#libraries infomration
'''random: https://docs.python.org/3/library/random.html'''

