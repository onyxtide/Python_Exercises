#Snake eyes dice game with randint() function and while loop
import random

die1 = 3
die2 = 3
total = die1 + die2

while total != 2:
  print("Nope")
  die1 = random.randint(1,6)
  die2 = random.randint(1,6)
  die1 = random.randint(1,6)
  die2 = random.randint(1,6)
  total = die1 + die2
else:
  print("Snake eyes!")
