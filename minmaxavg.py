num_list = [-5, 23, 0, "kitten", -9, 12, 99, [2, 44], None, 105, -43]
num_list2 = []
min = 0
max = 0
avg = 0
n = 6

for i in range(n):
    avg += num_list[i]
    if min == 0:
        min += num_list[i]
    elif num_list[i] <= min:
        min = num_list[i]
    if max == 0:
        max += num_list[i]
    elif num_list[i] >= max:
        max = num_list[i]

print(num_list2)
print(min, "érték a legkisebb a számszorban")
print(max, "érték a legnagyobb a számszorban")
print(avg/len(num_list), "az átlaga a számsornak")