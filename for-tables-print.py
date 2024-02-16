t1=int(input("Enter the start table to print: "))
t2=int(input("Enter the end table to print: "))

for i in range(t1,t2):
    for j in range(1, 11):
        print(j, "X", t1, "=", t1 * j)
