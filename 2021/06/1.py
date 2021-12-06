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
    def __init__(self,timer=8):
        self.timer=timer

    def tic(self):
        self.timer-=1
    
    def check_preg(self):
        if self.timer < 0:
            self.reset()
            return self.spawn()

    def reset(self):
        self.timer=6

    def get_timer(self):
        return self.timer

    def spawn(self):
        return Lanternfish()

DAYS=80

def main():
    input = getInput()
    init = [int(i) for i in input[0].split(',')]
    fish=[]
    
    for i in init:
        fish.append(Lanternfish(i))

    for i in range(DAYS):
        new_fish = []
        for f in fish:
            f.tic()
            if f.check_preg():
                new_f=f.spawn()
                new_fish.append(new_f)
                # print(f"{new_f.get_timer()},",end='')
                f.reset()
            # print(f"{f.get_timer()},",end='')
            
        fish.extend(new_fish)
        # print("")
    print(len(fish))
    
    



main()