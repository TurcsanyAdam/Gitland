num1 = int(input("Enter first number here: "))
num2 = int(input("Enter second number here: "))
divider_num1 = []
divider_num2 = []
common_div = []

for i in range(1, num1+1):
    if num1 % i == 0:
        divider_num1.append(i)

for j in range(1, num2+1):
    if num2 % j == 0:
        divider_num2.append(j)

for x in divider_num1:
    if x in divider_num2:
        common_div.append(x)


print(common_div[-1])