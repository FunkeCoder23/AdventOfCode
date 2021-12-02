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
    nextWin=[]
    prevSum=nextSum=0
    for (count,line) in enumerate(input):
        # init with 2 nums
        if count < 2:
            nextWin.append(int(line))
            continue
        # add 3rd num to window
        nextWin.append(int(line))
        # Get new total
        nextSum=sum(nextWin)          

        # if no prev sum, first window
        if prevSum == 0:
            if args.test: 
                print(f"{nextSum} (N/A - no previous measurement)")

        # if decreased
        elif nextSum < prevSum:
            decreased += 1
            if args.test:
                print(f"{nextSum} (decreased)")

        # if increased
        elif nextSum > prevSum:
            increased += 1
            if args.test: 
                print(f"{nextSum} (increased)")

        # if equal
        else:
            equal += 1
            if args.test: 
                print(f"{nextSum} (no change)")

        # set prev values
        prevSum = nextSum
        nextWin.pop(0)


    print( increased)

main()