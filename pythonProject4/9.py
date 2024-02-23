# 9.	Write a Python program to remove the nth index character from a nonempty string.




str_input = 'Eilute'
if len(str_input) >= 1:
   remove_char = int(input('Iveskite indeksa kuri norite pasalinti: '))
   new_string = str_input[:remove_char] + str_input[remove_char +1 :]
   print(new_string)
else:
    print('Eilute tuscia')
