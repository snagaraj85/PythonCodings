"""
Author: Nagarajan
Date: 16/02/2024
Batch: 3.30 - 5.30 PM
Desc: Credit/Debit with for loop
"""
c1=input("Enter the Customer Name: ")
print("1.Credit")
print("2.Debit")
bal=0
o1=int(input("Enter the option: "))
if o1==1:
    t1 = int(input("Enter the number of transaction to do: "))
    for i in range(t1):
        ta = int(input("Enter the amount to add: "))
        bal = bal + ta
        print("Total Balance of ", c1, " ", bal)

#bal=10000
elif o1==2:
    t1=int(input("Enter the number of transaction to do: "))
    bal=10000
    for i in range(t1):
        ta=int(input("Enter the amount to debit: "))
        bal=bal-ta
        if bal<5000:
            print("Balance is low,can't debit ")
            exit()
        else:
            print("Proceeding further ")
            print("Total Balance of ",c1," ",bal)
else:
    print("Invalid option")
