#!python.exe
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument(
    '-t', '--test', help="Run with test input", action='store_true')
args = parser.parse_args()

count=0

def getInput(file="input"):
    path=sys.path[0]
    if args.test:
        file = "test_input"
    with open(f"{path}/{file}", "r") as f:
        lines = f.read()
        return lines.splitlines()



class Lanternfish:

    def __init__(self):
        self.timers=[0]*9

    def add(self,timer=8):
        self.timers[timer]+=1

    def tic(self):
        preg=self.timers.pop(0)
        self.timers.append(preg)
        self.timers[6]+=preg

    def get_timers(self):
        return self.timers


    def __repr__(self):
        return str(self.timers)
    
DAYS=256

def main():
    input = getInput()
    init = [int(i) for i in input[0].split(',')]
    fish=Lanternfish()

    for f in init:
        fish.add(f)
    print(repr(fish))

    for i in range(DAYS):
        fish.tic()
        print(repr(fish))

    print(sum(fish.get_timers()))


    



main()