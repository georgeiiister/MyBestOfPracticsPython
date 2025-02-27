class MIterator:
    def __init__(self, name):
        self.__name = name
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.__index < len(self.__name):
            result = self.__name[self.__index]
            self.__index += 1
            return result
        else:
            raise StopIteration


for i in MIterator('hello'):
    print(i,end='')