#!python.exe
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument(
    '-t', '--test', help="Run with test input", action='store_true')
args = parser.parse_args()


def dprint(msg):
    if args.test:
        print(msg)
        
def getInput(file="input"):
    path=sys.path[0]
    if args.test:
        file = "test_input"
    with open(f"{path}/{file}", "r") as f:
        lines = f.read()
        return lines.splitlines()

def get_min_fuel(input):
    poss=input.split(',')
    mins=[0]*len(poss)
    for l in range(len(poss)):
        for p in poss:
            # dprint(p,"-",l, "=",abs(int(p)-(l+1)) )
            mins[l]+=abs(int(p)-(l+1))
        dprint(mins[l])
        dprint("")
    dprint(mins)
    print(min(mins))

def main():
    input = getInput()
    get_min_fuel(input[0])


main()