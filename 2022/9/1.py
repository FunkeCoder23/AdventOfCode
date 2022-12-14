DEBUG = True

if DEBUG:
    SIZE = 6
else:
    SIZE = 1000



def dprint(*values: object, sep="", end="\n"):
    if DEBUG:
        for value in values:
            print(value, sep=sep, end="")
        print("", end=end)


HX = HY = TX = TY = SX = SY = int(SIZE / 2)
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


def hamming_dist(x1, y1, x2, y2):
    ham = abs(x1 - x2) > 1 or abs(y1 - y2) > 1
    # dprint(f"H: {HX},{HY}\nT: {TX},{TY}\nham:{ham}")
    return ham


def up():
    global HX, HY, TX, TY
    OY = HY
    if check_bounds(HY + 1):
        HY += 1
        if hamming_dist():
            TX = HX
            TY = OY
        mark(TX, TY)
    else:
        print("Invalid up")
        exit()


def left():
    global HX, HY, TX, TY
    OX = HX
    if check_bounds(HX - 1):
        HX -= 1
        if hamming_dist():
            TX = OX
            TY = HY
        mark(TX, TY)
    else:
        print("Invalid left")
        exit()


def down():
    global HX, HY, TX, TY
    OY = HY
    if check_bounds(HY - 1):
        HY -= 1
        if hamming_dist():
            TX = HX
            TY = OY
        mark(TX, TY)
    else:
        print("Invalid down")
        exit()


def right():
    global HX, HY, TX, TY
    OX = HX
    if check_bounds(HX + 1):
        HX += 1
        if hamming_dist():
            TX = OX
            TY = HY
        mark(TX, TY)
    else:
        print("Invalid right")
        exit()


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
