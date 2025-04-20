class Bin2Int:
    """converter binary number to decimal number"""

    class Bin2IntError(Exception):
        pass

    class Base2Error(Bin2IntError):
        pass

    @staticmethod
    def bin2int(bin_value) -> int:
        """function with realization base transformation"""
        return sum(((2 ** exp) * int(value)
                    for exp, value in enumerate(reversed(tuple(bin_value.upper().lstrip('0B'))))))

    @staticmethod
    def bin_minus2int(bin_value) -> int:
        """function with realization base transformation with minus"""
        result = tuple(bin_value.upper().lstrip('0B'))
        result = tuple((int(not bool(int(i))) for i in result[:-1])) + (1,)
        result = sum(((2 ** exp) * value
                      for exp, value in enumerate(reversed(result))))
        return - result

    @staticmethod
    def bin2int_(bin_value) -> int:
        """function with realization base transformation with builtin methods"""
        return int(bin_value, 2)

    def __init__(self, bin_value: str, sign='plus'):
        bin_value = bin_value.upper().lstrip('0B')
        for i in bin_value:
            if i not in ('1', '0'):
                raise Bin2Int.Base2Error

        self.__bin_value = bin_value
        self.__int = None
        self.__sign = sign

    @property
    def int(self):
        """get decimal value from binary"""
        if self.__int is None:
            if self.__sign.upper() == 'plus'.upper():
                self.__int = self.__class__.bin2int(bin_value=self.__bin_value)
            elif self.__sign.upper() == 'minus'.upper():
                self.__int = self.__class__.bin_minus2int(bin_value=self.__bin_value)
        return self.__int

    @property
    def int_(self):
        """get decimal value from binary"""
        if self.__int is None:
            self.__int = self.__class__.bin2int_(bin_value=self.__bin_value)
        return self.__int


if __name__ == '__main__':
    import random

    examples = ((k[0], k[1], Bin2Int(bin_value=k[1]).int)
                for k in ((j, bin(j))
                          for j in (random.randint(1, 1000) for i in range(100))))
    print(f'{"bin value":>14}|{"dec value":>8}|{"result value":>12}|{"status"}')
    for item in examples:
        print(f'{item[1]:>14}|{item[0]:>9}|{item[2]:>12}|{"+" if item[0] == item[2] else "-":>2}')

    print(Bin2Int(bin_value='101100011', sign='minus').int)
