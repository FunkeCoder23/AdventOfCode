def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


global s_x, s_y, r_x, r_y
global houses
houses = {}
s_x = 0
s_y = 0
r_x = 0
r_y = 0


def drop_present(dir):
    global s_x, s_y, houses
    try:
        houses.update({(s_x, s_y): houses[(s_x, s_y)] + 1})
    except:
        houses.update({(s_x, s_y): 1})
    if dir == '^':
        s_y += 1
    elif dir == 'v':
        s_y -= 1
    elif dir == '<':
        s_x -= 1
    elif dir == '>':
        s_x += 1


def drop_present_r(dir):
    global r_x, r_y, houses
    try:
        houses.update({(r_x, r_y): houses[(r_x, r_y)] + 1})
    except:
        houses.update({(r_x, r_y): 1})
    if dir == '^':
        r_y += 1
    elif dir == 'v':
        r_y -= 1
    elif dir == '<':
        r_x -= 1
    elif dir == '>':
        r_x += 1


def advent():
    inp = getInput()[0]
    for turn, dir in enumerate(inp):
        if (turn % 2 == 0):
            drop_present(dir)
        else:
            drop_present_r(dir)
    print(len(houses))


advent()
