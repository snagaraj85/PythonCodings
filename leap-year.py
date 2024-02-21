inp = int(input("Enter the year to find its leap years: "))
inpend = inp+100
for i in range(inp,inpend,4):
    if i % 4 == 0:
        print(i," is leap year",end="\n")
    else:
        print(i," is not leap year")