def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


def get_sq_ft(dim):
    (l, w, h) = dim.split('x')
    smol_perim = min(int(l) * int(w), int(w) * int(h), int(h) * int(l))
    smol_side = min(int(l), int(h), int(w))
    smol_side_2 = int(smol_perim / smol_side)
    tot = (2 * smol_side) + (2 * smol_side_2) + (int(l) * int(h) * int(w))
    return tot


def advent():
    inp = getInput()
    sqft = 0
    for dim in inp:
        sqft += get_sq_ft(dim)
    print(sqft)


advent()