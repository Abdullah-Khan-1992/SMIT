

# 01
def create_bank_account(name, balance=0):

    account = { name:'John Doe', 'balance': balance, 'transactions' : []}
    return account


# 02

def deposit_money(account, amount):
    if amount > 0 :
        account['balance'] += amount
        account['transactions'].append(f"Deposit: +{amount}, Balance: {account['balance']}")
        print(f'Deposited {amount}. New balance:{account['balance']}')
    else:
        print("Sorry! You have not enough amount to deposit")

# 03

def withdraw_money(account, amount):
    if account['balance'] > amount:
        account['balance'] -= amount
        account['transactions'].append(f'withdrawal: -{amount}, Balance: {account['balance']}')
        print(f"withdrew {amount}. New balance:{account['balance']}")
    else:
        print("Error: Insufficient balance")

# 04

def Check_balance(account):
    print(f"Current balance: {account['balance']}")

# 05

def Print_Statement(account):
    print(f"Account statement for {account['John Doe']}")
    for transaction in account['transactions']:
        print(transaction)


account = create_bank_account('John Doe',0)
deposit_money(account,20000)
withdraw_money(account,10000)
Check_balance(account)
Print_Statement(account)