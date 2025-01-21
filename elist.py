class EList:
    def __add_item(self, index:int | None, value):
        """add value by index"""
        if index is not None:
            if index in self.__values:
                self.__values[index] = value
            else:
                raise IndexError
        else:
            try:
                for j, value in enumerate(value):
                    self.__values[j] = value
            except TypeError:
                pass

    def __init__(self, value = None):
        self.__values = {}
        self.__add_item(index = None, value = value)

    def __getitem__(self, index):
        return self.__values.get(index)

    def __setitem__(self, index, value):
        self.__add_item(index = index, value = value)

    def __len__(self):
        return len(self.__values)

    def __str__(self):
        return f'<{",".join([i for i in self.__values.values()])}>'

