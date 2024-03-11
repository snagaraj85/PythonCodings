# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 13:57:40 2024

@author: Admin
"""
import datetime

users = ['shiva', 'raj', 'kumar']
pins = ['1111', '2222', '3333']
amounts = [1000, 2000, 3000]
count = 0
std=[]
stcd=[]
sta=[]

print("****************************************************************************")
print("*                                                                          *")
print("*                         WELCOME TO SBI ATM                            *")
print("*                                                                          *")
print("****************************************************************************")
while True:
    user = input('\nENTER USER NAME: ')
    user = user.lower()
    if user in users:
        if user == users[0]:
            n = 0
        elif user == users[1]:
            n = 1
        else:
            n = 2
        break
    else:
        print('----------------')
        print('INVALID USERNAME')
        print('----------------')


while count < 3:
    print('------------------')
    pin = input('PLEASE ENTER PIN: ')
    print('------------------')
    if pin.isdigit():
        if user == 'shiva':
            if pin == pins[0]:
                break
            else:
                count += 1
                print('-----------')
                print('INVALID PIN')
                print('-----------')
                print()

        if user == 'raj':
            if pin == pins[1]:
                break
            else:
                count += 1
                print('-----------')
                print('INVALID PIN')
                print('-----------')
                print()

        if user == 'kumar':
            if pin == pins[2]:
                break
            else:
                count += 1
                print('-----------')
                print('Invalid PIN')
                print('-----------')
                print()
    else:
        print('------------------------')
        print('Incorect PIN details...')
        print('------------------------')
        count += 1


if count == 3:
    print('-----------------------------------')
    print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING... ')
    print('!! YOUR CARD HAS BEEN BLOCKED !!')
    print('-----------------------------------')
    exit()

print('-------------------------')
print('LOGIN SUCCESS, CONTINUE')
print('-------------------------')
print()
print('--------------------------')
print(str.capitalize(users[n]), 'Welcome to SBI ATM')
print('----------ATM MENU-----------')

while True:
    
    print('-------------------------------')
    response = input(
        'CHOOSE FROM FOLLOWING OPTIONS: \n[S]tatement \n[W]ithdraw \n[D]eposit  \n[C]hange PIN \n[Q]uit \nType Your Choices: ').lower()
    print('-------------------------------')
    valid_responses = ['s', 'w', 'd', 'p', 'q']
    response = response.lower()
    if response == 's':
        print('---------------------------------------------')
        print('Statement of Account Holder -',str.capitalize(users[n]) )
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")," --- ", amounts[n])
        print('---------------------------------------------')

    elif response == 'w':
        print('---------------------------------------------')
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
        print('---------------------------------------------')
        if cash_out % 100 != 0:
            print('------------------------------------------------------')
            print('WITHDRAWL SHOULD BE IN 100 RUPEES NOTES')
            print('------------------------------------------------------')
        elif cash_out > amounts[n]:
            print('-----------------------------')
            print('YOU HAVE INSUFFICIENT BALANCE')
            print('-----------------------------')
        else:
            amounts[n] = amounts[n] - cash_out
            print('-----------------------------------')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
            print('-----------------------------------')

    elif response == 'd':
        print()
        print('---------------------------------------------')
        cash_in = int(input('ENTER AMOUNT YOU WANT TO DEPOSIT: '))
        print('---------------------------------------------')
        print()
        if cash_in % 100 != 0:
            print('----------------------------------------------------')
            print('DEPOSIT AMOUNT TO MATCH 100 RUPEES NOTES')
            print('----------------------------------------------------')
        else:
            amounts[n] = amounts[n] + cash_in
            print('----------------------------------------')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
            print('----------------------------------------')
    elif response == 'c':
        print('-----------------------------')
        new_pin = int(input('ENTER A NEW PIN: '))
        print('-----------------------------')
        print('------------------')
        new_ppin = int(input('RE-ENTER NEW PIN: '))
        print('-------------------')
        if new_ppin != new_pin:
                print('------------')
                print('PIN MISMATCH')
                print('------------')
        else:
                pins[n] = new_pin
                print('------------')
                print('NEW PIN SAVED')
                print('------------')
    elif response == 'q':
        break
    else:
        print('------------------')
        print('Invalid Option Choosen...')
        print('------------------')
