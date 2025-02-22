import pathlib


class FileAsBites:

    def __init__(self, path_to_file: pathlib.Path):
        self.__path_to_file = path_to_file
        self.__file_content = ''
        self.__read_file_as_str_bytes()

    def __read_file_as_str_bytes(self):
        s = 'None'
        l = []
        char = ''
        total_string = []
        with open(self.__path_to_file, 'rb') as fl:
            while s != b'':
                s = fl.read(1)
                l.append(s)
                try:
                    char = bytes().join(l).decode('utf-8')
                    l.clear()
                    total_string.append(char)
                except UnicodeDecodeError:
                    pass
        self.__file_content = ''.join(total_string)

    def __str__(self):
        return self.__file_content


a = FileAsBites(pathlib.Path('/home/georgeiiister/python/file'))
print(a)
