#!python.exe
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument(
    '-t', '--test', help="Run with test input", action='store_true')
args = parser.parse_args()

def is_valid(i,j,b): 
    rows = len(b[0])
    cols = len(b)
    return (i>=0 and i <rows and j>=0 and j<cols)


def dprint2d(b):
    if args.test:
        for i in b:
            print(i)
            
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

class Something:
    def __init__(self):
        pass
    
    

def main():
    input = getInput()


main()