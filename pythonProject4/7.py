# 7.	Write a Python program to get a string from a given string
# where all occurrences of its first char have been changed to '$',
# except the first char itself. Sample String : 'restart' Expected Result : 'resta$t'

string_input = 'restart'

pirma_raide = string_input[0]
be_pirmos_raides = string_input[1:]
replace_string = be_pirmos_raides.replace(pirma_raide,'$')
new_string = pirma_raide + replace_string


print(new_string)