s1=int(input("Enter the start table: "))
s2=int(input("Enter the stop table: "))
for i in range(s1,s2+1):
    for j in range(1,11):
        print(i,"X",j,"=",j*i)
