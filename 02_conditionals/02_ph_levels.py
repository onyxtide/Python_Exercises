#Learning about Python's relational operators and elif statements via the pH scale
ph = int(input("Please tell me the ph level of the liquid, using arabic numericals: "))
if ph > 7:
  print("Basic")
elif ph < 7:
  print("Acidic")
else:
  print("Neutral")
