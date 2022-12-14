def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()

global x
global y
global houses
houses = {}
x=0
y=0


def drop_present(dir):
    global x, y, houses
    try:
        houses.update({(x,y):houses[(x,y)]+1})
    except:
        houses.update({(x,y):1})
    if dir == '^':
        y+=1
    elif dir == 'v':
        y-=1
    elif dir =='<':
        x-=1
    elif dir =='>':
        x+=1

def advent():
    inp = getInput()[0]
    for dir in inp:
        drop_present(dir)
    print(len(houses))
    


advent()