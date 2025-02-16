from decimal import Decimal
class Tax:
    taxes_percent = {range(0,1000):10,range(0,10000):20, range(0,10_000_000):25}
    def __init__(self,*args:Decimal):
        self.__income = args
        self.__sum_income = sum(self.__income)
        self.__tax_percent = None

    def __tax(self):
        for i in Tax.taxes_percent:
            if self.__sum_income in i:
                self.__tax_percent = Tax.taxes_percent.get(i)
                break

    @property
    def tax_percent(self):
        if self.__tax_percent is None:
            self.__tax()
        return self.__tax_percent

print(Tax(10,0,1000,10000).tax_percent)