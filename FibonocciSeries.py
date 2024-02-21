inp=int(input("Enter the number of fibonacci series to print: "))
n1=0
n2=1
nd=n2
#i=1
for i in range(1,inp+1):
#while i <= inp:
    print(nd,end=" ")
    n1=n2
    n2=nd
    nd=n1+n2
    #i += 1
#print()


