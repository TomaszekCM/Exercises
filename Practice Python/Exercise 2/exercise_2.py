# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
#
# Extras:
#
#     If the number is a multiple of 4, print out a different message.
#
#     Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#     If check divides evenly into num, tell that to the user.
#     If not, print a different appropriate message.


number = input("Podaj liczbę: ")
while number.isnumeric() == False:
    number = input("To naprawdę musi być liczba - inaczej nie zadziała. Podaj raz jeszcze: ")

if int(number) % 2 == 0:
    print("Podałeś liczbę parzystą.")
else:
    print("Podałeś liczbę nieparzystą.")


# Extras:

if int(number) % 4 == 0:
    print("Podana liczba jest podzielna przez 4")

print()
print("-------------------------------")
print()

print("Podaj dwie liczby: ")
x = input("1: ")
while x.isnumeric() == False:
    x = input("To musi być liczba - podaj pierwszą raz jeszcze: ")
y = input("2: ")
while y.isnumeric() == False:
    y = input("To musi być liczba - podaj drugą raz jeszcze: ")

if int(x) % int(y) == 0:
    print("Druga liczba jest dzielnikiem pierwszej.")
else:
    print("Pierwsza liczba nie dzieli się bez reszty przez drugą.")