def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()
global elves,elf_num
elves = {}
elf_num = 1
def count_calories(calories):
    global elves,elf_num
    # print(calories)
    if(calories.strip() == ""):
        elf_num +=1
        return
    try:
        elves.update({elf_num:elves[elf_num]+int(calories)})
    except:
        elves.update({elf_num:int(calories)})
    
def advent():
    global elves
    inp = getInput()
    for calories in inp:
        count_calories(calories)
    # print(elves)
    max_1 = max(elves.values())
    elves_1={key:val for key, val in elves.items() if val != max_1}
    max_2 = max(elves_1.values())
    elves_2={key:val for key, val in elves_1.items() if val != max_2}
    max_3 = max(elves_2.values())
    print(max_1+max_2+max_3)
advent()