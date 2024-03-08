# 2. Skaičių kvadratų sąrašas: Parašykite funkciją,
# kuri priima skaičių ir grąžina sąrašą,
# kuriame yra kvadratai visų skaičių nuo 1 iki nurodyto skaičiaus.

def kvadratas(skaicius):
    sarasas = []
    for i in range(1, skaicius+1):
        i = i**2
        sarasas.append(i)
    return sarasas

rezultatas = kvadratas(int(input('Iveskite skaciu: ')))
print(rezultatas)
