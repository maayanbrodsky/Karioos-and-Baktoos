from math import inf
from random import randint


TEST_BOARD = [[-34, 59, 50],
[83, -97, 39],
[-89, -98, -85]]  # optimal score for p2 is -216


def generate_board(n):
    return [[randint(-100, 100) for _i in range(n)] for _j in range(n)]

def print_board(board):
    print(*board, sep='\n')
    print('\n')


def check_for_negatives(row):
    optimal = -inf
    negatives = 0
    for num in row:
        if optimal < num < 0:
            optimal = num
            negatives += 1
    if negatives == 0:
        return max(row)
    else:
        return optimal


def max_points(board):
    points = 0
    for row in board:
        points += check_for_negatives(row)
    if points > 0:
        points = 0
    return points


board = generate_board(4)
print_board(board)
print(max_points(board))
