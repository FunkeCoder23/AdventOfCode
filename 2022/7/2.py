SCRIPT = []

CUR_DIR = None
DIRS = {'/': {}}
FILEPATH = []
SIZE = 0

SIZED_DIRS = []


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


# def getInput(file="test_input"):
def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


def parse_command(line):
    #print("Executing", line)
    cmds = line.split()
    cmd = cmds[1]
    arg = None
    if len(cmds) == 3:
        arg = cmds[2]
    if cmd == "cd":
        change_dir(arg)
    elif cmd == "ls":
        list_dir()


def list_dir():
    global SCRIPT, CUR_DIR
    #print("list")
    while len(SCRIPT) > 0 and not SCRIPT[0].startswith('$'):
        item = SCRIPT.pop(0)
        if 'dir' in item:
            dir, dirname = item.split()
            #print("adding dir", dirname)
            CUR_DIR.update({dirname: {}})
        else:
            size, file = item.split()
            #print("adding file", file)
            CUR_DIR.update({file: size})


def find_dir(dirs, arg):
    #print(dirs)
    if arg in dirs.keys():
        return dirs
    for dir in dirs.values():
        if type(dirs) is dict:
            find_dir(dir, arg)


def cd():
    global CUR_DIR, DIRS, FILEPATH
    CUR_DIR = DIRS
    for p in FILEPATH:
        CUR_DIR = CUR_DIR[p]
    #print("changing dir to ..\n",FILEPATH[-1])


def change_dir(arg):
    global CUR_DIR, PARENT_DIR, DIRS, FILEPATH
    if arg == "/":
        FILEPATH = ["/"]
        CUR_DIR = DIRS["/"]
        #print("changing dir to",arg)
    elif arg == '..':
        FILEPATH.pop(-1)
        cd()
    else:
        FILEPATH.append(arg)
        #print("changing dir to",arg)
        CUR_DIR = CUR_DIR[arg]


def advent():
    global SCRIPT, DIRS, SIZE
    #print("test")

    SCRIPT = getInput()
    while SCRIPT:
        line = SCRIPT.pop(0)
        if line.strip() == "":
            return
        #print(line)
        parse_command(line)
        #print(f"Current:\n{DIRS}\n")
    # pretty_print(DIRS)
    getsize(DIRS)
    total_size = 0
    sizes=[]
    for d in SIZED_DIRS:
        sizes.append(int(list(d.values())[0]))
        if list(d.keys())[0] == "/":
            # print(d)
            used_space = int(list(d.values())[0])
    left_space = 70000000 - used_space
    need_space = 30000000 - left_space
    # print(used_space, " out of ", 70000000, "Need ", need_space, " out of ", 30000000)
    min_sizes=[]
    for size in sizes:
        if size > need_space:
            min_sizes.append(size)
    # print(min_sizes)
    print(min(min_sizes))

    # print(SIZE)
    # exit()
    

def getsize(dir):
    global SIZED_DIRS
    tmpsize = 0
    added_items = []
    for itemname, item in dir.items():
        if type(item) is dict:
            dirsize = getsize(item)
            tmpsize += dirsize
            SIZED_DIRS.append({itemname: dirsize})
        elif type(item) is str:
            # print("checking ", itemname, item)
            tmpsize += int(item)
            added_items.append(itemname)
        else:
            print(itemname, type(item))
    return tmpsize


def pretty_print(dir=DIRS, pre=""):
    for itemname, item in dir.items():
        if type(item) is dict:
            print(f'{pre}-', itemname, "(dir)")
            pretty_print(item, pre + "  ")
        else:
            print(f'{pre}-', itemname, f"(file, size={item})")


advent()
