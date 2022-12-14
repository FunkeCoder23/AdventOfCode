def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


LIGHTS = [[False for i in range(1000)] for i in range(1000)]


def do_lights(line):
    cmd, start, null, end = line.split()
    start_x,start_y = [int(i) for i in start.split(',')]
    end_x,end_y =[int(i) for i in end.split(',')]
    for y in range(start_y,end_y+1):
        for x in range(start_x,end_x+1):
            if cmd == "on":
                LIGHTS[y][x]=True
            elif cmd == "off":
                LIGHTS[y][x]=False
            elif cmd == "toggle":
                LIGHTS[y][x]=not LIGHTS[y][x]                


def advent():
    inp = getInput()
    for line in inp:
        do_lights(line)
    light_count = 0
    for row in LIGHTS:
        light_count+=row.count(True)
    print(light_count)
    pass


advent()
