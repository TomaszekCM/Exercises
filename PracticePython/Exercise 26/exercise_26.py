#  This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.
#
# As you may have guessed, we are trying to build up to a full tic-tac-toe board.
#  However, this is significantly more than half an hour of coding, so we’re doing it in pieces.
#
# Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.
#
# If a game of Tic Tac Toe is represented as a list of lists, like so:
#
# game = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]
#
# where a 0 means an empty square, a 1 means that player 1 put their token in that space,
#  and a 2 means that player 2 put their token in that space.
#
# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
#  tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row,
#  a column, or a diagonal. Don’t worry about the case where TWO people have won
#  - assume that in every board there will only be one winner.
#
# Here are some more examples to work with:
#
# winner_is_2 = [[2, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]
#
# winner_is_1 = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]
#
# winner_is_also_1 = [[0, 1, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]
#
# no_winner = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 2]]
#
# also_no_winner = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 0]]
#
# second_wins = [[1, 2, 2],
# 	[2, 2, 0],
# 	[2, 1, 0]]

# for i in range(len(second_wins)):
#     print(i)


import numpy as np


def tic_tac_toe_winner(board):
    # now we check all colls and rows
    for row in board:
        if len(set(row)) == 1:
            if row[0] != 0:
                return f"wygrywa gracz {row[0]}"

    transposed_board = np.transpose(board)
    for col in transposed_board:
        if len(set(col)) == 1:
            if col[0] != 0:
                return f"wygrywa gracz {col[0]}"

    # we also have to check diagonals
    # we start from point 0,0
    win = False
    checked_point = board[0][0]
    if checked_point != 0:
        for i in range(len(board)):
            if checked_point == board[i][i]:
                win = True
            else:
                win = False
                break
        if win == True:
            return f"wyrywa gracz {checked_point}"

    # and now we have to start from point n,0
    checked_point = board[len(board)-1][0]
    if checked_point != 0:
        for i in range(len(board)):
            if checked_point == board[(len(board)-1)-i][i]:
                win = True
            else:
                win = False
                break
        if win == True:
            return f"wygrywa gracz {checked_point}"

    return "Nierozstrzygnięte!"



# First, not optimal (or could be called "ugly") version, working on 3x3 matrix only - it checks all points next to each
# point from first col and row of the matrix
def who_wins(board):

    index_1 = 0
    index_2 = 0
    west = 0, -1
    north_west = -1, -1
    north = -1, 0
    north_east = -1, 1
    east = 0, 1
    south_east = 1, 1
    south = 1, 0
    south_west = 1, -1
    directions = [west, north_west, north, north_east, east, south_east, south, south_west]

    def check_in_possition(x, y):
        checked_point = board[x][y]
        for i in directions:
            if 0 <= (x + i[0]) <= 2 and 0 <= y + i[1] <= 2 and checked_point == board[x + i[0]][y + i[1]]:
                if 0 <= (x + i[0] + i[0]) <= 2 and 0 <= y + i[1] + i[1] <= 2 and checked_point == board[x + i[0] + i[0]][y + i[1] + i[1]]:
                    return f'wygrywa gracz {checked_point}'
                else:
                    continue
            else:
                continue
        return "nothing"

    for i in range(len(board[0])):
        if board[i][index_2] != 0:
            result = check_in_possition(i, index_2)
            if result != "nothing":
                return result

    for i in range(len(board)):
        if board[index_1][i] != 0:
            result = check_in_possition(index_1, i)
            if result != "nothing":
                return result

    return "Nikt nie wygrał"




winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

second_wins = [[1, 2, 2],
	[2, 2, 0],
	[2, 1, 0]]

first_wins1 = [[1, 1, 2],
	[2, 1, 0],
	[2, 1, 0]]

second_wins2 = [[1, 2, 2],
	[2, 2, 2],
	[1, 1, 1]]

second_wins3 = [[2, 2, 1, 1],
	[2, 2, 1, 1],
	[1, 0, 2, 2],
    [1, 2, 1, 1]]


if __name__ == "__main__":
    print(tic_tac_toe_winner(no_winner))

    print(who_wins(no_winner))