length = int(input("Enter the side of the square  : "))
for i in range(length):
    for j in range(length):
        if(i == 0 or i == length - 1 or j == 0 or j == length - 1):
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()