from math import inf
from random import randint
from typing import List


TEST_BOARD = [[-34, 59, 50],
              [83, -97, 39],
              [-89, -98, -85]]  # optimal score for p2 is -216

NUM_RANGE = 100


def generate_board(n: int, num_range: int) -> List[List[int]]:
    """Takes board size and number range (positive and negative), returns the board."""
    return [[randint(-num_range, num_range) for _i in range(n)] for _j in range(n)]


def check_for_negatives(row: List[int]) -> int:
    """Main algorithm. Takes board line, checks for the largest negative integer
    and returns it if no negatives exist, returns largest positive."""
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


def max_points(board: List[List[int]]) -> int:
    """Takes the board, sums the points assuming P2 maximizes points
    in response to P1 trying to minimize points."""
    points = 0
    for row in board:
        points += check_for_negatives(row)
    if points > 0:
        points = 0
    return points


board = generate_board(4, 100)
print(*board, sep='\n')
print(f'\nMax points for P2: {max_points(board)}')
