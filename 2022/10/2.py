DEBUG = False


def dprint(msg):
    if DEBUG:
        print(msg)


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def debug(sprite):
    if DEBUG:
        print("Sprite position: ",end="")
        for i in range(40):
            if i in [sprite - 1, sprite, sprite + 1]:
                print("#", end="")
            else:
                print(".", end="")
        print("")


def light(pc, sprite):
    global CRT
    row = pc // 40
    column = pc % 40
    
    # debug(sum(INSTRS[:pc]))
    # print("Start Cycle   :",pc, end="")
    # if(INSTRS[pc] == 0):
    #     print(" begin executing addx ",INSTRS[pc+1])
    # else:
    #     print("finish executing addx ",INSTRS[pc], f"(Register X is now {sum(INSTRS[:pc])})")
    # print("During Cycle  :",pc)
    # print("Current CRT Row:", ''.join(i for i in CRT[row]))
    # print(row,column)
    if(column==0):
        CRT.append([])
    if column in [sprite - 1, sprite, sprite + 1]:
        CRT[row].append('#')
    else:
        CRT[row].append(' ')
    # print_CRT()


def getInput():
    if DEBUG:
        file = "test_input"
    else:
        file = "input"

    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


INSTRS = [1]
CRT = [[]]


def addx(pc, num):
    global INSTRS
    INSTRS.append(0)
    INSTRS.append(num)


def noop(pc):
    global INSTRS
    INSTRS.append(0)


def print_CRT():
    global CRT
    for row in CRT:
        for c in row:
            print(c, sep="", end="")
        print("")
    print("")


def advent():
    inp = getInput()
    for pc in range(1,241):
        if pc in range(len(inp)-1):
            inst = inp[pc-1]
            args = inst.split(" ")
            if args[0] == "noop":
                noop(pc)
            elif args[0] == "addx":
                addx(pc, int(args[1]))
        light(pc-1, sum(INSTRS[:pc]))
    print_CRT()


advent()
