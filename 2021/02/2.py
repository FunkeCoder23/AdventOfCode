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

aim=0
depth=0
position=0

def forward(num):
    global position, aim, depth
    if args.test:
        print(f"Adding {num} to position")
        print(f"Adding {num*aim} to depth")
    
    position +=num

    depth+=(num*aim)

def down(num):
    global position, aim, depth
    if args.test:
        print(f"Adding {num} to aim")
    aim += num

def up(num):
    global position, aim, depth
    if args.test:
        print(f"Decreasing {num} from aim")
    aim -= num



DIRECTIONS={
    "forward":forward,
    "down":down,
    "up":up
}

def main():
    input = getInput()
    for line in input:
        if args.test:
            print(line)
        arg=line.split(" ")

        dir = arg[0]
        num = int(arg[1])
        DIRECTIONS[dir](num)
    print(position*depth)

main()