#!python3
from random import randint
player = input("Камінь (к), ножниці (н) или папір(п)?")
choice = randint(1, 3)
print(player, "vs", choice)
