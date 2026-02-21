#Expanding on logical operators
height = int(input("what is your height in cm? "))
credits = int(input("how many credits do you have? "))

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif height < 137 and credits >= 10:
  print("You are not tall enough to ride.")
elif height > 137 and credits < 10: 
  print("You don't have enough credits.")
else:
  print("You do not meet the criteria to ride this roller coaster")
