# In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.
#
# This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100.
# The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
#
# At the end of this exchange, your program should print out how many guesses it took to get your number.
#
# As the writer of this program, you will have to choose how your program will strategically guess.
# A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number.
# But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range),
# and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy!


def let_me_guess(a,b):
    print(f"Pomyśl o jakiejś liczbie z przedziału {min(a, b)} - {max(a, b)}.")

    import time
    time.sleep(5)

    global number_of_tries
    number_of_tries = 0

    def guess(c, d):
        lower = min(c, d)
        higher = max(c, d)

        middle = int(lower + (higher - lower)/2)

        global number_of_tries
        number_of_tries += 1

        print(f"Strzelam, że wybrałeś {middle}!")
        answer = input("Czy zgadłem? (wpisz odpowiednio: 'TAK/ZA MAŁO/ZA DUŻO'): ")
        while answer != "TAK" and answer != "ZA MAŁO" and answer != "ZA DUŻO":
            answer = input("Dostępne opcje to 'TAK/ZA MAŁO/ZA DUŻO'! Wpisz raz jeszcze: ")

        if answer == "TAK":
            return True
        elif answer == "ZA MAŁO":
            return guess(middle, higher)
        else:
            return guess(lower, middle)

    guess(a, b)

    return f"Zgadłem za {number_of_tries} razem! :)"


if __name__ == "__main__":
    print(let_me_guess(1,100))