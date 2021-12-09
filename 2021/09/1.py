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


def get_board(input):
    board = []
    for line in input:
        board.append(list(line))
    dprint(board)
    return board


def check(x, y, b):
    n = int(b[y][x])
    if x == len(b[0])-1:
        r = 10
    else:
        r = int(b[y][x+1])

    if x == 0:
        l = 10
    else:
        l = int(b[y][x-1])

    if y == 0:
        u = 10
    else:
        u = int(b[y-1][x])

    if y == len(b)-1:
        d = 10
    else:
        d = int(b[y+1][x])
    dprint(f"n:{n} u:{u} d:{d} l:{l} r:{r}")
    return n < u and n < l and n < d and n < r


def get_lows(b):
    risk = 0
    r = len(b)
    c = len(b[0])
    for i in range(r):
        for j in range(c):
            if check(j,i, b):
                dprint(int(b[i][j]))
                risk += int(b[i][j]) + 1
    return risk

def dprint(msg):
    if args.test:
        print(msg)


def main():
    input = getInput()
    board = get_board(input)
    print( get_lows(board))


main()
