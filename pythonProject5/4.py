# 4. Write a Python program to count the number of even and odd numbers in a series of numbers
#     Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#     Expected Output :
#     Number of even numbers : 5
#     Number of odd numbers : 4


lyginiai = []
nelyginiai = []

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for i in numbers:
    if i % 2 == 0:
        lyginiai.append(i)
    else:
        nelyginiai.append(i)

lyginius_skaicius = len(lyginiai)
nelyginiu_skaicius = len(nelyginiai)

print('Suma lyginiu lygi: ', lyginius_skaicius)

print('Suma nelyginiu lygi: ', nelyginiu_skaicius)

