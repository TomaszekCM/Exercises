# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.
# For example, say I type the string:
#
#   My name is Michele
#
# Then I would see the string:
#
#   Michele is name My
#
# shown back to me.


user_sentence = input("Podaj jakieś zdanie, w którym chcesz odwrócić słowa: ")

def reverse_words(some_string):
    sentence_list = some_string.split(" ")
    reversed_list = sentence_list[::-1]
    final_sentence = " ".join(reversed_list)
    # final_sentence = ""
    # for i in reversed_list:
    #     final_sentence += (i + " ")
    return final_sentence

print(reverse_words(user_sentence))