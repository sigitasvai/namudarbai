# 4.	Capitalize First Letter: Write a Python function that takes a string as input
# and capitalizes the first letter of each word in the string.

# string_input = input('Iveskit simbolius: ')
string_input = 'safdfdf sdfdsfsdf sdfsdfsdf'

new = string_input.capitalize()
empty_string = ''
for i in string_input:
    if i == ' ':
        didzioji = string_input[i].upper()
        empty_string += didzioji


    else:
        empty_string += i
print(new)

