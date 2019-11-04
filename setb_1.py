num_list = []

for i in range(100,1000):
    if i % 7 == 0 or i % 9 == 0:
        num_list.append(i)
    num_list.reverse()
print(num_list[0:25])