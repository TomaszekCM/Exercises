# This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.
#
# Time for some fake graphics! Let’s say we want to draw game boards that look like this:
#
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
#
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
#
# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
#
# Remember that in Python 3, printing to the screen is accomplished by
#
#   print("Thing to show on screen")
#
# Hint: this requires some use of functions, as were discussed previously on this blog and elsewhere on the Internet,
# like this TutorialsPoint link.



def draw_board(x, y):

    hyphens = " ---"
    slash = "|   "
    row = ""
    board = hyphens * x + "\n"
    for i in range(y):
        board += slash * x + "|" + "\n" + hyphens * x + "\n"

    return board


def draw_board2(x, y, board):
    hyphens = " ---"
    slash = "|   "
    row = ""
    new_board = hyphens * x + "\n"

    for row in board:
        for col in row:
            if col == 0:
                new_board += "|   "
            else:
                new_board += f"| {col} "
        new_board +="|" + "\n" + hyphens * x + "\n"

    return new_board


def users_board():
    x = input("Podaj liczbę kolumn: ")
    while x.isnumeric() == False:
        x = input("LICZBĘ: ")

    y = input("Podaj liczbę wierszy: ")
    while y.isnumeric() == False:
        y = input("LICZBĘ: ")

    x = int(x)
    y = int(y)
    return draw_board(x, y)



if __name__ == "__main__":
    board = [["X", 0, 0], ["X", "O", 0], ["X", 0, 0]]
    print(draw_board2(3, 3, board))
    # print()
    # print(users_board())
