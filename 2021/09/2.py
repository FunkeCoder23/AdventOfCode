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


global path


def find_basin(basin, b):
    global path
    path.append(basin)
    size = 1    
    y= basin[0]
    x=basin[1]
    
    # right
    if x != len(b[0])-1:
        basin = [y, x+1]
        # dprint(basin)
        r = int(b[y][x+1])
        if r != 9 and basin not in path:
            dprint("right")
            size += find_basin(basin, b)

    if x != 0:
        basin=[y, x-1]
        dprint(basin)
        l = int(b[y][x-1])
        if l != 9 and basin not in path:
            dprint("left")
            size += find_basin(basin, b)

    if y != 0:
        basin=[y-1, x]
        dprint(basin)
        u = int(b[y-1][x])
        if u != 9 and basin not in path:
            dprint("up")
            size += find_basin(basin, b)

    if y != len(b)-1:
        basin=[y+1, x]
        dprint(basin)
        d = int(b[y+1][x])
        if d != 9 and basin not in path:
            dprint("down")
            size += find_basin(basin, b)
    dprint(path)
    return size


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
    basins = []
    r = len(b)
    c = len(b[0])
    for i in range(r):
        for j in range(c):
            if check(j, i, b):
                basins += [[i, j]]
    dprint(basins)
    return basins


def dprint(msg):
    if args.test:
        print(msg)


def main():
    global path
    input = getInput()
    board = get_board(input)
    basins = get_lows(board)
    sizes=[]
    for b in basins:
        path = []
        size= find_basin(b, board)
        dprint(f"SIZE:{size}")
        sizes.append(size)
    dprint(sizes)
    sizes.sort(reverse=True)
    dprint(sizes)
    mult=1
    for s in sizes[:3]:
        mult *=s
    print(mult)


main()
