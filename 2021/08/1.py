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
    
def dprint(msg):
    if args.test:
        print(msg)

def parse(input):
    dprint(input)
    inputs=input.split(' | ')[0]
    outputs=input.split(' | ')[1]
    dprint(inputs)
    dprint(outputs)
    inputs=inputs.split(' ')
    outputs=outputs.split(' ')
    dprint(inputs)
    dprint(outputs)
    return(inputs,outputs)

def get_num(wires):
    num = len(wires)
    dprint(num)
    if num == 2: return 1
    if num == 4: return 4
    if num == 3: return 7
    if num == 7: return 8
    else: return 0

    
    
def main():
    input = getInput()
    counts=[0]*10
    for line in input:
        ins,outs=parse(line)
        for out in outs:
            counts[get_num(out)] +=1
    dprint(counts)
    print(counts[1]+counts[4]+counts[7]+counts[8])
main()