def square_digits(num):
    num_sq = 0
    for d in range(num+1):
        num_sq += d
    return num_sq


print(square_digits(100))