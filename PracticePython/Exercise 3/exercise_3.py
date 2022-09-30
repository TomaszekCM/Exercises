# Take a list, say for example this one:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
#     Instead of printing the elements one by one, make a new list that has all the elements
#     less than 5 from this list in it and print out this new list.
#
#     Write this in one line of Python.
#
#     Ask the user for a number and return a list that contains only elements from the original list
#     that are smaller than that number given by the user.

my_file = open("list.txt", "r")
content = my_file.read()
my_file.close()

# content is a text looking as a list, so we have to remove square brackets and cut it to get a listt
list = (content[1:-1]).split(", ")
print(list)

print("Elementy mniejsze niż 5: ")

less_than_5 = []
for i in list:
    if int(i) < 5:
        print(i)
        less_than_5.append(i)

# Extras:

print(less_than_5)
print([i for i in list if int(i) < 5])

control_number = input("Podaj liczbę od krórej mniejsze mają być wyszukane elementy: ")

while control_number.isnumeric() == False:
    control_number = input("Podaj LICZBĘ! ")

print("Liczby mniejsze od ", control_number, "to: ", [i for i in list if int(i)<int(control_number)])