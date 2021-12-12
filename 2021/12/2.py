#!python.exe
import argparse
import sys
from copy import deepcopy
parser = argparse.ArgumentParser()
parser.add_argument(
    '-t', '--test', help="Run with test input", action='store_true')
args = parser.parse_args()


def is_valid(i, j, b):
    rows = len(b[0])
    cols = len(b)
    return (i >= 0 and i < rows and j >= 0 and j < cols)


def getInput(file="input"):
    path = sys.path[0]
    if args.test:
        file = "test_input"
    with open(f"{path}/{file}", "r") as f:
        lines = f.read()
        return lines.splitlines()


def dprint(msg):
    if args.test:
        print(str(msg))


def big(n: str):
    return n.isupper()

def small_visit(p:list):
    for c in p:
        if c.isupper():
            continue
        if p.count(c)>1:
            return True
    return False

def small(n: str, p: list):
    if (n=="start"):
        return False
    s = n.islower() 
    v = small_visit(p)
    return(s and not v)


class Caves:
    def __init__(self):
        self.paths = []

    def findPaths(self, s, d, g):
        path = []
        path.append(s)
        self.dfs(s, d, g, path)
        return len(self.paths)

    def dfs(self, s, d, g, path):
        if s == d:
            dprint(','.join(path))
            self.paths.append(deepcopy(path))
        else:
            for n in g[s]:
                dprint(path)
                if n not in path or big(n) or small(n, path):
                    path.append(n)
                    self.dfs(n, "end", g, path)
                    path.pop()


def main():
    graph = {"start": []}
    input = getInput()
    caves = []
    for l in input:
        n = l.split('-')
        caves.append(n[0])
        caves.append(n[1])
    for n in set(caves):
        graph.update({n: []})
    for l in input:
        n = l.split('-')
        a = n[0]
        b = n[1]
        graph[a].append(b)
        graph[b].append(a)
    dprint(graph)
    c = Caves()
    print(c.findPaths("start", "end", graph))


main()
