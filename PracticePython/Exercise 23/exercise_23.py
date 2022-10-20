# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.



def common_elements_of_lists(first_list, second_list):
    list1 = []
    list2 = []
    with open(first_list, 'r') as open_file:
        for i in open_file:
            list1.append(i.replace("\n", ""))

    with open(second_list, 'r') as open_file:
        for i in open_file:
            list2.append(i.replace("\n", ""))

    # common_elements = list(set(list1) & set(list2))
    common_elements = [i for i in list1 if i in list2]

    return f"""Lista pierwsza: {list1} \nLista druga: {list2} \nElementy wspólne: {common_elements}"""

if __name__ == "__main__":
    print(common_elements_of_lists("primenumbers.txt", "happynumbers.txt"))