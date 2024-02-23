# 6.	Write a Python function to get a string made of the first 2 and last 2 characters
# of a given string. If the string length is less than 2, the result should be an empty string.
# Sample String : 'w3resource' Expected Result : 'w3ce'
# Sample String : 'w3' Expected Result : 'w3w3' Sample String : ' w' Expected Result : Empty String

# string_input = input(''IVeskit simboliu eilute :)

string_input = 'www'

if len(string_input) < 2:
    print('')
elif len(string_input) == 2:
    print(string_input + string_input)
else:
    print(string_input[:3] + string_input[-1:])