def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


# def getInput(file="test_input"):
def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


STACKS = [[] for i in range(10)]


def init_crates(inp):
    for line_num, line in enumerate(inp):
        if line.strip() == "":
            return line_num
        else:
            crates = chunks(line, 4)
            for i, crate in enumerate(crates,1):
                if crate.strip() == "":
                    continue
                letter = crate[1:2]
                try:
                    int(letter)
                    continue
                except:
                    STACKS[i].insert(0, letter)
                    # print(letter)


def move(action):
    mov, times, frm, start, to, finish = action.split()
    times = int(times)
    start = int(start)
    finish = int(finish)
    l=[]
    for i in range(times):
        l.insert(0,STACKS[start].pop(-1))
    STACKS[finish]+=l
        # print(f"moved {l} from {start} to {finish}")
    # for stack in STACKS:
        # print(stack)
    # print('\n')


def advent():
    inp = getInput()
    moves_start = init_crates(inp)
    print("\nbefore")
    # for stack in STACKS:
        # print(stack)
    for action in inp[moves_start+1:]:
        if action.split()[0] != "move":
            continue
        move(action)

    print("\nafter")
    # for stack in STACKS:
        # print(stack)
    for stack in STACKS[1:]:
        if len(stack) >0:
            print(stack[-1], end='')
    print('')


advent()
