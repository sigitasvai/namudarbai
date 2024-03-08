# 6.Parašykite funkciją,
# kuri priima sąrašą skaičių ir grąžina jų vidurkį.
# Išbandykite funkciją su bet kokiu sąrašu skaičių.

def vidurkis(*args):
    sum = 0
    for i in range(len(list(args))):
        sum = sum + args[i]
    return sum / len(args)



rezultatas = vidurkis(5, 3, 4)
print(rezultatas)
