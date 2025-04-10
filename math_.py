import math
from functools import reduce
from decimal import Decimal

class UserSum:
    @staticmethod
    def __user_sum1(obj):
        return sum(obj)

    @staticmethod
    def __user_sum2(obj):
        result = Decimal('0')
        for i in obj:
            result+=i
        return result

    def __init__(self, obj):
        self.__obj = obj
        self.__decimal_obj = (Decimal(str(i)) for i in obj)
        self.__user_sum = None
        self.__decimal_sum = None

    @property
    def sum1(self):
        if self.__decimal_sum is None:
            self.__decimal_sum = UserSum.__user_sum1(obj=self.__obj)
            self.__user_sum = type(self.__obj[0])(self.__decimal_sum)
        return self.__user_sum

    @property
    def sum2(self):
        if self.__decimal_sum is None:
            self.__decimal_sum = UserSum.__user_sum2(obj=self.__obj)
            self.__user_sum = type(self.__obj[0])(self.__decimal_sum)
        return self.__user_sum

class LastNumber:
    def __init__(self, number:int, digit:int):
        self.__number = number
        if digit not in range(0,10):
            raise ValueError
        self.__digit = digit


    @property
    def yes(self):
        return self.__number % 10 == self.__digit

    @property
    def yes2(self):
        return int(str(self.__number)[-1]) == self.__digit


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
            self.__numbers = [input(f'input number >> ') for _ in range(2)]

        operators = Operations.operators

        if self.__result is None:
            expressions = {operators.get(operator).join(self.numbers)
                           :operator.join(self.numbers)
                           for operator in operators}
            self.__result = [f'{expression[0]} => {eval(expression[1])}'
                           for expression in expressions.items()]

        return self.__result

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

class Factorial:
    class FactorialError(Exception):
        pass

    class SignValueFactorialError(FactorialError):
        pass

    def __init__(self, value):
        self.__value = int(value)
        if self.__value <= 0:
            raise Factorial.SignValueFactorialError

        self.__factorial = Factorial.__factorial(value = self.__value)

    @staticmethod
    def __factorial(value:int)->int:
        result = None
        if value > 0:
            result = reduce(lambda i,j:i*j, range(1,value+1))
        return result

    @property
    def factorial(self):
        return self.__factorial

class PrimeNumber:
    @staticmethod
    def prime_number(value:int)->bool:
        result = False
        for j in range(2, int(math.sqrt(value)) + 1):
            if value % j == 0:
                break
        else:
            result = True
        return result
    @staticmethod
    def prime_number_in_range(begin_range:int, end_range:int)->list:
        result = []
        for i in range(begin_range,end_range):
            if PrimeNumber.prime_number(value = i):
                result.append(i)
        return result

    def __init__(self, begin_range:int, end_range:int):
        self.__begin_range = begin_range
        self.__end_range = end_range
        self.__prime_number_list = PrimeNumber.prime_number_in_range(
                                                                     begin_range = begin_range,
                                                                     end_range = end_range
                                                                     )

    @property
    def pn(self):
        return self.__prime_number_list

class MM:
    @staticmethod
    def m_x(obj, ttype = 1):
        """ttype: 1 - max, 0 - min"""
        result = None
        mx_by_type = {
                        1:lambda r, i: i if r < i else r
                      , 0:lambda r, i: i if r > i else r
                      }
        for i in obj:
            try:
                result = mx_by_type.get(ttype)(result, i)
            except TypeError:
                result = i
        return result


#print(*Operations().operation,sep='\n')
#print(Power(10,10).power2)
#print(Int2list(1234567).reverse)
#print(Factorial(value = input('value for factorial>> ')).factorial)
#print(PrimeNumber.prime_number(7399))
#print(*PrimeNumber(2,101).pn,sep='\n')
#print(LastNumber(302,2).yes, LastNumber(302,2).yes2)
#print(MM.m_x((-1,2,3),0))
print(UserSum((1,2,3)).sum1)