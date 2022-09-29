# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.


def get_users_number():
    users_number = input("Podaj liczbę, którą chcesz sprawdzić, czy jest liczbą pierwszą: ")
    while users_number.isnumeric() == False:
        users_number = input("LICZBĘ! ")
    return int(users_number)

# print(users_number)
users_number = get_users_number()

# dzielniki = [i for i in range(1, users_number+1) if users_number % i == 0]
#
# if len(dzielniki) == 2:
#     print("To jest liczba pierwsza!")
# else:
#     print("To nie jest liczba pierwsza - posiada następujące dzielniki: ", dzielniki)

print()
print()
print('-------------------------------------------------------------------------------------')
print()


# Szybsza wersja, bez podawania konkretnych dzielników - wystarczy sprawdzić reszty z dzielenia
# przez wszystkie liczby od 2 do n^(1/2) - jeśli tam nie będzie dzielników, to nie będzie ich wcale
import math
pierwsze_dzielniki = [i for i in range(1, int(math.sqrt(users_number))) if users_number % i == 0]
# print(pierwsze_dzielniki)
if len(pierwsze_dzielniki) <= 1:
    print("To jest liczba pierwsza!")
else:
    print("To nie jest liczba pierwsza.")