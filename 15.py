class Customer():

    def __init__(self, name, address, age, money):
        self.name = name
        self.address = address
        self.age = age
        self.balance = money

    def deposit_money(self, money):
        self.balance += money

    def withdraw_money(self, money):
        self.balance -= money
