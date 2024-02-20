i1=[]
i1=input("enter the numbers: ").split()
print(i1)
a = int(i1[0])
b = int(i1[1])
c = int(i1[2])
if a > b and a > c:
    print("a is greater",a)
elif b > c and b > a:
    print('b is greater',b)
else:
    print('c is greater',c)
if a < b and a < c:
    print("a is lesser ",a)
elif b < c and b < a:
    print('b is lesser ',b)
else:
    print('c is lesser',c)
