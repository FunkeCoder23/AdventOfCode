def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


WIRES = {}


def get_wires(inp):
    for inst in inp:
        wire = inst.split()[-1]
        WIRES.update({wire: inst.split('->')[0].split()})


def emulate(wire):
    inst = WIRES[wire]
    print(inst)
    typ = len(inst)
    if typ == 1:
        first = inst[0]
        if first in WIRES.keys():
            val = emulate(first)
        else:
            val = int(first)
    elif typ == 2:
        first = inst[1]
        if first in WIRES.keys():
            val = emulate(first)
        else:
            val = int(first)
        val = ~val & 65535
        WIRES.update({wire: val})
    if typ == 3:
        first = inst[0]
        cmd = inst[1]
        second = inst[2]
        if first in WIRES.keys():
            val1 = emulate(first)
        else:
            val1 = int(first)
        if second in WIRES.keys():
            val2 = emulate(second)
        else:
            val2 = int(second)

        if cmd == "AND":
            val = val1 & val2
        elif cmd == "OR":
            val = val1 | val2
        elif cmd == "LSHIFT":
            val = val1 << val2
        elif cmd == "RSHIFT":
            val = val1 >> val2
        val = val & 65535
    WIRES.update({wire: [val]})
    return val


def advent():
    inp = getInput()
    get_wires(inp)
    WIRES.update({'b':[46065]})
    wire = 'a'
    ans = emulate(wire)
    print(ans)
    pass


advent()
