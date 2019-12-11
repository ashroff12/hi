#2048 game
import random
import sys
score = 0
highscore = 0

board = []

def newgame():
    global board
    #fill board
    board = []
    row = []
    for i in range(4):
        row.append(0)
    for j in range(4):
        board.append(row.copy())
    newnumber()
    newnumber()
    newnumber()

def showboard():
    for i in range(4):
        row = ""
        for j in range(4):
            row = row + str(board[i][j]) + " "
        print(row)

def newnumber():
    newnum = 0
    newrow = random.randint(0,3)
    newcol = random.randint(0,3)
    while board[newrow][newcol] != 0:
        newrow = random.randint(0,3)
        newcol = random.randint(0,3)
    rand = random.randint(1,100)
    if rand < 10:
        newnum = 2
    else:
        newnum = 4
    board[newrow][newcol] = newnum

def move():
    print("select your direction (<, >, V, ^)")
    mymove = input()
    if mymove == "<":
        rotate(2)
        swiperight()
        rotate(2)
    elif mymove== ">":
        swiperight()
    elif mymove== "V":
        rotate(3)
        swiperight()
        rotate(1)
    elif mymove== "^":
        rotate(1)
        swiperight()
        rotate(3)
    else:
        print("LEAVE... THAT IS NOT A OPTION")
        sys.quit
    move()
def swiperight():
    x=0


def rotate(number_turns):
    x=0
newgame()
showboard()
            
    
