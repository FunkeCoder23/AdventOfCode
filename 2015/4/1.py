import hashlib

def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()

def brute_hash(inp):
    for i in range (int(1e6)):
        brute = f"{inp}{i}"
        hash = hashlib.md5(brute.encode())
        if(hash.hexdigest().startswith('00000')):
            print(i)
            return

def advent():
    inp = getInput()[0]
    brute_hash(inp)
    pass


advent()