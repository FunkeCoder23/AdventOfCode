def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()

def get_sq_ft(dim):
    (l,w,h)=dim.split('x')
    sqft = 2*int(l)*int(w) + 2*int(w)*int(h) + 2*int(h)*int(l)
    smol_side=min(int(l)*int(w),int(w)*int(h),int(h)*int(l))
    return sqft + smol_side

def advent():
    inp = getInput()
    sqft = 0
    for dim in inp:
        sqft += get_sq_ft(dim)
    print(sqft)


advent()