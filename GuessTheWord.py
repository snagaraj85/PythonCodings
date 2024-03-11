# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 11:47:14 2024

@author: Admin
"""
import random

list1=['apple','bat','car','dog','eagle','fish','goat','horse','icecream','jug']

l1=random.choice(list1)
chance=10
ug=''

while chance > 0:
    fail = 0
    for ch in l1:
        if ch in ug:
            print(ch)
        else:
            print("-")
            fail += 1
    if fail == 0:
        print("You won!, The word is ",l1)
        break
             
    ug1=input("Enter a character to guess: ") 
    ug+=ug1
    if ug1 not in l1:
        chance-=1
        print("Incorrect")
        print("You have ",chance, "chances left. ")
        if chance == 0:
            print("You Lose...The word is ",l1)
            
    
    


