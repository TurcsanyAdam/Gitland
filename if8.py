min = 0
max = 0
n = 5
for i in range(n):
    y = int(input("Enter a number here:"))
    if min == 0 and max ==0:
        min = min + y
        max = max + y
    elif y <= min:
        min =+ y
    elif y >= max:
        max =+ y
print("A legkisebb szám: " + str(min) + " A legnagyobb szám: " + str(max))