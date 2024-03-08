# 8.	Sukurkite kelias funkcijas, kurios atlieka skirtingus veiksmus
# (pvz., prideda du skaičius, atima juos, daugina, dalija ir kt.).
# Tada sukurkite pagrindinę funkciją, kuri leistų vartotojui pasirinkti,
# kokią operaciją jis nori atlikti ir iškvieskite atitinkamą funkciją pagal pasirinkimą.

def suma(skacius1, skacius2):
    res = skacius1 + skacius2
    return res

def atimtis(skacius1, skacius2):
    res = skacius1 - skacius2
    return  res

def daugyba(skaicius1, skaicius2):
    res = skaicius1 * skaicius2
    return res

def result(skaicius1, skaicius2):
    print('Pasirinkite koki veiksma norite atlikti: daugyba  - D, sudetis - S, atimtis - A ')
    a = input()
    if a == 'A':
         b = atimtis(skaicius1, skaicius2)
         return  b
    elif a == 'D':
         c = daugyba(skaicius1, skaicius2)
         return c
    elif a == 'S':
        d = suma(skaicius1, skaicius2)
        return d


a = result(2, 3)
print(a)
