import copy


class BinSearch:
    @staticmethod
    def hops_by_bin_search(size) -> int:
        import math
        return round(math.log2(size))

    @staticmethod
    def bin_search(collection, value, sort=False):
        collection_copy = copy.copy(collection) if not sort else sorted(copy.copy(collection))
        result = None
        if collection_copy and collection_copy[-1] >= value:
            while len(collection_copy) > 1:
                div2 = int(len(collection_copy) / 2)
                if collection_copy[:div2][-1] >= value:
                    collection_copy = collection_copy[:div2]
                else:
                    collection_copy = collection_copy[div2:]
        if collection_copy[0] == value:
            result = collection_copy[0]
        return result

    @staticmethod
    def bin_exists(collection, value, sort=False) -> bool:
        return bool(BinSearch.bin_search(collection=iobject,
                                         value=value,
                                         sort=sort
                                         ))

    def __init__(self, collection):
        self.__collection = collection
        self.__value = None
        f_hops = BinSearch.hops_by_bin_search
        self.__hops_by_bin_search = f_hops(size=len(self.__collection))

    @property
    def hops(self):
        return self.__hops_by_bin_search

    def exists(self, value):
        result = False
        if value ==  self.__value:
            result = True
        else:
            if BinSearch.bin_exists(collection=self.__collection, value=self.__value):
                self.__value = value
            else:
                result = False
        return result

    def search(self, value):
        self.__value = BinSearch.bin_search(collection=self.__collection,
                                             value=value
                                           )
        return self.__value

import array
my_obj = BinSearch(collection=array.array('i', tuple(range(1000_000_0))))
print(my_obj.search(900))