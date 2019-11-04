x = int(input("Enter a number here: "))

for i in range(x):
    ws = " " * (x -i -1)
    st = "*" * i
    print(ws + st + "*" + st + ws)
