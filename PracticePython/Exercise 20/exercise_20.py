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
    print(in_or_not([1,4,6,8,3,7, 3,4, 5, 6,7], 11))


# Extras:
