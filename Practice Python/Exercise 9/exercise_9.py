# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
#     Keep the game going until the user types “exit”
#     Keep track of how many guesses the user has taken, and when the game ends, print this out.


import random

number_to_guess = random.randint(1,9)

def game():
    users_guess = input("Zgadnij jaką cyfrę z zakresu 1-9 wylosował komputer: ")
    while users_guess.isnumeric() == False:
        users_guess = input("CYFRĘ podaj: ")

    counter = 1
    while True:
        if number_to_guess == int(users_guess):
            print("Brawo, zgadłeś za ", counter, " razem!")
            break
        elif number_to_guess > int(users_guess):
            users_guess = input("Za mało, spróbuj jeszcze raz: ")
            counter += 1
        else:
            users_guess = input("Za dużo, spróbuj raz jeszcze: ")
            counter += 1

        if users_guess == "exit":
            break
        while users_guess.isnumeric() == False:
            users_guess = input("CYFRĘ podaj: ")

game()