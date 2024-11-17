import copy
class Search:
    @staticmethod
    def hops_by_bin_search(size_array)->int:
        import math
        return round(math.log2(size_array))

    @staticmethod
    def bin_exists(array, value, sort = False)->bool:
        array_copy = copy.copy(array) if not sort else sorted(copy.copy(array))
        result = False
        div2 = 0
        if array_copy and array_copy[-1] >= value:
            while len(array_copy) > 1:
                if array_copy[-1] == value:
                    result = True
                    break
                else:
                    div2 = int(len(array_copy)/2)
                    if array_copy[:div2][-1]>=value:
                        array_copy = array_copy[:div2]
                    else:
                        array_copy = array_copy[div2:]
        return result

    def __init__(self, array):
        self.__array = array
        self.__exists = None
        self.__value = None
        self.__hops_by_bin_search = Search.hops_by_bin_search(size_array = len(self.__array))

    @property
    def hops_bin(self):
        return self.__hops_by_bin_search

    def exists(self,value):
        self.__value = value
        if self.__exists is None:
            self.__exists = Search.bin_exists(array = self.__array,value = self.__value)
        return self.__exists


obj = Search(array = tuple(range(1_000_000_0)))
print(obj.hops_bin)
