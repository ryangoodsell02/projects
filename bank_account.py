
class BankAccount:
    # TODO - define attributes
    def __init__(self, acct_id, first_name, last_name):
        self.acct_id = acct_id
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0.0

        # TODO - define methods
        # TODO - other items as mentioned in our requirements

    def __str__(self):
        # TODO - create a str that contains the values of the attributes
        return str(self.acct_id) + " Name: " + self.first_name \
            + " " + self.last_name + " Balance: $" + str(self.balance)

    def deposit(self, amount):
        # TODO - update the balance
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient Funds. Tried to withdraw " + str(amount)
                + " but only have " + str(self.balance))

        self.balance = self.balance - amount
        print(str(amount) + " withdrawn from account " + str(self.acct_id))


    def transfer_from(self, amount, to_account):
        self.withdraw(amount)
        to_account.deposit(amount)

def main():
    acct1 = BankAccount(123, "Joe", "Smith")
    acct2 = BankAccount(345, "Jane", "Doe")
    print("Before deposit:", acct1)
    acct1.deposit(500.00)
    print("After deposit:", acct1)

    print("Before withdraw:", acct1)
    try:

        # acct1.withdraw(550.00)
        acct1.transfer_from(525.00, acct2)

    except ValueError as e:
        print(e)
        # print("Could not withdraw the amount")

    print("After withdraw:", acct1)

    print("After transfer:", acct2)

main()