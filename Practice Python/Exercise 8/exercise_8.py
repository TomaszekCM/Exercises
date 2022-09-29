# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock

import time

print("Gra w kamień, papier i nożyczki")
print("--------------------------------")

options = ["kamień", "papier", "nożyczki"]

def who_wins(player_one, player_two):
    if player_one == player_two:
        return "Remis!"
    elif player_one == "kamień":
        if player_two == "papier":
            return "Wygrywa gracz 2!"
        elif player_two == "nożyczki":
            return "Wygrywa gracz 1!"
    elif player_one == "papier":
        if player_two == "kamień":
            return "Wygrywa gracz 1!"
        elif player_two == "nożyczki":
            return "Wygrywa gracz 2!"
    elif player_one == "nożyczki":
        if player_two == "kamień":
            return "Wygrywa gracz 2!"
        elif player_two == "papier":
            return "Wygrywa gracz 1!"


def game():
    print("Gracz 1:")
    player_one = input("Wpisz co wybierasz (kamień, papier, czy nożyczki): ")
    while player_one not in options:
        player_one = input("Wpisz poprawną opcję (kamień, papier, lub nożyczki)")
    # now we can give some time to change players
    time.sleep(1)
    print("Gracz 2:")
    player_two = input("Wpisz co wybierasz (kamień, papier, czy nożyczki): ")
    while player_two not in options:
        player_two = input("Wpisz poprawną opcję (kamień, papier, lub nożyczki)")

    print(who_wins(player_one, player_two))

    more = input("Czy chcesz grać dalej? (tak/nie): ")
    if more == "tak":
        game()
    # I do not use "else", as is would be pointless to require user to write (correctly) "nie" to stop the game
    # - if really wants, she/he would carefully write "tak"
# game()

def one_player_game():
    player_one = input("Wpisz co wybierasz (kamień, papier, czy nożyczki): ")
    while player_one not in options:
        player_one = input("Wpisz poprawną opcję (kamień, papier, lub nożyczki)")
    import random
    player_two = options[random.randint(0,2)]
    print("Komputer wybrał: ", player_two)
    time.sleep(2)

    result = who_wins(player_one, player_two)
    # this in this case these answers sound better than it would be using simple "print(who_wins....)"
    if result == "Wygrywa gracz 2!":
        print("Wygrał komputer!")
    elif result == "Wygrywa gracz 1!":
        print("Wygrałeś!")
    else:
        print(result)

    more = input("Czy chcesz grać dalej? (tak/nie): ")
    if more == "tak":
        one_player_game()

one_player_game()