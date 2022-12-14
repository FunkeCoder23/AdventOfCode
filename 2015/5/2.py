def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


def is_nice(word: str):
    pairs=0
    for i in range(len(word) -1):
        pair=word[i:i+2]
        pair_count=word.count(pair,i+2)
        pairs +=pair_count
    if pairs == 0:
        return 0
             
            
    for i in range(len(word) - 2):
        if word[i]==word[i+2]:
            return 1
    return 0

def advent():
    inp = getInput()
    count=0
    for word in inp:
        count += is_nice(word)
    print(count)


advent()
