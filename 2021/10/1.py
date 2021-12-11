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


def dprint(msg):
    if args.test:
        print(msg)


OPENINGS = ['{', '[', '(', '<']
CLOSINGS = ['}', ']', ')', '>']
SCORE = [1197, 57, 3, 25137]
PAIRS=list(zip(OPENINGS,CLOSINGS))


def match_brace(o,c):
    # dprint(o)
    i=OPENINGS.index(o)
    if c in PAIRS[i]:
        return True
    else:
        return False

def get_openings(line):
    global score
    o = []
    for c in line:
        if c in OPENINGS:
            o.append(c)
        elif c in CLOSINGS:
            t=o.pop(-1)
            if not match_brace(t,c):
                dprint(f"Expected {t}, got {c}. SCORE: { SCORE[CLOSINGS.index(c)]}")
                return SCORE[CLOSINGS.index(c)]
    return 0

def main():
    score=0
    input = getInput()
    for line in input:
        score += get_openings(line)
        dprint(score)
    print(score)


main()
