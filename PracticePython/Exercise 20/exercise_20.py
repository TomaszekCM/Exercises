# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest)
# and another number. The function decides whether or not the given number is inside the list and returns (then prints)
# an appropriate boolean.
#
# Extras:
#
#     Use binary search.



def in_or_not(list, number):
    if int(number) in list:
        return True
    else:
        return False

if __name__ == "__main__":
    print(in_or_not([1,3,4,5,6,7,8,11], 11))


# Extras:


def binary_in_or_not(list, number):
    if len(list) <= 3:
        # used try to reduce numbers of 'ifs' and to avoid out of range error
        # If there are only 3 arguments, the below algorithm does not work well, so the idea is to check 3 elements
        # starting from position [0]. Once our value is found, function returns result. If the function tries to
        # check position out of range, it means that there is no match in the list, so function returns "False"

        try:
            if list[0] == number:
                return True
            elif list[1] == number:
                return True
            elif list[2] == number:
                return True
            else:
                return False
        except:
            return False

    mid_index = int(len(list) / 2)

    if number == list[mid_index]:
        return True
    elif number < list[mid_index]:
        return binary_in_or_not(list[:mid_index], number)
    else:
        return binary_in_or_not(list[mid_index:], number)


if __name__ == "__main__":
    print(binary_in_or_not([343434,34245462,234662462623], 343434))