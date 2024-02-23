# 3. User Input: Create a program that asks the user to enter a number.
# Use a while loop to print the square of that number and ask the user if they want to enter another number.
# Continue the loop until the user chooses to exit.
#
#
testi = ''
while True:
  i = int(input('Iveskite skaiciu: '))
  print(i, 'skaiciaus kvadratas yra: ', i**2)
  print('Ar norite tesi? Y / N')
  testi = input('')
  if testi == 'Y':
      continue
  else:
      break
