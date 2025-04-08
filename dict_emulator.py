class DictEmulator10:
    __size = 10
    def __init__(self):
        self.__values = [None] * DictEmulator10.__size

    def add(self, key, value):
        index = key % DictEmulator10.__size
        self.__values[index] = value

    def get(self, key):
        index = key % DictEmulator10.__size
        return self.__values[index]

    @property
    def values(self):
        return self.__values

my_dict = DictEmulator10()
my_dict.add(key=1, value = '0001')
my_dict.add(key=2, value = '0002')
my_dict.add(key=3, value = '0003')

print(my_dict.get(key=3))
print(my_dict.values)