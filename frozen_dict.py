class FD:
    """emulator frozen dict"""
    def __init__(self):
        self.__dict = dict()
        self.__list = []

    def __ikey(self, key):
        try:
            return self.__list.index(key)
        except ValueError:
            self.__list.append(key)
            return len(self.__list)-1

    def __setitem__(self, key, value):
        self.__dict[self.__ikey(key = key)] = value

    def __getitem__(self, item):
        return self.__dict.get(self.__ikey(key = item))

    def __repr__(self):
        return str({self.__list[ikey]:self.__dict[ikey] for ikey,value in enumerate(self.__list)})

if __name__ == '__main__':
    fd = FD()
    fd['key1'] = 'value1'
    fd['key2'] = 'value2'

    print(repr(fd))
