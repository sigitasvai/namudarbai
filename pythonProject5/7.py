# . Multiplication Table:
#     Ask the user to enter a number and print its multiplication table (up to 10) using a for loop.


skaicius = int(input('Iveskite skaiciu: '))

for i in range(1, 11):
    result = skaicius * i
    print(result)