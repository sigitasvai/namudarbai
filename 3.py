# 3.	Faktorialo skaičiavimas:
# Parašykite funkciją, kuri priima sveikąjį skaičių ir grąžina jo faktorialą.
#
def faktorialas(skacius):
    rez = 1
    for i in range(1, skacius + 1):
        rez = rez * i

    return rez




result = faktorialas(int(input('Iveskite skaiciu: ')))
print(result)

