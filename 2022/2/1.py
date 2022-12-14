def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


SHAPE_SCORE = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def play_round(round):
    (one, two) = round.split(' ')
    tie = SHAPE_SCORE[two] + 3
    win = SHAPE_SCORE[two] + 6
    lose = SHAPE_SCORE[two]
    score = {
        ("X", "A"): tie,
        ("Y", "A"): win,
        ("Z", "A"): lose,
        ("X", "B"): lose,
        ("Y", "B"): tie,
        ("Z", "B"): win,
        ("X", "C"): win,
        ("Y", "C"): lose,
        ("Z", "C"): tie,
    }
    return score[(two, one)]


def advent():
    inp = getInput()
    tot_score =0;
    for round in inp:
        tot_score += play_round(round)
    print(tot_score)


advent()
