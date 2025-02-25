class User:
    def __init__(self,name,city,balance = 0):
        self.name = name
        self.city = city
        self.balance = balance


class BankAccount(User):
    def __init__(self,name,city,balance=0):
        super().__init__(name,city,balance)


    def deposit(self,amount):
        '''A depost method that adds amount to the balance'''
        
        self.balance += amount
        return f'Deposited {amount}'
    

    def withdrawl(self,amount):
        '''A withdrawl Method that deducts amount from the balance'''

        self.balance -= amount
        return f'withdrew {amount}'
    

    def display(self):
        '''To display individual User'''

        return {'name':self.name,'city':self.city,'balance':self.balance}

class Bank:
    def __init__(self):
        self.database = {}

    def add_account(self,name,city,balance=0):
        '''To add a account to the Bank's database'''

        account = BankAccount(name,city,balance)
        self.database[name] = account

    def display_all(self):
        '''A Method to display all the user in the bank'''

        for key,values in self.database.items():
            print(f'<name = {key}: \tcity = {values.city} \t balance = {values.balance}\t')


bank = Bank()
bank.add_account('User1','Mumbai',0)
bank.add_account('User2','Pune',0)
bank.add_account('User3','Chennai',0)
bank.display_all()
user1 = bank.database['User1']
user1.display()
user1.deposit(12)
user1.withdrawl(12)
