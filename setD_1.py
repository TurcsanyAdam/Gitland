while True:
    try:
        a = int(input("Enter a number here between -100 and 100: "))
        if a < -100 or a > 100:
            raise ValueError
        break
    except ValueError:
        print("Not a number between -100 and 100")

while True:
    try:
        b = int(input("Enter a number here between -100 and 100: "))
        if b < -100 or b > 100:
            raise ValueError
        break
    except ValueError:
        print("Not a number between -100 and 100")

while True:
    try:
        c = int(input("Enter a number here between -100 and 100: "))
        if c < -100 or c > 100:
            raise ValueError
        break
    except ValueError:
        print("Not a number between -100 and 100")
while True:
    try:
        d = int(input("Enter a number here between -100 and 100: "))
        if d < -100 or d > 100:
            raise ValueError
        break
    except ValueError:
        print("Not a number between -100 and 100")

while True:
    try:
        e = int(input("Enter a number here between -100 and 100: "))
        if e < -100 or e > 100:
            raise ValueError
        break
    except ValueError:
        print("Not a number between -100 and 100")

while True:
    try:
        f = int(input("Enter a number here between -100 and 100: "))
        if f < -100 or f > 100:
            raise ValueError
        break
    except ValueError:
        print("Not a number between -100 and 100")

A = (a, b)
B = (c, d)
C = (e, f)

area = (a * (d - f) + c * (f - b) + e * (b - d))/2

print(abs(area))