DEBUG = True
DEBUG = False


def dprint(*msg):
    if DEBUG:
        for arg in msg:
            print(arg, end=" ")
        print("")


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


# def getInput(file="test_input"):
def getInput():
    if DEBUG:
        file = "test_input"
    else:
        file = "input"
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


SIZE = 0
VISIBLE = [[False for i in range(SIZE)] for i in range(SIZE)]


def get_score(r, c, rows, cols, forest):
    global SIZE
    tree = int(forest[r][c])
    up = down = left = right = 1
    if r == 0 or r == SIZE - 1 or c == 0 or c == SIZE - 1:
        return 0
    dprint("Tree:  ", tree)
    #TODO count trees between tree and blocking tree
    for i in range(r - 1, -1, -1):
        col_u = cols[c][i:r]
        if tree <= max(col_u) or i == 0:
            dprint("Up:    ", col_u)
            up = len(col_u)
            break

    for i in range(c - 1, -1, -1):
        row_l = rows[r][i:c]
        if tree <= max(row_l) or i == 0:
            dprint("Left:  ", row_l)
            left = len(row_l)
            break

    for i in range(r + 1, SIZE):
        col_d = cols[c][r + 1:i + 1]
        if tree <= max(col_d) or i == SIZE - 1:
            dprint("Down:  ", col_d)
            down = len(col_d)
            break

    for i in range(c + 1, SIZE):
        row_r = rows[r][c + 1:i + 1]
        if tree <= max(row_r) or i == SIZE - 1:
            dprint("Right: ", row_r)
            right = len(row_r)
            break

    score = up * left * down * right
    dprint(f"{tree}({r},{c})\n", up, left, down, right, "=", score, '\n')
    return score


def is_visible(forest):
    rows = make_rows(forest)
    cols = make_columns(forest)
    tree_scores = []
    for r, row in enumerate(rows):
        for c, col in enumerate(cols):
            tree_scores.append(get_score(r, c, rows, cols, forest))
    print(max(tree_scores))


def advent():
    global SIZE
    forest = getInput()
    SIZE = len(forest)
    is_visible(forest)
    # for v in VISIBLE:
    # dprint(v)
    pass


advent()
