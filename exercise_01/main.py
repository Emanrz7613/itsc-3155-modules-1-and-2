from BankAccount import BankAccount


acct=BankAccount("Eric",2547.33)
acct.deposit(400)
acct.withdraw(200)
print(acct.get_balance())