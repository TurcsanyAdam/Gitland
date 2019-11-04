T = int(input("Enter a year here: "))
A = T%19
B = T%4
C = T%7
D = (19 * A + 24) % 30
E = (2 * B + 4 * C + 6 * D + 5)%7
H = 22 + D + E

if H <= 31:
    print("Húsvét március " + str(H) + " -ra esik")
elif E == 6 and D == 29:
    print("Nem hústvét vasárnap")
elif E == 6 and D == 28 and A > 10:
    print("Nem húsvét vasárnap")
else:
    print("Húsvét április " + str(H-31) + " -ra esik")
