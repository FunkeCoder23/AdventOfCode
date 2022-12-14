def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


def advent():
    inp = getInput()
    string_chars = mem_used = 0
    for i in inp:
        enc = i.encode().decode('unicode_escape')
        string_chars += len(i)
        mem_used += len(enc) - 2
    print(string_chars - mem_used)
    pass


advent()
