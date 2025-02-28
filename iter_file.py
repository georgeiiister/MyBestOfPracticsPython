class IFile:
    def __init__(self, path:str):
        self.__path = path
        self.__file = None

    def __enter__(self):
        self.__file = open(self.__path)
        return self.__file

    def __exit__(self, exc_type = None, exc_val = None, exc_tb = None):
        self.__file.close()

    def __iter__(self):
        return self.__file

    def __next__(self):
        for rec in self:
            return rec
        else:
            raise StopIteration
obj = IFile('/home/georgeiiister/python/file_name1.txt')
with obj as fl:
    for i in fl:
        print(i.rstrip('\n'))