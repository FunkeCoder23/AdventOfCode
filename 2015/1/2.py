def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


def advent():
    inp = getInput()[0]
    floor = 0
    for num,c in enumerate(inp,1):
        if c == '(':
            floor +=1
        elif c==')':
            floor -=1
        if floor == -1:
            print(num)
            exit()
    pass


advent()