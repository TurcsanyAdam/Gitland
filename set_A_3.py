Fibonacchi_num = [0,1,]
n = int(input("Enter lenght here: "))

for i in range(n):
    Fibonacchi_num.append(Fibonacchi_num [i] + Fibonacchi_num[i+1])

x = len(str((Fibonacchi_num[-1])))
l = " "

for i in Fibonacchi_num:
    y = len(str(i))
    print((x-y) * l + str(i))
