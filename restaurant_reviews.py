#This mini-challenge prints the review of the restaurant based on how many stars it has
rating = float(input("How many stars does this restaurant have? "))

if rating > 4.5:
  print("Perfection")
elif rating > 4:
  print("Excellent")
elif rating > 3:
  print("Good")
elif rating > 2:
  print("Fair")
else:
  print("Poor")
