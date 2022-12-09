import sys, os, time



new_path = sys.path[0][:-2] + "24"
sys.path.append(new_path)
new_path2 = sys.path[0][:-2] + "26"
sys.path.append(new_path2)
new_path3 = sys.path[0][:-2] + "27"
sys.path.append(new_path3)
from exercise_24 import draw_board2
from exercise_26 import tic_tac_toe_winner
from exercise_27 import make_a_move



def tic_tac_toe():
    os.system('clear')
    def is_there_a_move(board):
        for row in board:
            for i in row:
                if i == 0:
                    return True

    class Player:
        player = "O"
        def change_player(self):
            if self.player == "X":
                self.player = "O"
            else:
                self.player = "X"

    print("Witaj w grze w kółko i krzyżyk!")
    current_player = Player()

    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    while is_there_a_move(board):
        print(draw_board2(3, 3, board))
        board = make_a_move(board, current_player.player)
        result = tic_tac_toe_winner(board)
        if result == "Nierozstrzygnięte!":
            current_player.change_player()
        else:
            os.system('clear')
            print(draw_board2(3, 3, board))
            return result
        os.system('clear')

    print(draw_board2(3, 3, board))

    return "Remis!"


def more_games():
    x = 0
    o = 0
    r = 0
    games = 0

    once_again = "tak"
    while once_again == "tak":
        game = tic_tac_toe()
        print(game)
        if game[-1] == "X":
            x += 1
        elif game[-1] == "O":
            o += 1
        else:
            r += 1
        games += 1

        time.sleep(2)
        once_again = input("Czy chcesz zagrać jeszcze raz (tak/nie)? ")

    if x == 1:
        x_games = "grę"
    elif x == 0 or x >= 5:
        x_games = "gier"
    else:
        x_games = "gry"

    if o == 1:
        o_games = "grę"
    elif o == 0 or x >= 5:
        o_games = "gier"
    else:
        o_games = "gry"

    if o == 1:
        no_games = "gry"
    else:
        no_games = "gier"

    return f"Wyniki {games} {no_games}: Użytkownik 'X' wygrał {x} {x_games}, użytkownik 'O' wygrał {o} {o_games}. Nierozegranych było {r}."


if __name__ == "__main__":
    # jedna gra:
    # print(tic_tac_toe())
    # więcej gier:
    print(more_games())