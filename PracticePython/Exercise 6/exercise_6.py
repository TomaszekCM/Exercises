# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)


customers_string = input("Podaj napis aby sprawdzić czy czytany od tyłu jest taki sam jak od przodu: ")

if customers_string == customers_string[::-1]:
    print("Twój tekst jest taki sam od przodu jak i od tyłu")
else:
    print("Twój tekst czytany od tyłu brzmi inaczej niż czytany od przodu")


# Alternatively:
# is_a_palindrome = True
# for i in range(0,int(len(customers_string)/2+1)):
#     if customers_string[i] != customers_string[-i-1]:
#         is_a_palindrome = False
#
# if is_a_palindrome:
#     print("Twój tekst jest taki sam od przodu jak i od tyłu")
# else:
#     print("Twój tekst czytany od tyłu brzmi inaczej niż czytany od przodu")