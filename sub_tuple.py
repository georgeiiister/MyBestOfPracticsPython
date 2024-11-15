class SubTuple:
    @staticmethod
    def is_sub_tuple_(first:tuple, second:tuple):
        return set(second).issubset(first)

    def __init__(self, first:tuple, second:tuple):
        self.__first = first
        self.__second = second
        self.__result = None

    @property
    def is_sub_tuple(self):
        return SubTuple.is_sub_tuple_(first=self.__first, second=self.__second)

print(SubTuple(first=(1,2,3),second=(2,3,4)).is_sub_tuple)