# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 09:40:25 2024

@author: Nagarajan
"""

import random
import datetime

print("**** Welcome To SBI ****")
print("1. Signup/Register with Bank")
print("2. Exit")
inp = int(input("Enter the option to proceed "))
cnlist=[]
aclist=[]
pwlist=[]
ba=10000
mb=2000
#file = open("bankaccount.txt", "w")

if(inp ==1):
    cn=input("Enter Customer Name: ")
    cnlist.append(cn)
    pw=int(input("Enter the password: "))
    pwlist.append(pw)
    pw1=int(input("Re-Enter the password: "))
    if pwlist[0] != pw1:
        print("Password not match, exiting...")
        exit()
    else:
        an=random.randint(1111111111111111,9999999999999999)
        aclist.append(an)
        print("Account registered with below details. ")
        print("Cust. Name: ",cnlist[0]," - Ac.No. ",aclist[0])
        un1=input("Enter UserName to Login: ")
        pd1=input("Enter Password: ")
        if un1 == cnlist[0] or pd1==pwlist[0]:
            print("Login Success ")
            print("-"*75)
            print("Welcome to SBI, ",cnlist[0],"                  ",datetime.datetime.today())
            print("1.Credit ")
            print("2.Debit ")
            print("Performing Credit Operation")
            print("Balance before credit",ba)
            for i in range(3):
                
                da=int(input("Enter the amount to credit :"))
                ba=ba+da
                print("Total Balance after Deposit: ",ba)
                
                    
            print("Performing Debit Operation")
            print("Balance before debit",ba)
            for i in range(3):
                wa=int(input("Enter the amount to debit :"))
                ba=ba-wa
                if ba <= mb:
                    print("Low Balance:",mb," No further debit allowed")
                    break                    
                else:
                    print()
                print("Total Balance after withdrawal: ",ba)
            
            print("Balance After Transaction: ",ba)
            print("Interest Details @ 10% per Annum: ")
            int1=ba*10/100
            tb=ba+(ba*10/100)
            print("Total Balance: ",tb)
            print("Interest Amount: ",int1)
            print("-"*75)
            
            
        else:
            print("Invalid Credentials")
else:
    print("Exiting the program...")
    exit()


#file.close()    
    
