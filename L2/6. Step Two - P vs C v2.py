#!python3
from random import randint
player = input("Камень (к), ножницы (н) или бумага(б)?")
choice = randint(1, 3)
if choice == 1:
  computer = "к"
elif choice == 2:
  computer = "п"
else: 
  computer = "н"
print(player, "vs", computer)
