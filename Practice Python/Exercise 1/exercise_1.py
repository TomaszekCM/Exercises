# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Note: for this exercise, the expectation is that you explicitly write out the year
# (and therefore be out of date the next year).
#
# Extras:
#
#     Add on to the previous program by asking the user for another number
#       and printing out that many copies of the previous message.
#
#     Print out that many copies of the previous message on separate lines.
#     (Hint: the string "\n is the same as pressing the ENTER button)


# Main exercise:

name = input("Podaj swoje imię: ")
age = input("Podaj swój wiek: ")

while age.isnumeric() == False:
    age = input("Wiek musi być w formacie liczbowym! Podaj swój wiek jeszcze raz: ")

from datetime import date
today = date.today().year
date = today + 100 - int(age)
if date >= today:
    message = "W " + str(date) + " roku " + name + " skończy 100 lat. "
else:
    message = "W " + str(date) + " roku " + name + " skończył 100 lat. "
# print(message)


# Extras:

how_many_times = input("Podaj ile razy mam to wypisać: ")

while how_many_times.isnumeric() == False:
    how_many_times = input("Podaj liczbę! ")

print()
print(int(how_many_times)*message)
print("--------------------------------")
for i in range(int(how_many_times)):
    print(message)