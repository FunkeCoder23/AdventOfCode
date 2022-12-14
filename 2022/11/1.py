DEBUG = False


class Monkey():

    def __init__(self, num):
        self.num = num
        self.items = []
        self.divby = 1
        self.arg1 = ""
        self.op = ""
        self.arg2 = ""
        self.truethrow = num
        self.falsethrow = num
        self.inspected = 0

    def __str__(self):
        return f"""
        Monkey {self.num}
        Items: {self.items}
        divisible by {self.divby}
        new = {self.arg1} {self.op} {self.arg2}
        If true: {self.truethrow}
        If False: {self.falsethrow}
        """

    def set_items(self, start):
        items = start.split(":")[1]
        items = items.split(",")
        for item in items:
            self.items.append(int(item))

    def set_op(self, op):
        args = op.split(" ")
        self.arg1 = args[3]
        self.op = args[4]
        self.arg2 = args[5]

    def set_div_by(self, test):
        args = test.split(" ")
        self.divby = int(args[3])

    def set_true_throw(self, throw):
        args = throw.split(" ")
        self.truethrow = int(args[5])

    def set_false_throw(self, throw):
        args = throw.split(" ")
        self.falsethrow = int(args[5])

    def test(self):
        self.inspected += 1
        old = self.items.pop(0)
        if self.arg1 == "old":
            arg1 = old
        else:
            arg1 = int(self.arg1)

        if self.arg2 == "old":
            arg2 = old
        else:
            arg2 = int(self.arg2)

        if self.op == "+":
            new = arg1 + arg2
        elif self.op == "*":
            new = arg1 * arg2

        new = new // 3
        return new, new % self.divby == 0

    def throw(self):
        item, res = self.test()
        if res == True:
            return item, self.truethrow
        else:
            return item, self.falsethrow

    def catch(self, item):
        self.items.append(item)


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


MONKEYS = []


def parseMonkeys(inp):
    global MONKEYS
    num = -1
    for line in inp:
        line = line.lstrip()
        if line.startswith("Monkey"):
            num += 1
            MONKEYS.append(Monkey(num))
        elif line.startswith("Starting"):
            MONKEYS[num].set_items(line)
        elif line.startswith("Operation"):
            MONKEYS[num].set_op(line)
        elif line.startswith("Test"):
            MONKEYS[num].set_div_by(line)
        elif line.startswith("If true"):
            MONKEYS[num].set_true_throw(line)
        elif line.startswith("If false"):
            MONKEYS[num].set_false_throw(line)
    # print("Start")
    # for m in MONKEYS:
        # print(m)

def get_inspected():
    global MONKEYS
    inspected = []
    for m in MONKEYS:
        inspected.append(m.inspected)
    print(inspected)
    top=sorted(inspected, reverse=True)[:2]
    print(top[0]*top[1])
    
def advent():
    global MONKEYS
    inp = getInput()
    parseMonkeys(inp)
    for round in range(20):
        for monkey in MONKEYS:
            while len(monkey.items) > 0:
                item, to = monkey.throw()
                MONKEYS[to].catch(item)
        # print("Round", round+1)
        # for m in MONKEYS:
            # print(m)
    get_inspected()
    pass


advent()
