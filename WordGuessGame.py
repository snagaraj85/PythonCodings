"""
Author: Nagarajan.S
Course: Python Programming
Batch: 3.30 PM - 5.30 PM
Descripton: Word Guess Game
"""
import random

list1=['resin','rinse','siren','paste','tapes','listen','silent','fried','fired','care','race','steal','slate','lime','mile','least','tales','tied','tide','heart','earth','break','brake','miles','slime','smile','stone','notes','tones','later','later','alert','parts','strap','traps']

l1=random.choice(list1)
le=len(l1)
chance=10
ug=[]
while chance > 0:
    fail = 0
    if len(ug) == len(l1):
        print("--------------------------------------------------")
        print("You correctly guessed all letters in the word: ",ug)
        word = input("Now enter the correct word which was guessed: ")
        if word != l1:
            print("You Lost... The guessed word is ","'",l1,"'")
            break
        else:
            print("You Won.!!! The guessed word is ","'",l1,"'")
            break
    print("Guess the word: ","_ "*le)
    ch = input("Enter a letter to guess: ")
    if ch in l1:
        if ch in ug:
            print("Already Guessed Letter, Try Different")
        else:
            #print(ch)
            ug.append(ch)
            print(ug)
            
    else:
        print("Incorrect")
        chance-=1
        print(f"You have left with {chance} chances to try")

if chance == 0:
    print("You Lost...The guessed word is ","'",l1,"'")
        
   


