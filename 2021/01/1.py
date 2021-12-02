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


def main():
    input = getInput()

    decreased = increased = equal = 0
    prevNum=nextNum=None
    for line in input:
        nextNum = int(line)

        if prevNum is None:
            prevNum = nextNum
            if args.test: 
                print(line + " (N/A - no previous measurement)")
            continue

        if nextNum < prevNum:
            decreased += 1
            if args.test:
                print(line + " (decreased)")

        elif nextNum > prevNum:
            increased += 1
            if args.test: 
                print(line + " (increased)")
        else:
            equal += 1

        prevNum=nextNum
    print( increased)

main()