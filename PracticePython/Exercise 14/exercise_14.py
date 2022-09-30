# Write a program (function!) that takes a list and returns a new list that contains all the elements
# of the first list minus all the duplicates.
#
# Extras:
#
#     Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#     Go back and do Exercise 5 using sets, and write the solution for that in a different function.



def no_duplicated(list):
    new_set = set(list)
    new_list = [i for i in new_set]
    return new_list

print(no_duplicated([1,1,2,2,3,4,5,"d",6]))


# Extras:

# 1
def loop_no_duplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(loop_no_duplicates([1,1,2,2,3,4,5,"d",6]))

# 2

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def no_common_elements(x, y):
    new_list = []
    for i in x:
        if i in y:
            new_list.append(i)

    set_without_duplicates = set(new_list)
    # and we need to have a list instead of set:
    final_list = [i for i in set_without_duplicates]
    return final_list

print(no_common_elements(a,b))