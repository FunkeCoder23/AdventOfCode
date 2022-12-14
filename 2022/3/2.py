def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

# def getInput(file="test_input"):
def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()

def get_priority(item):
    if item <= 'Z':
        return ord(item) - (65 - 26 - 1)
    else:
        return ord(item) - 96 
    
def unpack(group):
    one,two,three = (set(g) for g in group)
    print(one,two,three)
    shr = one.intersection(two,three)
    return get_priority(shr.pop())


def advent():
    inp = getInput()
    total = 0
    for group in chunks(inp,3):
        total += unpack(group)
    print(total)
    pass


advent()
