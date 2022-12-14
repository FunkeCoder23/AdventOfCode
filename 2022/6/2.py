def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

# def getInput(file="test_input"):
def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


def advent():
    inp = getInput()
    pass


advent()