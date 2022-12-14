def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

# def getInput(file="test_input"):
def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


def find_marker(line):
    markers = []
    for idx,c in enumerate(line):
        if len(markers) == 14:
            return idx
        while c in markers:
            markers.pop(0)
        markers.append(c)
        
        
def advent():
    inp = getInput()
    print(find_marker(inp[0]))


advent()