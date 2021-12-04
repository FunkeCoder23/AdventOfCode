#!python.exe
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument(
    '-t', '--test', help="Run with test input", action='store_true')
args = parser.parse_args()


def getInput(file="input"):
    path=sys.path[0]
    if args.test:
        file = "test_input"
    with open(f"{path}/{file}", "r") as f:
        lines = f.read()
        return lines.splitlines()

def get_board(lines):
    board=[]
    for line in lines:
        nums=line.split()
        board.append(nums)
    return board


def main():
    boards=[]
    input = getInput()
    drawing=input[0]
    print(drawing)
    input.remove(drawing)
    input.remove('')

    drawing=drawing.split(',')
    print(drawing)
    board=[]
    for line in input:
        if line== '':
            boards.append(board)
            board=[]
            continue
        nums=line.split()
        for num in nums:
            board.append(num)
    for board in boards:
        print(board)
    called=[]
    winner=None
    for draw in drawing:
        if winner is not None:
            break
        called.append( draw)
        print(called)
        for board in boards:
            if draw in board:
                board[board.index(draw)]='X'
            if check_board(board):
                winner=board
                break

    print("WINNER")
    print_board(winner)
    print(called)
    print(score(winner)*int(called[-1]))
    
def score(board):
    sum=0
    for num in board:
        # print(num)
        if num == 'X':
            continue
        sum += int(num)
    print(sum)
    return sum



def check_board(board):
    # print_board(board)
    for i in range(5):
        if board[i*5] == board [i*5+1] == board [i*5+2]== board [i*5+3]== board [i*5+4]:   
            print("winner")
            return True
        if board[i] == board [i+5] == board[i+10] == board [1+15] == board[i+20]:
            print("winner")
            return True
    return False


def print_board(board):
    for r in range(5):
        for c in range(5):
            print(board[r*5+c],end=' ')
        print()
    print()

main()