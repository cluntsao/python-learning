from CreditCard import CreditCard

class PredatoryCreditCard(CreditCard):
    
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        success = super().charge(price)

        if not success:
            self._balance += 5
        
        return success

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

def main():
    card1 = PredatoryCreditCard('John Doe', '1st Bank', '5391 0375 9387 5309', 2500, 0.01)
    print(card1.get_account())
    card1.charge(1500)
    print(card1.get_balance())
    card1.process_month()
    print(card1.get_balance())
    
if __name__ == '__main__':
    main()