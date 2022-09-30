# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence
# is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

from PracticePython.funkcions import get_number

how_many_numbers = get_number("Podaj liczbę elementów ciągu Fibonacciego, którą chcesz wyświetlić: ")

def fibonacci(n):
    required_numbers = []
    if n == 0:
        return []
    elif n== 1:
        return [1]
    elif n==2:
        return [1,1]
    elif n>2:
        required_numbers = [1, 1]
        i = 1
        while i < (n -1):
            required_numbers.append(required_numbers[i] + required_numbers[i-1])
            i += 1
        return required_numbers

print(fibonacci(how_many_numbers))


# or simpler:
def fib(n):
    a, b = 1, 1

    for i in range(n):
        yield a
        a, b = b, a + b

print(list(fib(how_many_numbers)))