'''
Write a python program to demonstrate basic banking operations. Create a class named
banking having separate class methods for each operation. Call each method with an
instance of the class and attribute values to be taken from the user.
'''

class BankAccount:
    
    
    def __init__(self,AccNumber,AccHolder,AccBalance):
        self.AccNumber = AccNumber
        self.AccHolder = AccHolder
        self.AccBalance  = AccBalance 
    
 
    def DepositBalance(self,DepositAmount):
        self.AccBalance+=DepositAmount
        print("*"*100)
        print("The Amount Credited.\nThe Account Balance is : ",self.AccBalance)
        

    def WithdrawBalance(self,WithdrawAmount):
        if (WithdrawAmount > self.AccBalance):
            print("*"*100)
            print("You don't have enough balance.")
            print("*"*100)
        else:
            self.AccBalance-=WithdrawAmount
        print("*"*100)
        print("The Amount Debited.\nThe Account Balance is : ",self.AccBalance)
    

    def Display(self):
        print("*"*100)
        print("Account Number : ",self.AccNumber)
        print("Account Holder : ",self.AccHolder)
        print("Account Balance : ",self.AccBalance)
        

def PersonDetails():
    while True:
        try:
            AccNum = int(input("Enter Account Nuimber : "))
            AccName = input("Enter Person Name : ")
            AccBal = float(input("Enter Account Balance : "))
            break
        except Exception:
            print("Invalid Details...\n")
    return AccNum,AccName,AccBal

AccNum1,AccName1,AccBal1 = PersonDetails()

F_Person = BankAccount(AccNum1,AccName1,AccBal1)
print("*"*100)
F_Person.DepositBalance(float(input("Enter Deposit Ammount : ")))
print("*"*100)
F_Person.WithdrawBalance(float(input("Enter Withdrawal Ammount : ")))

F_Person.Display()
print("*"*100)