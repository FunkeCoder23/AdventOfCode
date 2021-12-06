#!python.exe
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument(
    '-t', '--test', help="Run with test input", action='store_true')
args = parser.parse_args()


def getInput(file="input"):
    path=sys.path[0]
    if args.test:
        file = "test_input"
    with open(f"{path}/{file}", "r") as f:
        lines = f.read()
        return lines.splitlines()


def split_pair(line):
    pairs=line.split('->')
    pair1 = pairs[0].split(',')
    pair2 = pairs[1].split(',')
    x1=int(pair1[0])
    x2=int(pair2[0])
    y1=int(pair1[1])
    y2=int(pair2[1])
    return(x1,y1,x2,y2)

SIZE=1000
board = [ [0]*SIZE for i in range(SIZE)]

def make_line(x1,y1,x2,y2):
    if x1==x2:
        # print (" x matches ")
        if y1 > y2:
            y=y1
            y1=y2
            y2=y
        for y in range (y1, y2+1):
            # print(f"marking {x1},{y}")
            board[y][x1]+=1
            # print_board()

    elif y1==y2:
        # print(x1, x2)
        if x1 > x2:
            x=x1
            x1=x2
            x2=x
            # print(x1, x2)
        # print("y matches")
        for x in range (x1, x2+1):
            # print(f"marking {x},{y1}")
            board[y1][x]+=1
            # print_board()

        
def print_board():
    for line in board:
        print(line)

def count_board():
    count=0
    for line in board:
        for num in line:
            if num > 1:
                count+=1
    return count


def main():
    input = getInput()
    for line in input:
        
        (x1,y1,x2,y2)=split_pair(line)
        # print(split_pair(line))
        make_line(x1,y1,x2,y2)
    
    print_board()
    print(count_board())

main()