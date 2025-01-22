import os
import string
import random

class UFileError(Exception):
    pass

class UFileTests:
    pass

class SampleFile(UFileTests):
    __num_rows = 100
    __num_chars = 100
    __end_of_row = '\n'

    @staticmethod
    def random_string(chars, k):
        return "".join(random.choices(chars, k = k))

    def __init__(self, name):
        self.__name = name
        self.__num_rows  = SampleFile.__num_rows
        self.__num_chars = SampleFile.__num_chars
        self.__end_of_row = SampleFile.__end_of_row

        self.__k = round(self.__num_chars / len(string.ascii_letters))

        self.__ascii_letters = string.ascii_letters * self.__k
        self.__ascii_letters = self.__ascii_letters[:self.__num_chars]

        rs = SampleFile.random_string
        self.__content = [
                            f'{rs(self.__ascii_letters, self.__num_chars)}'
                            f'{self.__end_of_row }'
                            for i in range(self.__num_rows)
                           ]

    @property
    def content(self):
        return self.__content

    def __getitem__(self, item):
        return self.__content[item]

    def __len__(self):
        return len(self.__content)

    @property
    def k(self):
        return self.__k

    @property
    def ascii_letters(self):
        return self.__ascii_letters

    @property
    def file_name(self):
        return self.__name

    @file_name.setter
    def file_name(self, other):
        self.__name = other

    def write(self):
        with open(self.__name,'w+') as file:
            file.writelines(self.__content)

class UFile:

    @staticmethod
    def exists(path, raise_error = False):
        result = os.path.exists(path)
        if raise_error and not result:
            raise FileNotFoundError
        return result

    def __init__(self, path):
        self.__path_to_file = None
        self.__set_path(path)
        self.__content = ''
        self.__load()
        self.__list_content =[]
        self.__list()

    def __set_path(self, path):
        UFile.exists(path, raise_error = True)
        self.__path_to_file = path

    def __load(self):
        with open(self.__path_to_file) as file:
            self.__content = file.read()

    def __list(self, splitter='\n'):
        self.__list_content = self.__content.split(splitter)

    @property
    def content(self):
        return self.__list_content

path = '/home/georgeiiister/txt/file3.txt'
f = SampleFile(name=path)
f.write()

f = UFile(path)
print(*f.content,sep='\n')
