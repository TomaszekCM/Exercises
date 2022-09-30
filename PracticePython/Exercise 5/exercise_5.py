# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes.
#
# Extras:
#
#     Randomly generate two lists to test this
#     Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def common_elements(list1, list2):
    common_list = []
    for i in list1:
        if i in list2 and i not in common_list:
            common_list.append(i)
    return common_list

print(common_elements(a,b))


# Extras:

import random

# function "sample" generated from range gives no duplicates
first_list = random.sample(range(1, 303), 20)
second_list = random.sample(range(1,303), 20)

first_list.sort()
second_list.sort()

print("Pierwsza wygenerowana lista: ", first_list)
print("Druga wygenerowana lista: ", second_list)
print("Elementry wspólne (policzone pierwotną funkcją): ", common_elements(first_list, second_list))

# common_elements_2 = [i for i in random.sample(range(1, 20), 19) if i in random.sample(range(1, 20), 19)]
print("Wspólne elementy 2 losowych list (napisane w jednej linii): ", [i for i in random.sample(range(1, 100), 10) if i in random.sample(range(1, 100), 10)])

# bb = [random.randint(1, 50) for a in range(1,29)]
# print("bbb", bb)

print("I na koniec trochę bardziej losowo, w jednej linii, ale z potencjalnymi powtórzeniami",
      [i for i in random.sample([random.randint(1, 50) for a in range(1,29)], 19) if i in random.sample([random.randint(1, 50) for a in range(1,29)], 19)])
