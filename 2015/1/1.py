def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


def advent():
    inp = getInput()[0]
    up = inp.count('(')
    print(up)
    down=inp.count(')')
    print(down)
    print(up-down)


advent()