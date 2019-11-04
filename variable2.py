date1_hour = int(input("Enter hour of first date: "))
date1_min = int(input("Enter min of first date: "))
date1_sec = int(input("Enter sec of first date: "))
date2_hour = int(input("Enter hour of second date: "))
date2_min = int(input("Enter min of second date: "))
date2_sec = int(input("Enter sec of second date: "))

date1 = (date1_hour) * 3600 + (date1_min)* 60 + (date1_sec)
date2 = (date2_hour) * 3600 + (date2_min)* 60 + (date2_sec)

print(abs(date1 - date2))