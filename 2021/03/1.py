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

def split(word):
    return [c for c in word]

def main():
    
    input = getInput()
    bitsize=len(input[0])
    
    eps=''
    gam=''

    ones=[0]*bitsize
    zeros=[0]*bitsize

    for line in input:
        nums=split(line)
        for (count, bit) in enumerate(nums):
            if bit == '0':
                zeros[count]+=1
            else:
                ones[count]+=1
    for i in range(bitsize):
        if ones[i] > zeros[i]:
            gam+='1'
            eps+='0'
        else:
            eps+='1'
            gam+='0'
    print(gam)
    print(eps)
    gam=int(gam,2)
    eps=int(eps,2)
    print(gam)
    print(eps)
    print(eps*gam)

main()