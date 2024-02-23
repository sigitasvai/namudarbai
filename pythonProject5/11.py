# Generate a random number between 1 and 10. Ask the user to guess the number using a while loop.
# Provide feedback if the guessed number is too high or too low.
# Continue the loop until the user guesses correctly.
import random

s = random.randrange(1, 10)
print(s)
while True:
    spejimas = int(input('Iveskite spejama skaiciu: '))
    if spejimas == s:
        print('Jus atspejote!')
        break
    elif spejimas > s:
        print('Spejamas skaicius yra mazesnis')
    elif spejimas < s:
        print('Spejamas skaicius yra didesnis')

