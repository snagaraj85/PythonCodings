"""
Desc: Banking System

Author: Nagarajan.S
"""
import datetime

#dt=datetime.datetime.now()
#print(dt.strftime("%d-%b-%Y %H:%M:%S"))
ua="Admin"
apwd='6666'
userlist=[]
pwlist=[]
cnlist=[]
aclist=[]
addrlist=[]
initialbal=[]
acst=[]



while True:
    
    print("1.User Registration")
    print("2.User Login")
    print("3.Admin Login")
    print("4.Exit")
    
    
    
    opt = int(input("Select the option: "))
    
    def createAcnts():
        name = input("Enter the Name: ")
        pwd = input("Enter the Password: ")
        while True:
            try:
                cn = int(input("Enter the Contact No. "))
                break
            except:
                print("Invalid Contact Number, Only Numbers allowed")        
        addr = input("Enter the Location: ")
        while True:
            try:
                ac=int(input("Enter the Acnt. No. "))
                break
            except:
                print("Invalid Account Number, Only Numbers allowed")
                
        ib = 1000
        acst = True                            
        
        userlist.append(name)
        pwlist.append(pwd)
        cnlist.append(cn)
        addrlist.append(addr)
        aclist.append(ac)
        initialbal.append(ib)
        print("-"*50)
        print("Account Registered with below details: ")
        print("Name: ",name,"\nAc.No: ",ac)
        print("Address: ",addr,"\nContact.No: ",cn)
        print("Account Balance: ",ib)
        print("-"*50)
        
    def Userlogin():
        
        while True:
            
            un1 = input("Enter UserName to Login: ")
            pd1 = input("Enter Password: ")
        
            if un1 not in userlist:
                print("Invalid User")
                
            elif pd1 not in pwlist:
                print("Invalid Password")
                                            
            else:
                n=userlist.index(un1)
                break
            
        if un1 == userlist[n] and pd1 == pwlist[n]:
            print("Login Success")
                                
            while True:
                print("*** Banking Sub Menu ***")
                print("1.Deposit")
                print("2.Withdrawls")
                print("3.Statements")
                print("4.Modify Personal Info")
                print("5.Exit")
                
                opt1=int(input("Select the option: "))
                
                if opt1 == 1:
                    while True:
                        try:
                            print("Current Balance: ",initialbal[n])
                            dp = int(input("Enter the amount to deposit: "))
                            temp = dp+initialbal[n]
                            initialbal[n] = temp
                            print("Amount Deposited, Account Balance",initialbal[n])
                            break
                        except:
                            print("Invalid Amount Entered")
                    
                if opt1 == 2:
                                                                                            
                    try:
                        while True:
                            print("Current Balance: ",initialbal[n])
                            wd = int(input("Enter the amount to withdrawl: "))
                            temp = initialbal[n] - wd
                            if temp < 1000:
                                print("Low Balance,Min Balance to Maintain is 1000, Transaction not allowed")
                                break
                            else:
                                initialbal[n] = temp
                                print("Amount Withdrawn, Account Balance",initialbal[n])
                                break                             
                            
                    except:
                        print("Invalid Amount Entered")
                if opt1 == 3:
                    dt=datetime.datetime.now()
                    print("-"*50)
                    print("Acnt. Name: ",userlist[n],"\t"*3,dt.strftime("%d-%b-%Y %H:%M:%S"))
                    print("Acnt. No",aclist[n])
                    print("-"*50)
                    print("Account Balance: ",initialbal[n])
                    print("-"*50)
                    print("Address: ",addrlist[n],"\t"*3,"Contact No: ",cnlist[n])
                    print("-"*50)
                if opt1 == 4:
                    while True:
                    
                        print("*** Update Personal Info ***")
                        print("1.Name")
                        print("2.Contact No.")
                        print("3.Address")
                        print("4.Exit")
                    
                        opt2=int(input("Select the option to update Personal Info: "))
                    
                        if opt2==1:
                            n1=input("Enter the New Name: ")
                            userlist[n] = n1
                            print("Name Updated")
                        if opt2==2:
                            c1=input("Enter New Contact No. ")
                            cnlist[n] = c1
                            print("Contact Updated")
                        if opt2==3:
                            a1=input("Enter New Address. ")
                            addrlist[n] = a1
                            print("Address Updated")
                        if opt2==4:
                            break                    
                    
                if opt1 == 5:
                    break
            
        else:
            print("UserName or Password Incorrect")    
    
    def adminmgmt():
        
                  
        alogin = input("Enter admin name: ")
        apwd = input("Enter admin password: ")
        
        if alogin == 'Admin' and apwd == '6666':
            print("Admin Login Validated")
            while True:
                print("*** Admin Menu ***")
                print("1.View Reports")
                print("2.Delete Customers")
                print("3.UnLock Users")
                print("4.Exit")
                    
                opt3 = int(input("Enter the Options: "))
                    
                if opt3==1:
                    print("-"*50)
                    print("Ac. Name","Ac.No","Address","Balance")
                    print("-"*50)
                    for i in range(len(userlist)):
                        print(userlist[i],aclist[i],addrlist[i],initialbal[i])
                    print("-"*50)
                    break
                if opt3==2:
                    print("-"*50)
                    print("Ac. Name","Ac.No","Address","Balance")
                    print("-"*50)
                    for i in range(len(userlist)):
                        print(userlist[i],aclist[i],initialbal[i])
                    print("-"*50)
                    dc = input("Enter the customer name to delete: ")
                    ind = userlist.index(dc)
                    userlist.pop(ind)
                    aclist.pop(ind)
                    cnlist.pop(ind)
                    addrlist.pop(ind)
                    initialbal.pop(ind)
                    pwlist.pop(ind)
                    acst.pop(ind)
                    print("* Customer Account Deletd *")
                    print("-"*50)
                    print("Ac. Name","Ac.No","Address","Balance")
                    print("-"*50)
                    for i in range(len(userlist)):
                        print(userlist[i],aclist[i],initialbal[i])
                    print("-"*50)
                    break
                if opt3==3:
                    pass                
                if opt3==4:
                    break
        else:
            print("Invalid Admin Credetials")
                    
                
        
    
    if opt==1:
        createAcnts()    
    if opt==2:
        Userlogin()
    if opt==3:
        adminmgmt()
    if opt==4:
        break
    




