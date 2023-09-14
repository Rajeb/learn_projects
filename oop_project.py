from bank_accounts import *

Dave = BankAccount(1000, 'Dave')

Sara = BankAccount(1500, 'Sara')

# Dave.getBalance()
# Sara.getBalance()

# Sara.deposit(500)


Dave.withdraw(10)
Dave.transfer(10000, Sara)
Dave.transfer(100, Sara)


Jim= InterestRewardsAcc(500, "Jim")
Jim.getBalance()
Dave.getBalance()
Jim.transfer(500, Dave)
Jim.getBalance()