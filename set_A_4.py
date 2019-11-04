import random

num1 = (random.randint(1,6))
num2 = (random.randint(1,6))
num3 = (random.randint(1,6))
num4 = (random.randint(1,6))
num5 = (random.randint(1,6))

defender_count = 0
attacker_limit = 3
defender_limit = 2

while True:
    try:
        attacker_count = int(input("How many units attack (1-3): "))
        if attacker_count < 1 or attacker_count > 3:
            raise ValueError
        break
    except ValueError:
        print("Invalid integer. The number must be in the range of 1-3.")

while True:
    try:
        defender_count = int(input("How many units attack (1-2): "))
        if defender_count < 1 or defender_count > 2:
            raise ValueError
        break
    except ValueError:
        print("Invalid integer. The number must be in the range of 1-2.")

attacker_unit = 0
defender_unit = 0

if attacker_count == 1 and defender_count == 1:
    print(num1)
    print(num4)
    if num1 > num4:
        defender_unit += 1
    else:
        attacker_unit += 1


if attacker_count == 2 and defender_count == 1:
    print(num1, num2)
    print(num4)
    if num1 > num4:
        defender_unit += 1
    else:
        attacker_unit += 1

if attacker_count == 3 and defender_count == 1:
    print(num1, num2, num3)
    print(num4)
    if num1 > num4:
        defender_unit += 1
    else:
        attacker_unit += 1

if attacker_count == 2 and defender_count == 2:
    print(num1, num2)
    print(num4, num5)
    if num1 > num4:
        defender_unit += 1
    else:
        attacker_unit += 1
    if num2 > num5:
        defender_unit += 1
    else:
        attacker_unit += 1

if attacker_count == 3 and defender_count == 2:
    print(num1, num2, num3)
    print(num4, num5)
    if num1 > num4:
        defender_unit += 1
    else:
        attacker_unit += 1
    if num2 > num5:
        defender_unit += 1
    else:
        attacker_unit += 1

if attacker_count == 1 and defender_count == 2:
    print(num1)
    print(num4, num5)
    if num1 > num4:
        defender_unit += 1
    else:
        attacker_unit += 1

print(" Attacker lost", attacker_unit, "units\n","Defender lost", defender_unit, "units")
