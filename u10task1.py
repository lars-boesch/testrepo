from public.currency_converter import convert
from public.exchange_rates import EXCHANGE_RATES

class BankAccount:

    def __init__(self, currency="CHF"):
        if currency in EXCHANGE_RATES:
            self.__currency = currency
        else: raise Warning
        self.__balance = 0

    def get_currency(self):
        return self.__currency

    def get_balance(self):
        return self.__balance
        
    def deposit(self, amount, currency="CHF"):
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise Warning
        if amount < 0:
            raise Warning
        if not isinstance(currency, str):
            raise Warning
        if currency in EXCHANGE_RATES:
            self.__balance += convert(amount, currency, self.__currency)
        else: raise Warning
    
    def withdraw(self, amount, currency="CHF"):
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise Warning
        if amount < 0:
            raise Warning
        if not isinstance(currency, str):
            raise Warning
        if currency in EXCHANGE_RATES:
            self.__balance -= convert(amount, currency, self.__currency)
        else: raise Warning
        if self.__balance < 0:
            raise Warning