#!python3
from random import randint
print("a", "b")
player = input("Камінь (к), ножниці (н) или папір(п)?")
choice = randint(1, 3)
if choice == 1:
  computer = 'к'
elif choice == 2:
  computer = 'п'
elif choice == 3:
  computer = 'н'
print(player, "vs", computer)

if player == computer:
  print("Нічия!!!")
