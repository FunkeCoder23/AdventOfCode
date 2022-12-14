DEBUG = True

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


def parse_list(line):
    


def get_packet(line):
    packet=[]
    for c in line:
        if c = '[':
            l, line =line.split(']', 1)
            parse_list(l)
            

def advent():
    inp = getInput()
    
    pass


advent()
