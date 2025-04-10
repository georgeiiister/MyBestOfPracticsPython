import random
class RandomRec:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__dict = {}
        self.__len_strings = 0
        self.__file = None

    def __enter__(self):
        self.__file = open(self.__file_path, 'rt')
        return self

    def __exit__(self, exc_type=None, exc_val=None, exc_tb=None):
        self.__file.close()

    @property
    def random_string(self):
        for i, rec in enumerate(self.__file):
            self.__len_strings+=len(rec)
            self.__dict[i] = self.__len_strings
        num_row = random.randint(0, max(self.__dict))
        position = self.__dict[num_row]
        self.__file.seek(position, 0)
        return self.__file.readline()

    @property
    def random_string_(self):
       return random.choice(self.__file.readlines()).rstrip('\n')


with RandomRec('rnd') as f:
    print(f.random_string_)