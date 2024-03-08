# 4.	Daugybos lentelė: Parašykite funkciją,
# kuri priima sveikąjį skaičių ir spausdina jo daugybos lentelę iki 10.




def daugybos_lentele(skaicius):
    res = 1
    for i in  range(1, 11):
        res = skaicius * i
        print(res)




daugybos_lentele(int(input('Iveskite skaiciu: ')))
