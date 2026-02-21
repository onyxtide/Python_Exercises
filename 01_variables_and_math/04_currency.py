#This asks the user how much money in different currencies they have available and then transforms the sum into USD
pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))
USD = int((pesos * 3703.70) + (soles * 3.33) + (reais * 5.26))
print(USD)
