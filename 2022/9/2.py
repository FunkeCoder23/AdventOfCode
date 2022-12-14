DEBUG = True

if DEBUG:
    SIZE = 6
else:
    SIZE = 1000


class knot():

    def __init__(self, name):
        self.x = int(SIZE / 2)
        self.y = int(SIZE / 2)
        self.name = name
        self.visited = set((self.x, self.y))

    def move(self, x, y):
        self.x = x
        self.y = y
        self.visited.append((self.x, self.y))

    def move_dir(dir):
        if dir == "up":
            move(self.x,self.y+1)
        if dir == "down":
            move(self.x,self.y-1)
        if dir == "left":
            move(self.x-1,self.y)
        if dir == "right":
            move(self.x+1,self.y)
            


KNOTS = [
    knot("H"),
    knot(1),
    knot(1),
    knot(2),
    knot(3),
    knot(4),
    knot(5),
    knot(6),
    knot(7),
    knot(8),
    knot(9),
    knot('T'),
]


def dprint(*values: object, sep="", end="\n"):
    if DEBUG:
        for value in values:
            print(value, sep=sep, end="")
        print("", end=end)


SX = SY = int(SIZE / 2)
VISITED = [[0 for i in range(SIZE)] for i in range(SIZE)]
VISITED[SX][SY] = 1


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def check_bounds(x):
    return x >= 0 and x < SIZE


def pretty_print():
    if not DEBUG: return
    global HX, HY, TX, TY
    for y in reversed(range(len(VISITED))):
        for x in range(len(VISITED[0])):
            if (x, y) == (HX, HY):
                sym = "H"
            elif (x, y) == (TX, TY):
                sym = "T"
            elif (x, y) == (SX, SY):
                sym = "s"
            else:
                sym = '.'
            dprint(sym, end="")
        dprint("")
    dprint("")


def mark(x, y):
    global VISITED
    VISITED[x][y] = 1


def hamming_dist(a: knot, b: knot):
    if a = None:
        return
    ham = abs(a.x - b.x) > 1 or abs(a.y - b.y) > 1
    # dprint(f"H: {HX},{HY}\nT: {TX},{TY}\nham:{ham}")
    return ham

def getInput():
    if DEBUG:
        file = "test_input"
    else:
        file = "input"

    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


def move(inp):
    MOVES = {
        "U": up,
        "L": left,
        "D": down,
        "R": right,
    }
    mov, amt = inp.split()
    dprint(f"== {inp} ==\n")
    for i in range(int(amt)):
        MOVES[mov]()
        pretty_print()


def advent():
    inp = getInput()
    # pretty_print()
    for mov in inp:
        move(mov)
    print(sum(sum(V) for V in VISITED))
    pass


advent()
