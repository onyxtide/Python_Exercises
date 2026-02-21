'''
Snapple is a famous tea brand born in Brooklyn, NY. Every bottle cap hides a quirky, fun fact. 🍑

Here we use the random module to generate a number between 1 and 6.
'''
import random
tea = random.randint(1, 6)

if tea == 1:
  print('Flamingos turn pink by eating shrimp.')
elif tea == 2:
  print('Honey never goes bad.')
elif tea == 3:
  print('Shrimp can only swim backwards.')
elif tea == 4:
  print('A taste bud\'s life is about 10 days.')
elif tea == 5:
  print('You can\'t sneeze while sleeping.')
elif tea == 6:
  print('Tiny pocket in jeans was for watches.')
