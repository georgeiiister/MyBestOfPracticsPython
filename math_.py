class Operations:
    operators = {'*':'X','+':'+','/':':','//':':','**':'^'}

    def __init__(self):
        self.__numbers = None
        self.__result = None

    @property
    def numbers(self):
        return self.__numbers

    @property
    def operation(self):
        if self.__numbers is None:
            self.__numbers = [input(f'input number >> ') for i in range(2)]

        operators = Operations.operators

        if self.__result is None:
            expressions = {operators.get(operator).join(self.numbers)
                           :operator.join(self.numbers)
                           for operator in operators}
            self.__result = [f'{expression[0]} => {eval(expression[1])}'
                           for expression in expressions.items()]

        return self.__result

import math
class Power:
    def __init__(self, a,b):
        self.__a = a
        self.__b = b
        self.__result = None

    def __power1(self):
        if self.__result is None:
            self.__result = math.pow(self.__a, self.__b)

    def __power2(self):
        if self.__result is None:
            if not isinstance(self.__b,int):
                raise TypeError(f'{self.__b} is not instance of class int')

            self.__result = 1
            for i in range(self.__b):
                self.__result*=self.__a

    @property
    def power1(self):
        self.__power1()
        return self.__result

    @property
    def power2(self):
        self.__power2()
        return self.__result

class Int2list:
    def __init__(self, num:int):
        self.__num = num
        self.__list = None
        self.__list_reverse = None

    @property
    def int2list(self):
        if self.__list is None:
            self.__list = list(str(self.__num))
        return self.__list

    @property
    def reverse(self):
        if self.__list_reverse is None:
            self.__list_reverse = list(reversed(list(str(self.__num))))
        return self.__list_reverse

#print(*Operations().operation,sep='\n')
#print(Power(10,10).power2)
print(Int2list(1234567).reverse)
