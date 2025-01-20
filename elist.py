class EList:
    def __init__(self,obj=None):
        self.__values = {}
        try:
            for j, value in enumerate(obj):
                self.__values[j] = value
        except TypeError:
            pass

    def __getitem__(self, item):
        if item in self.__values:
            return self.__values.get(item)
        else:
            raise IndexError

    def __setitem__(self, item, other):
        if item in self.__values:
            self.__values[item] = other
        else:
            raise IndexError