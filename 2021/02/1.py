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

depth=0
position=0

def forward(num):
    global position
    if args.test:
        print(f"Adding {num} to position")
    position +=num

def down(num):
    global depth
    if args.test:
        print(f"Adding {num} to depth")
    depth += num

def up(num):
    global depth
    if args.test:
        print(f"Decreasing {num} from depth")
    depth -= num



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
    print(depth*position)

main()