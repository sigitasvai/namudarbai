# 8.	Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing', add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc' Expected Result : 'abcing' Sample String : 'string' Expected Result : 'stringly'

string_input = 'string'
if len(string_input) < 3:
    print(string_input)
elif string_input.endswith('ing'):
     print(string_input + 'ly')
else:
    print(string_input + 'ing')