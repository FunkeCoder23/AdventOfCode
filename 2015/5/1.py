def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


def is_nice(word: str):
    if word.count("ab") > 0: return 0
    if word.count("cd") > 0: return 0
    if word.count("pq") > 0: return 0
    if word.count("xy") > 0: return 0

    vowels = word.count('a')
    vowels += word.count('e')
    vowels += word.count('i')
    vowels += word.count('o')
    vowels += word.count('u')
    if vowels < 3:
        return 0

    for c in range(ord('a'), ord('z') + 1):
        if (word.count(f"{chr(c)}{chr(c)}")) > 0: return 1

    return 0


def advent():
    inp = getInput()
    count=0
    for word in inp:
        count += is_nice(word)
    print(count)


advent()
