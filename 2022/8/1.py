DEBUG = True


def dprint(*msg):
    if DEBUG:
        for arg in msg:
            print(arg, end=" ")
        print("")


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


# def getInput(file="test_input"):
def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


def make_rows(forest):
    rows = [[] for row in forest]
    for i, row in enumerate(forest):
        rows[i] = [int(t) for t in row]
    return rows


def make_columns(forest):
    columns = [[] for row in forest]
    for row in forest:
        for col in range(len(forest)):
            columns[col].append(int(row[col]))
    return columns


SIZE = 99
VISIBLE = [[False for i in range(SIZE)] for i in range(SIZE)]


def is_visible(forest):
    rows = make_rows(forest)
    cols = make_columns(forest)

    for r, row in enumerate(rows):
        for c, col in enumerate(cols):
            tree = int(rows[r][c])
            # Outside Edge
            if r == 0 or r == SIZE - 1 or c == 0 or c == SIZE - 1:
                VISIBLE[r][c] = True
                continue
            #Left to Right
            if tree > max(rows[r][c + 1:]):
                # dprint(r, c, "is visible from right")
                VISIBLE[r][c] = True
            # else:
            # dprint(r, c, "is not visible from right", rows[r][c+1:])
            #Right to Left
            if tree > max(rows[r][:c]):
                # dprint(r, c, "is visible from left")
                VISIBLE[r][c] = True
            # else:
            # dprint(r, c, "is not visible from left", rows[r][:c])

            #Top Down
            if tree > max(cols[c][:r]):
                # dprint(r, c, "is visible from top")
                VISIBLE[r][c] = True
            # else:
            # dprint(r, c, "is not visible from top", cols[c][:r])  #Bottom up
            #Bottom up
            if tree > max(cols[c][r + 1:]):
                # dprint(r, c, "is visible from bottom")
                VISIBLE[r][c] = True
            # else:
            # dprint(r, c, "is not visible from bottom",
            # cols[c][r+1:])
            # dprint("")


def advent():
    forest = getInput()
    is_visible(forest)
    # for v in VISIBLE:
    # dprint(v)
    dprint(sum(sum(r) for r in VISIBLE))
    pass


advent()
