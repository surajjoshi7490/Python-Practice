class Account:
   
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    
    def deposit(self,deposit_amount):
        self.deposit_amount=deposit_amount
        self.balance+= deposit_amount
        return f"Deposit Accepted of :: ${deposit_amount} "
    
    def withdraw(self,Withdrawal_amount):
        self.Withdrawal_amount=Withdrawal_amount
         
        if Withdrawal_amount<=self.balance:
            self.balance-=Withdrawal_amount
            return f"Withdrawal Accepted of :: ${Withdrawal_amount} "
        else:
            return f"Funds Unavailable!"
        
    
    def Account_detail(self):
        return f"Account Owner :: {self.owner}\nAccount Balance :: ${self.balance}"
    
    
acct1=Account("Jose",100)
print(acct1.Account_detail()) 
print(acct1.owner)
print(acct1.balance)
print(acct1.deposit(50))
print(acct1.withdraw(50))
