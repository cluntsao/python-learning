"""

Robustness, Adaptability, Reusability

Abstraction is to distill a complicated system down to its most fundamental parts.

Encapsulation: Different components of a software system should not reveal the internal details of their respective implementations. 

Software Development
  - Design
  - Implementation
  - Testing and Debugging

UML (Unified Modeling Language)

Classes: should have a name that serves as a singular noun, and should be capitalized. E.g. Date, CreditCard
Functions: make_payment, calculate_sqrt
_XXXX: for internal use in a class or module

Testing & Debugging:


"""
class CreditCard:

    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._acnt

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount


if __name__ == '__main__':
    wallet = list()
    wallet.append(CreditCard('John Doe', '1st Bank', '5391 0375 9387 5309', 2500))
    wallet.append(CreditCard('John Doe', '1st Bank', '5391 0375 9387 5309', 3500))
    wallet.append(CreditCard('John Doe', '1st Bank', '5391 0375 9387 5309', 5000))

    print(wallet[0].get_account())

    a = 1
    b = 2
    print(a.__add__(b))