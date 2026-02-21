#Let's calculate one's weight on different planets! 
print("Little astronaut, let's see how much you weight on the planet of your choice!")
print("You need to know that before you land there!")
print("In a minute wou will need to type:")
print("1 for Mercury")
print("2 for Venus")
print("3 for Mars")
print("4 for Jupiter")
print("5 for Saturn")
print("6 for Uranus")
print("7 for Neptune")

weight = float(input("But first, what is your weight? "))
planet = int(input("Now choose your destination. Please, type the number of the planet: "))

if planet == 1:
  print("Your weight there will be:", weight * 0.38)
elif planet == 2:
  print("Your weight there will be:", weight * 0.91)
elif planet == 3:
  print("Your weight there will be:", weight * 0.38)
elif planet == 4:
  print("Your weight there will be:", weight * 2.53)
elif planet == 5:
  print("Your weight there will be:", weight * 1.07)
elif planet == 6:
  print("Your weight there will be:", weight * 0.89)
elif planet == 7:
  print("Your weight there will be:", weight * 1.14)
else:
  print("Invalid number")
