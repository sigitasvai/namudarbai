#
# 1.Pasisveikinimo funkcija: Parašykite funkciją,
# kuri priima vartotojo vardą kaip argumentą ir grąžina pasisveikinimo žinutę su tuo vardu.

def pasisveikinimas(vardas):
    b ='Sveiki! ' + vardas
    return b

a = pasisveikinimas(input('Iveskite savo varda: '))
print(a)