startt=int(input("Enter start table to print: "))
stopt=int(input("Enter stop table to print: "))
i=startt
j=1

while i <= stopt:
    while j <= 10:
        print(i,"X",j,"=",i*j)
        j += 1
    i+=1
    j=1

