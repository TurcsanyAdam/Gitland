min = 0
n = 5
for i in range(n):
    y = int(input("Enter a number here:"))
    if min == 0:
        min = min +y
    elif y <= min:
        min =+ y
print(min)