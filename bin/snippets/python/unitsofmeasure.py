from decimal import Decimal

amount_spent_in_usd = Decimal('99.99')
amount_spent_in_eur = Decimal('79.99')
one_eur_in_usd = Decimal('1.293')

total_spent_in_usd = amount_spent_in_usd + amount_spent_in_eur ### Ooooops!

class CurrencyAmount(object):
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency.upper()

    def __add__(self, other):
        assert isinstance(other, CurrencyAmount), 'can only sum valuta amounts'
        assert self.currency == other.currency, 'can only add same currencies,' +\
             'but tried to add %s to %s' % (other.currency, eur.currency)
        return type(self)(amount = self.amount + other.amount)

class Eur(CurrencyAmount):
    def __init__(self, amount):
        CurrencyAmount.__init__(self, amount, 'EUR')

class Usd(CurrencyAmount):
    def __init__(self, amount):
        CurrencyAmount.__init__(self, amount, 'USD')

total_spent_in_usd = Eur('79.99') + Usd('99.99')
# Traceback (most recent call last):
#   File "unitsofmeasure.py", line 28, in <module>
#     total_spent_in_usd = Eur('79.99') + Usd('99.99')
#   File "unitsofmeasure.py", line 17, in __add__
#     'but tried to add %s to %s' % (self.currency, other.currency)
# AssertionError: can only add same currencies,but tried to add EUR to USD

