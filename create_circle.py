import math

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
    def pi():
        return math.pi

    __counter_of_instances = GeneratorOfCircle()
    __dict_instances = {}
    __area_all_of_instances = 0

    @classmethod
    def __add2dict_instance(cls, circle_instance):
        cls.__dict_instances[circle_instance.internal_id] = circle_instance
        cls.__area_all_of_instances += circle_instance.area

    @classmethod
    def instance(cls, internal_id:int):
        return cls.__dict_instances.get(internal_id)

    @classmethod
    def area_all_of_instances(cls):
        return cls.__area_all_of_instances

    @classmethod
    def calc_area_by_radius(cls, radius):
        return Circle.pi() * pow(radius,2)

    def __init__(self, radius):
        self.__radius = radius
        self.__area = None
        self.__internal_id = next(Circle.__counter_of_instances)

    @property
    def internal_id(self):
        return self.__internal_id

    def __calc_area(self):
        self.__area = Circle.calc_area_by_radius(radius = self.__radius)
        Circle.__add2dict_instance(circle_instance = self)

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