class Bank:
    def __init__(self,amt):
        self.amt = amt

    def credit(self):
        d1=int(input("Enter the amount to deposit: "))
        self.amt=self.amt+d1
        print("Balance After Deposit: ",self.amt)
    def debit(self):
        d2=int(input("Enter the amount to withdraw: "))
        self.amt = self.amt - d2
        print("Balance After Withdraw: ",self.amt)

opt = 1
opt1 = 2
amt = Bank(2000)
while opt == 1 or opt1 == 2:
    print("1.Credit")
    print("2.Debit")
    print("3.Exit")

    o1 = int(input("Enter the operation to perform: "))
    if o1==1:
        #c1=Bank()
        amt.credit()
    elif o1==2:
        #c2=Bank()
        amt.debit()
    else:
        exit()

