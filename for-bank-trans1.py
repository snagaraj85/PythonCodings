c1=input("Enter the Customer Name: ")
bal=0
t1=int(input("Enter the number of transaction to do: "))
for i in range(t1):
    ta=int(input("Enter the amount to add: "))
    bal=bal+ta
print("Total Balance of ",c1," ",bal)

