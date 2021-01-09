def generate_board_alt(n):
    return [[[randint(n ** 2 * - 1, n ** 2), 0] for _i in range(n)] for _j in range(n)]

def pick_row(board, i):
    for square in board[i]:
        square[1] = 1
    return board


def pick_column(board, j):
    for row in board:
        row[j][1] = 1
    return board

def run_game(n):
    board = generate_board(n)
    board = pick_row(i)
    board = pick_column(j)



board = generate_board(4)
print_board(board)
pick_row(board, 0)
pick_column(board, 1)
print_board(board)


# def p1_rows(board):
#     row_mins = []
#     for x, row in enumerate(board):
#         row_mins.append((x, check_for_negatives(row)))
#     best_order = sorted([num[1] for num in row_mins], reverse=True)
#     print(row_mins)
#     print(best_order)
#     row_choice = []
#     for num in best_order:
#         for pair in row_mins:
#             if pair[1] == num:
#                 row_choice.append(pair[0])
#     return row_choice



# def p2_columns(board, p1_moves):
#     points = 0
#     for i, row in enumerate(p1_moves):
#         current_row = board[row]
#         for counter in enumerate(current_row)
#
#         points += (min(board[row]))
#         # print(min(board[row]))
#     print(points)


# p1_moves = p1_rows(test_board)
# p2_columns(test_board, p1_moves)