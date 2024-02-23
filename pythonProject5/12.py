# 9.Factorial Calculation: Ask the user to enter a number and calculate its factorial using a for loop.
# The factorial of a number n is the product of all positive integers up to n.

skaicius = int(input('Iveskite skaiciu: '))
sum = 1
for i in range(1, skaicius + 1):
    sum *= i

print(sum)