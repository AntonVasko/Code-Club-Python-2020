#!python3
from random import randint
number = randint(1, 4)
if number == 1:
  print("Один")
elif number == 3:
  print("Три")
else:
  print("Не один і не три, а щось інше:", number)
print("Кінець")
