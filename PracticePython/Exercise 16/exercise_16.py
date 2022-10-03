# Note: this is a 4-chili exercise, not because it introduces a concept, but because this exercise is more like a project.
# Feel free to skip this and come back when you’re more ready!
#
# Write a password generator in Python. Be creative with how you generate passwords
# - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.
#
# Extra:
#
#     Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random, string
from PracticePython.functions import get_number


def password_generator():
    password_lenght = get_number("Podaj liczbę znaków Twojego hasła (co najmniej 8 znaków): ")
    while password_lenght < 8:
        password_lenght = get_number("Podaj liczbę większą niż 7!: ")

    choices = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits]
    password_parts = []

    for i in choices:
        password_parts.append(random.choice(i))

    for i in range(password_lenght-4):
        password_parts.append(random.choice(random.choice(choices)))

    random.shuffle(password_parts)
    new_password = "".join(password_parts)

    return new_password


# if __name__ == "__main__":
#     # for i in range(10):
#     print(password_generator())


# Extras

def new_password_generator():
    strong_or_week = input("Czy nowe hasło ma być słabe, czy silne (wpisz: słabe/silne): ")
    while strong_or_week not in ["słabe", "silne"]:
        strong_or_week = input("Wpisz 'słabe' lub 'silne' ! ")

    if strong_or_week == "słabe":
        from words import words_to_password
        how_many_words = random.choice([1,2])
        if how_many_words == 1:
            new_password = random.choice(words_to_password)
        else:
            new_password = "".join([random.choice(words_to_password) for i in range(1,3)])

    else:
        new_password = password_generator()

    return new_password


if __name__ == "__main__":
    print(new_password_generator())