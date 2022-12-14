def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


LIGHTS = [[0 for i in range(1000)] for i in range(1000)]


def do_lights(line):
    cmd, start, null, end = line.split()
    start_x, start_y = [int(i) for i in start.split(',')]
    end_x, end_y = [int(i) for i in end.split(',')]
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            if cmd == "on":
                LIGHTS[y][x] += 1
            elif cmd == "off":
                LIGHTS[y][x] = (LIGHTS[y][x] - 1) if LIGHTS[y][x] > 0 else 0
            elif cmd == "toggle":
                LIGHTS[y][x] += 2


def advent():
    inp = getInput()
    for line in inp:
        do_lights(line)
    light_count = sum(sum(row) for row in LIGHTS)
    print(light_count)
    pass


advent()
