# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:41:18 2024

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

pwdlen = input("Enter the length of the password to be generated: ")

def passwordgen(pl):
    
    if pl.isdigit():
           
        c1=random.choice(chars1)
        c2=random.choice(chars2)
        sc1=random.choice(spchar)
        n1=random.choice(num)
        
        pl = int(pl)
        if pl < 8:
            print("Password length should be minimum 8. ")
            exit()
        else:
            print()
        
        print("----------------------------------------------------------")
        print("                COMPLEX PASSWORD GENERATOR                ")
        print("1. Password should not contain special characters ")
        print("2. Password should not contain numerals ")
        print("3. Password should not contain special characters & numerals ")
        print("4. Password with all combinations ")
        print("5. Quit the program ")
        print("----------------------------------------------------------")
        opt = int(input("Select the option to generate the password: "))
        
          
        if opt == 1:
            tempp=c1+c2+n1
            tcl1= num+chars1+chars2   
            for i in range(pl-3):
                cl1=random.choice(tcl1)
                tempp = tempp+cl1
                    
            print("The generated complex password is ",tempp)
            
        if opt == 2:
            tempp=c1+c2+sc1
            tcl1= spchar+chars1+chars2   
            for i in range(pl-3):
                cl1=random.choice(tcl1)
                tempp = tempp+cl1
                    
            print("The generated complex password is ",tempp)
            
        if opt == 3:
            tempp=c1+c2
            tcl1= chars1+chars2   
            for i in range(pl-2):
                cl1=random.choice(tcl1)
                tempp = tempp+cl1
                    
            print("The generated complex password is ",tempp)    
            
        if opt == 4:
            tempp=c1+c2+sc1+n1
            tcl1=chars1+chars2+spchar+num    
            for i in range(pl-4):
                cl1=random.choice(tcl1)
                tempp = tempp+cl1
                    
            print("The generated complex password is ",tempp)
        
        if opt == 5:
            exit()
    
    else:
        print("Invalid input entered...")
           
passwordgen(pwdlen)
