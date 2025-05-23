import math
from functools import reduce
from decimal import Decimal
import threading
import typing
import sys


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

    __factorial_recu = 1

    def __init__(self, value):
        self.__value = int(value)
        if self.__value <= 0:
            raise Factorial.SignValueFactorialError

        self.__factorial = self.__class__.__factorial(value = self.__value)

    @staticmethod
    def __factorial(value:int)->int:
        result = None
        if value > 0:
            result = reduce(lambda i,j:i*j, range(1,value+1))
        return result

    @staticmethod
    def factorials(*args)->dict[int,int]:

        class FactorialThread(threading.Thread):
            __count_of_threads = 0

            @classmethod
            def number_thread(cls):
                cls.__count_of_threads +=1
                return cls.__count_of_threads

            def __init__(self, values:list[int], dict_of_result:dict[int, int]):
                super().__init__(name=f'thread {self.__class__.number_thread()}')
                self.__values = values
                self.__dict_result = dict_of_result

            def run(self):
                for value in self.__values:
                    self.__dict_result[value] = Factorial(value=int(value)).factorial

            @property
            def dict_result(self):
                return self.__dict_result

        size_collection = 10 #items
        result = {}
        collection_of_values = []
        threads = []

        for item in args:
            collection_of_values.append(item)
            if len(collection_of_values)%size_collection == 0:
                threads.append(FactorialThread(values=collection_of_values.copy()
                                               ,dict_of_result = result))
                collection_of_values.clear()

        if collection_of_values:
            threads.append(FactorialThread(values=collection_of_values.copy(),dict_of_result = result))

        for thread in threads:
            thread.start()

        while True:
            if all((not thread.is_alive() for thread in threads)):
                break
        return result

    @staticmethod
    def __factorial_eval(value:int):
        result = None
        if value > 0:
            result = eval('*'.join([str(i) for i in range(1,value+1)]))
        return result

    @staticmethod
    def __factorial_for(value:int):
        result = 1
        if value > 0:
            for i in range(1,value+1):
                result *= 1
        return result

    @staticmethod
    def __factorial_recursive(value: int):
        if value > 1:
            Factorial.__factorial_recu *= value
            Factorial.__factorial_recursive(value-1)

        return Factorial.__factorial_recu

    @staticmethod
    def __factorial_recursive2(value: int):
        if value > 1:
            if value == 1:
                return 1
            return Factorial.__factorial_recursive(value - 1) * value

        return Factorial.__factorial_recu

    @property
    def factorial(self):
        return self.__factorial

    @property
    def factorial_recursive(self):
        return Factorial.__factorial_recursive(value = self.__value)

    @property
    def factorial_recursive2(self):
        return Factorial.__factorial_recursive2(value=self.__value)

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
                        1:lambda r, k: i if r < k else r
                      , 0:lambda r, k: i if r > k else r
                      }
        for i in obj:
            try:
                result = mx_by_type.get(ttype)(result, i)
            except TypeError:
                result = i
        return result

class EvenNumber:
    __divider = 2
    @staticmethod
    def even_number_(number_):
        return not bool(number_ % EvenNumber.__divider)
    def __init__(self, number_):
        self.__number = number_
        self.__even_number = EvenNumber.even_number_(number_ = number_)

    @property
    def even_number(self):
        return self.__even_number

#print(*Operations().operation,sep='\n')
#print(Power(10,10).power2)
#print(Int2list(1234567).reverse)
#print(Factorial(value = input('value for factorial>> ')).factorial_recursive2)
#print(PrimeNumber.prime_number(7399))
#print(*PrimeNumber(2,101).pn,sep='\n')
#print(LastNumber(302,2).yes, LastNumber(302,2).yes2)
#print(MM.m_x((-1,2,3),0))
#print(EvenNumber(9).even_number)
sys.set_int_max_str_digits(0)
with open('factorial.txt','tw+') as fl:
    for i,j in Factorial.factorials(*range(1,10000)).items():
        fl.write(f'{i} {j}\n')