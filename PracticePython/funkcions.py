def get_number(message):
    users_number = input(message)
    while users_number.isnumeric() == False:
        users_number = input("LICZBĘ! ")
    return int(users_number)