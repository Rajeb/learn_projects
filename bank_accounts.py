
class BlanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(
            f"\nAccount '{self.name}' created.\n Balance = ${self.balance:.2f}")
        
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
        
    ##Add deposit method
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.getBalance()  
        
    ### Add withdraw method but needs to check balance before withdraw to see if the withdraw amount is valid or not######################
    ## need to add error by adding "Exception Class" by checking the viable transaction    
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else: 
            raise BlanceException(
            f"\nSorry, account '{self.name}' only has a balance of ${self.balance: .2f}"
        )
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount) # check if that exception is met or not
            self.balance = self.balance - amount
            print("\nWithdraw Complete.")
            self.getBalance()
        except BlanceException as error:
            print(f'\nWithdraw interrupted. {error}')
            
    ## add transfer method
    def transfer(self, amount, account):
        try:
            #print(f"\n'{self.name}'  has a before transfer balance of ${self.balance: .2f}")
            print('\n**********\n\nBegining transfer.... 🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Complete ✅\n\n**********')
        except BlanceException as error:
            print(f'transfer interrupted. 👎 {error}')
            
            
# Start a new class and use inheritance from BankAccount    
    
class InterestRewardsAcc(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit Completed.")
        self.getBalance()
        
        