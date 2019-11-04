while True:
    try:
        num = int(input("Enter a number here between 0 and 4000: "))
        if num < 1 or num > 4000:
            raise ValueError
        break
    except ValueError:
        print("Not a number between 1 and 4000")

arabic = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
roman = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')

result = []
for i in range(len(arabic)):
    count = int(num / arabic[i])
    result.append(roman[i] * count)
    num -= arabic[i] * count

print("".join(result))