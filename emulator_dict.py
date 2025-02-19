class MyDict:
    def __init__(self):
        self.__size = 10
        self.__data = [None for i in range(self.__size)]

    def add(self,other:int):
        ind:int = self.__ind(other)
        self.__data[ind] = other

    @property
    def data(self):
        return self.__data

    def __ind(self, other)->int:
        return int(int((other / self.__size - other// self.__size) * self.__size))

    def value(self,other):
        return self.__data[self.__ind(other)]

my_dict = MyDict()
my_dict.add(911)
my_dict.add(912)
my_dict.add(913)

print(my_dict.value(911))
