# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 09:40:25 2024

@author: Nagarajan
"""

import random
import datetime

file = open("bankaccount.txt", "w")
dt=datetime.datetime.today()
dt1=str(dt)
print("-" * 75)
file.write("-" * 75)
file.write("\n")
print("*" *30, "Welcome To SBI", "*" *29)
wo="-" *30 + " Welcome To SBI " + "-" *29
file.write(wo)
file.write("\n")
print("-" * 75)
file.write("-" * 75)
file.write("\n")
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
    pw = int(input("Enter the password: "))
    pwlist.append(pw)
    pw1 = int(input("Re-Enter the password: "))
    if pwlist[0] != pw1:
        print("Password not match, exiting...")
        exit()
    else:
        an = random.randint(1111111111111111, 9999999999999999)
        aclist.append(an)
        print("Account registered with below details. ")
        print("Cust. Name: ", cnlist[0], " - Ac.No. ", aclist[0])
        un1 = input("Enter UserName to Login: ")
        pd1 = input("Enter Password: ")
        if un1 == cnlist[0] or pd1 == pwlist[0]:
            print("Login Success ")
            print()
            print("-" * 75)
            print("Ac. Name: ",cnlist[0], " "*33, datetime.datetime.today())
            w1="Ac. Name: " + cnlist[0] + " " * 33 + dt1
            file.write(w1)
            file.write("\n")
            print("Ac. No: ",aclist[0])
            ac1=str(aclist[0])
            file.write(ac1)
            file.write("\n")
            print("1.Credit ")
            print("2.Debit ")
            print("-" * 75)
            print("Performing Credit Operation")
            print("Initial Balance ", ba)
            file.write("\n")
            file.write(f"Initial Balance : {ba}\n")
            file.write("\n")
            file.write(f"Balance before credit: {ba}\n")

            for i in range(3):
                da = int(input("Enter the amount to credit :"))
                ba = ba + da
            print("Total Balance after Deposit: ", ba)

            file.write(f"Total Balance after Deposit: {ba}\n")
            print("Performing Debit Operation")
            print("Balance before debit", ba)
            file.write("\n")
            file.write(f"Balance before debit: {ba}\n")
            for i in range(3):
                wa = int(input("Enter the amount to debit :"))
                ba = ba - wa
                if ba <= mb:
                    print("Min Balance to maintain is: ", mb, " No further debit allowed")
                    break
                else:
                    print()
            print("Total Balance after debit: ", ba)
            file.write(f"Total Balance after debit: {ba}\n")
            file.write("\n")
            print("Final Balance After Transaction: ", ba)
            file.write(f"Final Balance after Transactions: {ba}\n")
            print("Interest Details @ 10% per Annum. ")
            file.write(f"Interest Details @ 10% per Annum.\n")
            int1 = ba * 10 / 100
            tb = ba + (ba * 10 / 100)
            print("Interest Amount: ", int1)
            file.write(f"Interest Amount: {int1}\n")
            print("Total Balance: ", tb)
            file.write(f"Total Balance: {tb}\n")
            print("-" * 75)
            w2="-" * 75
            file.write(w2)
            file.write("\n")


        else:
            print("Invalid Credentials")
            exit()
else:
    print("Exiting the program...")
    exit()

file.close()
