
class BankAccount:

    def __init__(self, owner = 'John Doe', balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insufficient funds.')

    def __str__(self):
        return('{}: {}'.format(self.owner, self.balance))

def main():
    pass
#add stuff in here for tests

if __name__ == '__main__':
    main()

