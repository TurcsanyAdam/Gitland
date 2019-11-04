numbers = []
lenght = int(input("Enter lenght here: "))

for i in range(lenght):
    numbers.append(int(input("Enter a number here: ")))
n = len(numbers)


x = 1
while x < n:
    j = 0
    while j <= n - 2:
        if numbers[j] > numbers[j+1]:
            temp = numbers[j+1]
            numbers[j+1] = numbers[j]
            numbers[j] = temp
        else:
            j += 1
    else:
        x += 1


print(numbers)
