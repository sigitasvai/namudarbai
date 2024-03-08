# Žodyno kūrimas:Sukurkite žodyną, kuriame būtų asmens duomenys.
# Juose turi būti tokie duomenys, kaip "vardas", "amžius", "lytis" ir "profesija".
# Atspausdinkite reikšmę, susijusią su raktu "amžius".


asmens_duomenys = {'vardas': ['Jonas','Egle','Audrius', 'Inga'],
                   'amzius': [30, 40, 35, 39],
                   'lytis': ['vyras', 'moteris', 'vyras', 'moteris'],
                   'profesija': ['gydytojas', 'mokytojas', 'vairuotojas','valytojais'],

                   }
# print(asmens_duomenys['amzius'])

# Žodyno atnaujinimas:
#  Pridėkite naują raktą-reikšmę prie žodyno, sukurtam pirmoje užduotyje,
#  reprezentuojančią asmens "miestą".

asmens_duomenys['miestas'] = ['Vilnius', 'Kaunas', 'Klaipeda', 'Panevezys']



# Iteravimas per žodyną:
# Parašykite ciklą, kad išspausdintumėte visas raktas-reikšmes žodyne, sukurtame pirmoje užduotyje.

for i in asmens_duomenys.items():
    print(i)

# Žodyno metodai:
# Naudodami žodynų metodus, išskirkite ir atspausdinkite visus raktus ir visus reikšmes atskirai iš žodyno,
# sukurto pirmoje užduotyje.

print(asmens_duomenys.keys())
print(asmens_duomenys.values())

# Sąlyginiai veiksmai su žodynais:
# Patikrinkite, ar žodyne yra raktas "miestas".
# Jei yra, atspausdinkite "Miesto informacija prieinama",
# kitaip atspausdinkite "Miesto informacija neprieinama".

if 'miestas' in asmens_duomenys.keys():
    print('Miesto informacija prieinama')
else:
    print('Miesto informacija neprieinama')

# Žodyno rikiavimas:
# Surikiuokite žodyną, sukurtą septintoje užduotyje,
# pagal raktus ir išspausdinkite surikiuotas raktas-reikšmes.

sorted_asmens_duomenys = sorted(asmens_duomenys.items())
print(dict(sorted_asmens_duomenys))



