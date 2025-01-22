import os

class CountWordsError(Exception):
    pass

class PathFileError(CountWordsError):
    def __init__(self):
        self.__describe_error = {'en':'Path to file not found'}

class CountWords:
    def __init__(self):
        self.__path = None
        self.__count_of_rows = 0
        self.__count_of_words = 0
        self.__count_of_chars = 0
        self.__file()
        self.__calc()

    def __file(self):
        self.__path = self.__path or input('Enter file ppath>> ')
        if not os.path.exists(self.__path):
            self.__path = None
            raise PathFileError

    def __calc(self):
        with open(self.__path) as fl:
            for row in fl:
                self.__count_of_rows += 1
                self.__count_of_chars += len(row)
                self.__count_of_words += len(row.split())

    def __str__(self):
        return (
                    f'count of rows = {self.__count_of_rows}, '
                    f'count of words = {self.__count_of_words}, '
                    f'count of chars = {self.__count_of_chars}'
                )

if __name__=='__main__':
    _ = CountWords()
    print(_)
