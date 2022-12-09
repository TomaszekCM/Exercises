# Implement a function that takes as input three variables, and returns the largest of the three.
# Do this without using the Python max() function!
#
# The goal of this exercise is to think about some internals that Python normally takes care of for us.
# All you need is some variables and if statements!

from PracticePython.functions import get_number

def max_of_three():
    a = get_number("Podaj pierwszą liczbę: ")
    b = get_number("Podaj drugą liczbę: ")
    c = get_number("Podaj trzecią liczbę: ")

    if a >= b:
        biggest = a
    else:
        biggest = b

    if biggest < c:
        biggest = c

    return f"Największą z podanych liczb jest {biggest}."


print(max_of_three())