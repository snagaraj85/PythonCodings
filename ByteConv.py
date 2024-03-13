n=int(input("Enter a number: "))
# print(bin(n))
# print(oct(n))
# print(hex(n))
# b1=bin(n)
# o1=oct(n)
# h1=hex(n)
# print("Decimal Value is ",n)
# print("Binary Value is ",b1[2:])
# print("Octal Value is is ",o1[2:])
# print("HexaDecimal Value is ",h1[2:])
i=0
while i<=n:
    print("Binary : ",bin(i))
    print("Octal : ",oct(i))
    print("HexaDecimal : ",hex(i))
    i+=1


