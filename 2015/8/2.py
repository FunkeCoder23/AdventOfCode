def getInput(file="test_input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


def advent():
    inp = getInput()
    string_chars = mem_used = 0
    for i in inp:
        #enc = i.encode().decode('unicode_escape')
        
        enc = i.encode().decode('unicode_escape')#[1:]#.encode().decode('unicode_escape')
        print(len(enc), enc)
        print(len(i), i)
        # string_chars += len(i)
        # mem_used += len(enc) - 2
    # print(string_chars - mem_used)
    pass


advent()
