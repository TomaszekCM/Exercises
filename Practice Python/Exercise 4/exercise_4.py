# Create a program that asks the user for a number and then prints out a list of all the divisors
# of that number. (If you don’t know what a divisor is, it is a number that divides evenly
# into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

users_number = input("Podaj liczbę, której dzielniki chcesz znaleźć: ")
while users_number.isnumeric() == False:
    users_number = input("LICZBĘ! ")
users_number = int(users_number)

print(users_number)

dzielniki = [i for i in range(1, users_number+1) if users_number % i == 0]

print(dzielniki)

# this looks as slow as the above solution
div=[]
for y in range(1,users_number+1):
    a=int(users_number/y)
    if users_number-a*y==0:
        div.append(y)

print(div)

# Above code is not effective for the high numbers