# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 11:51:03 2024

@author: Admin
"""
import random
tempp=''
num = ['0','1','2','3','4','5','6','7','8','9']
spchar=['<','!','@','#','$','%','^','&','*','(',')','+','-','=','?','>']
chars1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
chars2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
cl=num+spchar+chars1+chars2

print(" *** Complex Password Generator *** ")

pwdlen = int(input("Enter the length of the password to be generated: "))

c1=random.choice(chars1)
c2=random.choice(chars2)
sc1=random.choice(spchar)
n1=random.choice(num)

# def passwordgen():
        
#     tempp=c1+c2+sc1+n1
    
#     for i in range(pwdlen-4):
#         cl1=random.choice(cl)
#         tempp = tempp+cl1
        
#     print(tempp)

if pwdlen < 8:
    print("Password length should be minimum 8. ")
    
else:
    print()

scy = input("Press N if the password should not contain special characters. Y/N ?").upper()
numy = input("Press N if the password should not contain numbers. Y/N ?" ).upper()
sny =  input("Press N if the password should not contain numbers and special characters. Y/N ?" ).upper()

  
if scy == 'N':
    tempp=c1+c2+n1
    tcl1= num+chars1+chars2   
    for i in range(pwdlen-3):
        cl1=random.choice(tcl1)
        tempp = tempp+cl1
            
    print("The generated complex password is ",tempp)
    
elif numy == 'N':
    tempp=c1+c2+sc1
    tcl1= spchar+chars1+chars2   
    for i in range(pwdlen-3):
        cl1=random.choice(tcl1)
        tempp = tempp+cl1
            
    print("The generated complex password is ",tempp)
    
elif sny =='N':
    tempp=c1+c2
    tcl1= chars1+chars2   
    for i in range(pwdlen-2):
        cl1=random.choice(tcl1)
        tempp = tempp+cl1
            
    print("The generated complex password is ",tempp)    
    
else:
    tempp=c1+c2+sc1+n1
    tcl1=chars1+chars2+spchar+num    
    for i in range(pwdlen-4):
        cl1=random.choice(tcl1)
        tempp = tempp+cl1
            
    print("The generated complex password is ",tempp)

 
           
# passwordgen()
