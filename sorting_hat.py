#Putting it all together by creating a sorting hat test with results
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("It's time to place you, little wizard, into a proper house for you! ")
print("A wizard should be laconic!")
print("This means that you should only use whole numbers to respond to the questions")
print("LET'S START!")

Q1 = int(input("Question number one: do you like 1)Dawn or 2)Dusk? "))

if Q1 == 1:
  Gryffindor += 1; Ravenclaw += 1
elif Q1 == 2: 
     Hufflepuff += 1;  Slytherin += 1
else: 
     print ("Wrong input") 

Q2 = int(input("When I'm dead, I want people to remember me as: 1)The Good, 2)The Great, 3)The Wise, 4) The Bold? "))

if Q2 == 1:
  Hufflepuff += 2
elif Q2 == 2:
  Slytherin += 2
elif Q2 == 3:
  Ravenclaw += 2
elif Q2 == 4:
  Gryffindor += 2
else:
  print("Wrong input")

Q3 = int(input("Which kind of instrument most pleases your ear? 1) The violin, 2) The trumpet, 3)The piano, 4)The drum "))

if Q3 == 1:
  Slytherin += 4
elif Q3 == 2:
  Hufflepuff += 4
elif Q3 == 3:
  Ravenclaw += 4
elif Q3 == 4:
  Gryffindor += 4
else:
  print("Wrong input")

print("You are this amount of Slytherin:", Slytherin)
print("You are this amount of Hufflepuff:", Hufflepuff)
print("You are this amount of Ravenclaw:", Ravenclaw)
print("You are this amount of Gryffindor:", Gryffindor)

