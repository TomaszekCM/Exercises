# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code,
# use the code from the solution), and instead of printing the results to a screen, write the results to a txt file.
# In your code, just make up a name for the file you are saving to.
#
# Extras:
#
#     Ask the user to specify the name of the output file that will be saved.

import sys

# this exercise requires to import function written before; as there is a space in the folder name, it is problematic
# to import a function from a different directory, so the easiest way woyld be to append sys.path list, to make python
# search in the appropriate folder
new_path = sys.path[0][:-2] + "19"
sys.path.append(new_path)
from exercise_19 import get_plain_text

def into_file(name):
    file = open(name, "w")
    file.write(get_plain_text())
    file.close()
    print("zrobione")

def into_named_file():
    file_name = input("Podaj nazwę pliku do którego chcesz zapisać tekst: ") + ".txt"
    into_file(file_name)

if __name__ == "__main__":
    # into_file("nowy plik.txt")
    into_named_file()
