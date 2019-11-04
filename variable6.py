amount = int(input("Enter money to be exchanged: "))

money1 = 10
money2 = 5
money3 = 2
money4= 1


min_coins = ((amount//money1) + (amount%money1//money2) + ((amount%money1)%money2//money3) + (((amount%money1)%money2)%money3)//money4)

print(min_coins)