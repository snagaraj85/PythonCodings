import random
import datetime

print("**** Welcome To SBI ****")
print("1. Register/Transact with Bank")
print("2. Exit")
inp = int(input("Enter the option to proceed "))
cnlist=[]
aclist=[]
pwlist=[]

if(inp ==1):
    cn=input("Enter Customer Name: ")
    cnlist.append(cn)
    pw=int(input("Enter the password: "))
    pwlist.append(pw)
    an=random.randint(1111111111111111,9999999999999999)
    aclist.append(an)
    print("Account registered with below details. ")
    print("Cust. Name: ",cnlist[0],'\n',"Ac.No. ",aclist[0])
    un=input("Enter UserName to Login: ")
    pwd=input("Enter Password: ")

    if cnlist[0] == un and pwlist[0] == pwd:
        print("Login Success. ")
        print("---- Welcome to SBI ", cnlist[0], " ----")
        print("C.Name: ",cnlist[0],"                     ",datetime.date.today())
    else:
        print("login failed")
else:
    exit()
