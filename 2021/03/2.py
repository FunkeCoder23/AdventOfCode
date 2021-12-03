#!python.exe
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument(
    '-t', '--test', help="Run with test input", action='store_true')
args = parser.parse_args()


def getInput(file="input"):
    path = sys.path[0]
    if args.test:
        file = "test_input"
    with open(f"{path}/{file}", "r") as f:
        lines = f.read()
        return lines.splitlines()


def split(word):
    return [c for c in word]


def main():

    input = getInput()
    bitsize = len(input[0])
    oxylines = input
    colines = input


    ones = [0]*bitsize
    zeros = [0]*bitsize

    for i in range(bitsize):
        zerolines=[]
        onelines=[]
        # print(f"OXYLINES\n{oxylines}")
        for line in oxylines:
            nums = split(line)
            bit = nums[i]
            if bit == '0':
                zeros[i] += 1
                zerolines.append(line)
            else:
                ones[i] += 1
                onelines.append(line)
        if ones[i] >= zeros[i]:
            oxylines=onelines
        else:
            oxylines=zerolines

    ones = [0]*bitsize
    zeros = [0]*bitsize
    for i in range(bitsize):
        if len(colines) ==1:
            break
        zerolines=[]
        onelines=[]
        print(f"CO2lines\n{colines}")
        for line in colines:
            nums = split(line)
            bit = nums[i]
            if bit == '0':
                zeros[i] += 1
                zerolines.append(line)
            else:
                ones[i] += 1
                onelines.append(line)
        print(zeros)
        print(ones)
        if zeros[i] < ones[i]:
            print("Less Zeros in ",i)
            colines=zerolines
        elif zeros[i] == ones[i]:
            print("Equal in ",i)
            colines=zerolines
        else:
            print("Less Ones in ",i)
            colines=onelines

    print(colines)
    print(oxylines)
    oxy = int(oxylines[0], 2)
    co = int(colines[0],2)
    print(oxy*co)


main()
