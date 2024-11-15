class ExistsValueInCollection:
    @staticmethod
    def exists_(collection: tuple[int] | list[int], value: int, sort=False) -> bool | None:
        result = None
        if collection:
            collection_sorted = sorted(collection) if sort else collection
            while len(collection_sorted) > 1:
                len_div2 = int(len(collection_sorted) / 2)
                if collection[:len_div2][-1] == value:
                    return True
                elif collection_sorted[:len_div2][-1] > value:
                    collection_sorted = collection_sorted[:len_div2]
                else:
                    collection_sorted = collection_sorted[len_div2:]
            else:
                return collection_sorted[0] == value
        return result

    def __init__(self, collection: tuple[int] | list[int], sort=False):
        self.__collection = collection
        self.__sort = sort
        self.__exists = None

    def exists(self, value):
        return ExistsValueInCollection.exists_(collection=self.__collection, value=value)

    def exists_iteration(self, value):
        for i in self.__collection:
            if i == value:
                return True
        else:
            return False

    def exists_low2(self, value):
        return bool(any(i == value for i in self.__collection))

    def exists_hi(self, value):
        return bool(self.__collection.index(value))


lstA = [i for i in range(1000_000_00)]
obj = ExistsValueInCollection(collection=lstA)

import time

vtime = time.time()
print(obj.exists(value=999_000))
print(time.time() - vtime)

vtime = time.time()
print(obj.exists_iteration(value=999_000))
print(time.time() - vtime)

vtime = time.time()
print(obj.exists_hi(value=999_000))
print(time.time() - vtime)

vtime = time.time()
print(obj.exists_low2(value=999_000))
print(time.time() - vtime)
