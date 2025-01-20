import math
import decimal

class CircleError(Exception):
    pass

class RadiusNotNumber(CircleError):
    pass

class GeneratorOfCircle:
    def __init__(self):
        self.__start = 1
        self.__stop = 1_000_000_000
        self.__step = 1
        self.__current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.__current <= self.__stop:
            self.__current += self.__step
            return self.__current
        else:
            raise StopIteration

class Circle:

    @staticmethod
    def check_radius(radius, raise_error=True):
        result = False
        try:
            result = bool(decimal.Decimal(radius))
        except decimal.InvalidOperation:
            if raise_error:
                raise RadiusNotNumber
        finally:
            return result

    @staticmethod
    def pi():
        return decimal.Decimal(str(math.pi))

    __counter_of_instances = GeneratorOfCircle()
    __dict_instances = {}
    __area_all_of_instances = 0
    __circumference_all_of_instances = 0

    @classmethod
    def __add2dict_instance(cls, circle_instance):
        cls.__dict_instances[circle_instance.internal_id] = circle_instance
        cls.__area_all_of_instances += circle_instance.area
        cls.__circumference_all_of_instances += circle_instance.circumference

    @classmethod
    def instance(cls, internal_id:int):
        return cls.__dict_instances.get(internal_id)

    @classmethod
    def area_all_of_instances(cls):
        return cls.__area_all_of_instances

    @classmethod
    def circumference_all_of_instances(cls):
        return cls.__circumference_all_of_instances

    @classmethod
    def calc_area_by_radius(cls, radius):
        Circle.check_radius(radius=radius)
        return Circle.pi() * pow(decimal.Decimal(str(radius)),2)

    @classmethod
    def calc_circumference_by_radius(cls, radius):
        Circle.check_radius(radius=radius)
        return 2 * Circle.pi() * decimal.Decimal(str(radius))

    def __init__(
                    self,
                    radius,
                    precision_print = None
                 ):
        Circle.check_radius(radius = radius)
        self.__radius = decimal.Decimal(str(radius))
        self.__area = None
        self.__circumference = None
        self.__internal_id = next(Circle.__counter_of_instances)
        self.__precision_print = precision_print

    @property
    def internal_id(self):
        return self.__internal_id

    def __add2dict(self):
        Circle.__add2dict_instance(circle_instance=self)

    def __calc_area(self):
        self.__area = Circle.calc_area_by_radius(radius = self.__radius)
        self.__add2dict()

    def __calc_circumference(self):
        calc_circumference = Circle.calc_circumference_by_radius
        self.__circumference = calc_circumference(radius=self.__radius)
        self.__add2dict()

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, other):
        self.__radius = other
        self.__calc_area()

    @property
    def area(self):
        if self.__area is None:
            self.__calc_area()
        return self.__area

    @property
    def circumference(self):
        if self.__circumference is None:
            self.__calc_circumference()
        return self.__circumference

    def __str__(self):
        result = (self.__radius, self.__area, self.__circumference)
        if self.__precision_print is not None:
            result  = tuple(round(i,self.__precision_print) for i in result)
        return (
                    f'circle:['
                    f'radius={result[0]}, '
                    f'area={result[1]}, '
                    f'circumference={result[2]}'
                    f']'
                )
    @property
    def precision_print(self):
        return self.__precision_print

    @precision_print.setter
    def precision_print(self,other):
        self.__precision_print = other