s1=int(input("Enter the stop table: "))
s2=int(input("Enter the start table: "))
for i in range(s2,s1+1):
    for j in range(1,11):
        print(i,"X",j,"=",j*i)