def calc(v1=22,v2=11):
    result=v1+v2
    print("Addition  of 2 numbers: ",result)
    result = v1 - v2
    print("Subtraction  of 2 numbers: ", result)
    result = v1 * v2
    print("Multi[ly  of 2 numbers: ", result)
    result = v1 / v2
    print("Division  of 2 numbers: ", result)

i1=int(input("Enter a value: "))
i2=int(input("Enter a value: "))
calc()
calc(i1,i2)