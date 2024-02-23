# 3.	Remove Duplicates: Write a Python function that takes
# a string as input and removes any duplicate characters,
# maintaining the original order of characters.

string_input = input('Iveskite simboliu eilute: ')

string_list = list(string_input)
new_list = []
for i in string_list:
    if i not in new_list:
        new_list.append(i)


print(new_list)
# nezinau kaip vel kovertuoti atgal list i string

