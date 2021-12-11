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
SCORE = [3, 2, 1, 4]
PAIRS = list(zip(OPENINGS, CLOSINGS))


def match_brace(o, c):
    # dprint(o)
    i = OPENINGS.index(o)
    if c in PAIRS[i]:
        return True
    else:
        return False


def get_openings(line):
    score = 0
    o = []
    for c in line:
        if c in OPENINGS:
            o.append(c)
        elif c in CLOSINGS:
            t = o.pop(-1)
            if not match_brace(t, c):
                return score
    o.reverse()
    dprint(o)
    for t in o:
        score *= 5
        score += SCORE[OPENINGS.index(t)]
        dprint(score)
    return score


def main():
    scores = []
    input = getInput()
    for line in input:
        score = get_openings(line)
        if score != 0:
            scores.append(int(score))
        dprint(scores)
    scores.sort()
    dprint(scores)
    print(scores[int(len(scores)/ 2)] )


main()
