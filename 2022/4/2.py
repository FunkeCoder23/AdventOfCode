def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

# def getInput(file="test_input"):
def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()
def get_section(line):
    # print(line)
    elf1,elf2=line.split(',')
    x1,x2 = [int(i) for i in elf1.split('-')]
    set1=set(x for x in range(x1,x2+1))
    x1,x2 = [int(i) for i in elf2.split('-')]
    set2=set(x for x in range(x1,x2+1))
    # print(set1)
    if len(set1.intersection(set2)) > 0:
        return 1
    return 0


def advent():
    inp = getInput()
    subsets=0
    for line in inp:
        subsets+=get_section(line)
    print(subsets)

advent()