def getInput(file="input"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()


SHAPE_SCORE = {
    "A": 1,
    "B": 2,
    "C": 3,
}
WIN_SHAPE = {
    "A": "B",
    "B": "C",
    "C": "A",
}
LOSE_SHAPE = {
    "A": "C",
    "B": "A",
    "C": "B",
}


def play_round(round):
    (one, two) = round.split(' ')
    tie = SHAPE_SCORE[one] + 3
    win = SHAPE_SCORE[WIN_SHAPE[one]] + 6
    lose = SHAPE_SCORE[LOSE_SHAPE[one]]

    ROUND_END = {
        "X": lose,
        "Y": tie,
        "Z": win,
    }

    return ROUND_END[two]


def advent():
    inp = getInput()
    tot_score = 0
    for round in inp:
        tot_score += play_round(round)
    print(tot_score)


advent()
