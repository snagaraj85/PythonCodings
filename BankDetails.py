# import random
# import datetime
#
# print("**** Welcome To SBI ****")
# print("1. Register/Transact with Bank")
# print("2. Exit")
# inp = int(input("Enter the option to proceed "))
# cnlist = []
# aclist = []
# pwlist = []
#
# if (inp == 1):
#     cn = input("Enter Customer Name: ")
#     cnlist.append(cn)
#     pw = int(input("Enter the password: "))
#     pwlist.append(pw)
#     an = random.randint(1111111111111111, 9999999999999999)
#     aclist.append(an)
#     print("Account registered with below details. ")
#     print("Cust. Name: ", cnlist[0], " - Ac.No. ", aclist[0])
#     un1 = input("Enter UserName to Login: ")
#     pd1 = input("Enter Password: ")
#     if un1 == cnlist[0] or pd1 == pwlist[0]:
#         print("Login Success ")
#         print("----------------------------------------------------------------------")
#         print("Welcome to SBI, ", cnlist[0], "                  ", datetime.date.today())
#         print("1.Credit ")
#         print("2.Debit ")
#         t1 = int(input("Select Credit or Debit: "))
#         if t1 == 1:
#             ba = 1000
#             da = int(input("Enter the amount to deposit :"))
#             ba = ba + da
#             print("Total Balance after Deposit: ", ba)
#             print("Interest Details @ 10% Per Annum: ")
#             int1 = ba * 10 / 100
#             tb = ba + (ba * 10 / 100)
#             print("Total Balance: ", tb)
#             print("Interest Amount: ", int1)
#             print("----------------------------------------------------------------------")
#         elif t1 == 2:
#             ba = 1000
#             wa = int(input("Enter the amount to withdraw :"))
#             ba = ba - wa
#             print("Total Balance after withdrawal: ", ba)
#             print("Interest Details @ 10% per Annum: ")
#             int1 = ba * 10 / 100
#             tb = ba + (ba * 10 / 100)
#             print("Total Balance: ", tb)
#             print("Interest Amount: ", int1)
#             print("----------------------------------------------------------------------")
#         else:
#             print("Invalid option entered.")
#     else:
#         print("Invalid Credentials")
# else:
#     print("Invalid input")
#     # exit()
#
#
#
# number   = 1
#
# while  number <= 10:
#     print(number)
# number+=1

for i in range(1,11):
    print(i)