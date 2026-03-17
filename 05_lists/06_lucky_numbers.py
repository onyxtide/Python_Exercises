#Generate two lists of random numbers (five from 1–69 and one from 1–26 each)
import random

my_numbers = []
winning_numbers = []


for _ in range(5):
  num = random.randint(1, 69)
  my_numbers.append(num)
  win_num = random.randint(1, 69)
  winning_numbers.append(win_num)


my_numbers.append(random.randint(1,26))
winning_numbers.append(random.randint(1,26))

print(my_numbers)
print(winning_numbers)
