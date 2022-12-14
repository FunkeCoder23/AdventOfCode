def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


global elves, elf_num
elves = {}
elf_num = 1


def count_calories(calories):
    global elves, elf_num
    # print(calories)
    if (calories.strip() == ""):
        elf_num += 1
        return
    try:
        elves.update({elf_num: elves[elf_num] + int(calories)})
    except:
        elves.update({elf_num: int(calories)})


def advent():

    inp = getInput()
    for calories in inp:
        count_calories(calories)
    # print(elves)
    print(max(elves.values()))


advent()
