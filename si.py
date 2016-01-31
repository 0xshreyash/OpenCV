P = float(input("Enter the Principal: "))
R = float(input("Enter the Rate: "))
T = float(input("Enter the Time: "))
print "The simple interest is :", (P*T*R)/100
print "The amount is :", (P + (P*T*R)/100)