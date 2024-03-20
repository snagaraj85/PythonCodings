"""
Author: Nagarajan.S
Course: Python Programming
Batch: 3.30 PM - 5.30 PM
Descripton: Bank Transaction
"""
import random
import datetime


dt=datetime.datetime.today()
dt1=str(dt)
print("-" * 75)

print("*" *30, "Welcome To SBI", "*" *29)
wo="-" *30 + " Welcome To SBI " + "-" *29

print("-" * 75)

print("1. Signup/Register with Bank")
print("2. Exit")
inp = int(input("Enter the option to proceed "))
cnlist = []
aclist = []
pwlist = []
ba = 10000
mb = 2000


if (inp == 1):
    cn = input("Enter Customer Name: ")
    cnlist.append(cn)
    pw = input("Enter the password: ")
    pwlist.append(pw)
    pw1 = input("Re-Enter the password: ")
    if pwlist[0] != pw1:
        print("Password not match, exiting...")
        exit()
    else:
        print()
    an = random.randint(1111111111111111, 9999999999999999)
    aclist.append(an)
    print("Account registered with below details. ")
    print("Cust. Name: ", cnlist[0], " - Ac.No. ", aclist[0])
    un1 = input("Enter UserName to Login: ")
    pd1 = input("Enter Password: ")
    
    if un1 == cnlist[0] and pd1 == pwlist[0]:
        print("Login Success ")
        print()
        print("-" * 75)
        print("Ac. Name: ",cnlist[0], " "*33, datetime.datetime.today())
        w1="Ac. Name: " + cnlist[0] + " " * 33 + dt1
        
        print("Ac. No: ",aclist[0])
        ac1=str(aclist[0])
        
        print("-" * 75)
        print("Performing Credit Operation")
        print("Initial Balance ", ba)
        

        for i in range(3):
            da = int(input("Enter the amount to credit :"))
            ba = ba + da
            print("Total Balance after Deposit: ", ba)
            print()
            
        print("Performing Debit Operation")
        print("Balance before debit", ba)
        
        for i in range(3):
            wa = int(input("Enter the amount to debit :"))
            ba = ba - wa
            if ba <= mb:
                print("Min Balance to maintain is: ", mb, " No further debit allowed")
                break
            else:
                print("Total Balance after debit: ", ba)
                print()
                
        print("Final Balance After Transactions: ", ba)
        
        print("Interest Details @ 10% per Annum. ")
        
        int1 = ba * 10 / 100
        tb = ba + (ba * 10 / 100)
        print("Interest Amount: ", int1)
        
        print("Total Balance: ", tb)
        
        print("-" * 75)
        w2="-" * 75
        

    else:
        print("Invalid Credentials")
        exit()
else:
    print("Exiting the program...")
    exit()



