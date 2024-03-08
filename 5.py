# 5.Didžiausio ir mažiausio skaičiaus radimas:
# Parašykite funkciją, kuri priima sąrašą skaičių
# ir grąžina didžiausią ir mažiausią skaičius šiame sąraše.

def max_min(*args):
    res = []
    dizdiausias = max(args)
    res.append(dizdiausias)
    maziausias = min(args)
    res.append(maziausias)
    return res




rezultatas = max_min(5, 6, 9, 10, 3, 55 )
print(rezultatas)
