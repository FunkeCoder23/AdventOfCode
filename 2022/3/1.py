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
    
def unpack(sack):
    spl = int(len(sack)/2)
    one = set(c for c in sack[:spl])
    two = set(c for c in sack[spl:])
    shr = one.intersection(two)
    return get_priority(shr.pop())

def advent():
    inp = getInput()
    total = 0
    for sack in inp:
        total += unpack(sack)
    print(total)
    pass


advent()
