A = int(input("Give length of A side: "))
B = int(input("Give length of B side: "))
C = int(input("Give length of C side: "))

if (A*A + B*B) == C*C:
    print("Derékszögű a háromszög")
else:
    print("Nem derékszögű a háromszög")