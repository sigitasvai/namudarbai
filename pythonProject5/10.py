# 7. Nested Loop - Multiplication Table:
#     Use a nested loop (combination of while and for) to print the multiplication table from 1 to 5.

# skaicius = int(input('Iveskite skaiciu: '))
skaicius = int(5)
count = 1
while count <= skaicius:
    for i in range(1, 6):
        result = count * i
        print(result)
    count += 1
