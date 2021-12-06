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

if args.test:
    SIZE=10
else:
    SIZE=1000

board = [ [0]*SIZE for i in range(SIZE)]

def make_line(x1,y1,x2,y2):
    if x1==x2:
        # print (" x matches ")
        (y1,y2)=sort(y1,y2)
        for y in range (y1, y2+1):
            # print(f"marking {x1},{y}")
            board[y][x1]+=1
            # print_board()

    elif y1==y2:
        (x1,x2)=sort(x1,x2)
        # print("y matches")
        for x in range (x1, x2+1):
            # print(f"marking {x},{y1}")
            board[y1][x]+=1
            # print_board()

def sort(x1,x2):
    if x1 > x2:
        x=x1
        x1=x2
        x2=x
    return (x1,x2)

def make_diagonal(x1,y1,x2,y2):
    print((x1,y1,x2,y2))
    if abs(x1-x2)==abs(y1-y2):
        x=x1
        y=y1
        if(x2>x1):
            x2+=1
        else:
            x2-=1
        while x != x2:
            # print(f"diagonal from {x1}{y1} to {x2}{y2} ")
            # print(f"marking {x},{y}")
            
            board[y][x]+=1
            if (x1 < x2):
                x+=1
            else:
                x-=1
            
            if (y1 < y2):
                y +=1
            else:
                y-=1
        # print("")
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
        make_diagonal(x1,y1,x2,y2)
    print_board()
    print(count_board())

main()