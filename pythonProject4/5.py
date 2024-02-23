# 5.	Check Anagrams: Write a Python function that checks
# if two strings are anagrams of each other. An anagram is a word or phrase
# formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.

zodis1 = input('Iveskite pirma zodi: ')
zodis2 = input('Iveskite antra zodi: ')


if sorted(zodis1) == sorted(zodis2):
    print('Anograma')
else:
    print('Ne anograma')
