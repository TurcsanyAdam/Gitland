n = int(input("Enter a number here: "))
even = 0
odd = 0
odd_sum = 0

for i in range(n):
    if i % 2 == 0:
        even = even +1
    else:
        odd = odd +1
        odd_sum = odd_sum + i

print(even, odd, odd_sum)