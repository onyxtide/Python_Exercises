#Calculate the bill and divide it four ways. Store what each person has to pay in a my_share variable
total = 0
bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]

for i in bill:
  total = total + i

my_share = total/4

print(my_share)
