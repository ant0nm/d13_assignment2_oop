import random
from zombie import Zombie

# testing out the Zombie class
print(Zombie.horde)

print()
print("Day 1:")
Zombie.new_day()
print(Zombie.horde)
print("List of all the zombies:")
for zombie in Zombie.horde:
    print('*', zombie)
print("Deadliest zombie:")
print(Zombie.deadliest_zombie())
zombie1 = Zombie.horde[0]
zombie2 = Zombie.horde[1]
print("The 2 zombies:")
print(zombie1)
print(zombie2)
print(zombie1.encounter())
print(zombie2.encounter())

print()
print("Day 2:")
Zombie.new_day()
print(Zombie.horde)
print("List of all the zombies:")
for zombie in Zombie.horde:
    print('*', zombie)
print("Deadliest zombie:")
print(Zombie.deadliest_zombie())
zombie1 = Zombie.horde[0]
zombie2 = Zombie.horde[1]
print("The 2 zombies:")
print(zombie1)
print(zombie2)
print(zombie1.encounter())
print(zombie2.encounter())
