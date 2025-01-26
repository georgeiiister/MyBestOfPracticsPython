class StrDiv:
    def __init__(self, value):
        self.__value = value

    def __truediv__(self, other):
        result = []
        if len(self.__value) % other == 0:
            part = []
            for item in self.__value:
                part.append(item)
                if len(part) == other:
                    result.append(''.join(part))
                    part.clear()
        return result

a = StrDiv('abcdfg')

print(a/3)