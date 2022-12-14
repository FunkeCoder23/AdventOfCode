DEBUG = False


def dprint(msg):
    if DEBUG:
        print(msg)


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def getInput():
    if DEBUG:
        file = "test_input"
    else:
        file = "input"

    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


INSTRS = [1]

def addx(pc, num):
    global INSTRS
    INSTRS.append(0)
    INSTRS.append(num)

def noop(pc):
    global INSTRS
    INSTRS.append( 0)


def advent():
    inp = getInput()
    for pc in range(1,len(inp)+3):
        if pc in range(len(inp)-1):
            inst = inp[pc-1]
            args = inst.split(" ")
            if args[0] == "noop":
                noop(pc)
            elif args[0] == "addx":
                addx(pc, int(args[1]))
        # print(pc, sum(INSTRS[:pc]))
    total_str=0
    for i in [20,60,100,140,180,220]:
        str = sum(INSTRS[:i])*i
        # print(i, str)
        total_str += str
    print(total_str)
    pass


advent()
