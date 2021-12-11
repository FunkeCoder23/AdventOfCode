#!python.exe
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument(
    '-t', '--test', help="Run with test input", action='store_true')
args = parser.parse_args()


def getInput(file="input"):
    path = sys.path[0]
    if args.test:
        file = "test_input"
    with open(f"{path}/{file}", "r") as f:
        lines = f.read()
        return lines.splitlines()


def dprint(msg):
    if args.test:
        print(msg)


SIZE = 10


def get_board(input):
    board = []
    for c, l in enumerate(input):
        board.append(list(int(i) for i in l))
    return board

global flashed
flashed=[]

def step(board):
    inc(board)
    while check(board):
        continue
    reset(board)

def reset(board):
    # dprint("resetting")
    for i, r in enumerate(board):
        for j, c in enumerate(r):
            if c > 9:
                board[i][j]=0
    bprint(board)
                
def check(board):
    # dprint("Checking")
    global flashed
    changed = False
    for i, r in enumerate(board):
        for j, c in enumerate(r):
            if c > 9:
                if not flashed[i][j]:
                    flash(i, j, board)
                    changed = True
    return changed
BOLD = '\033[1m'
END = '\033[0m'
def bprint(board):
    global flashed
    if args.test:
        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if flashed[i][j]:
                    print(f"{BOLD}{c}{END}",end='')
                else:
                    print(c,end='')
            print('')
global count
count=0

def flash(y, x, b):
    global count
    count+=1
    # dprint(f"Flashing {x,y} {b[y][x]}")
    global flashed
    flashed[y][x]=True
    # End of row

    rend = (x == len(b[0])-1)
    rbeg = (x == 0)
    cend = (y == len(b)-1)
    cbeg = (y == 0)
    if not cbeg:
        b[y-1][x]+=1 #N
        if not rend:
            b[y-1][x+1]+=1 #NE
    if not rend:
        b[y][x+1]+=1 #E
        if not cend:
            b[y+1][x+1]+=1 #SE
    if not cend:
        b[y+1][x]+=1 #S
        if not rbeg:                
            b[y+1][x-1]+=1 #SW
    if not rbeg:
        b[y][x-1]+=1 # W
        if not cbeg:
            b[y-1][x-1]+=1#NW

def inc(board):
    dprint("incrementing")
    for i, r in enumerate(board):
        board[i] = list(map(plus, r))
    bprint(board)


def plus(x):
    x += 1
    return x


def main():
    DAYS=100
    global flashed
    flashed = [[False]*SIZE for i in range(SIZE)]
    input = getInput()
    b = get_board(input)
    bprint(b)
    for i in range(DAYS):
        flashed = [[False]*SIZE for i in range(SIZE)]
        step(b)
    print(count)


main()
