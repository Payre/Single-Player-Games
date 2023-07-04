#necessary modules
import numpy as np
import random as rad


#creating a game board

'''initializing an empty board with an order of 3x3'''
board = np.array([[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']])
#print(board)

#the ai of the game
def ai(npc):
    while True:
        npc_r = rad.randint(0,2)
        npc_c = rad.randint(0,2)
        if board[npc_r, npc_c] == ' ':
            board[npc_r, npc_c] = npc
            break


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
    ai(npc)
    print(board)
    print("ok xa ta")

#checks win or loss
'''    if inpu == "x":
        if (board[0,0] == board[1,1] == board[2,2]) or (board[0,2] == board[1,1] == board[2,0]) or (board[0,0] == board[0,1] == board[0,2]) or (board[1,0] == board[1,1] == board[1,2]) or (board[2,0] == board[2,1] == board[2,2]) or (board[0,0] == board[1,0] == board[2,0]) or (board[0,1] == board[1,1] == board[2,1] or (board[0,2] == board[1,2] == board[2,2])):
            print(f"{inpu} is the winner")
            break
    else:
        if (board[0,0] == board[1,1] == board[2,2]) or (board[0,2] == board[1,1] == board[2,0]) or (board[0,0] == board[0,1] == board[0,2]) or (board[1,0] == board[1,1] == board[1,2]) or (board[2,0] == board[2,1] == board[2,2]) or (board[0,0] == board[1,0] == board[2,0]) or (board[0,1] == board[1,1] == board[2,1] or (board[0,2] == board[1,2] == board[2,2])):
            print(f"{inpu} is the winner")
            break'''




#taking input from the user.
#choose position - make infinite; switch player; declare winner.
#once the game is functional, release beta 0.0 on github
#try to implement function for alpha release.
#make more user friendly 1.5
#add graphics 2.0
#end project

#libraries infomration
'''random: https://docs.python.org/3/library/random.html'''

