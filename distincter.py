class Distincter:
    def __init__(self, lst:list):
        self.__lst = lst
    def distinct1(self):
        return list(set(self.__lst))

    def distinct2(self):
        return [i for j,i in enumerate(self.__lst)
                if (self.__lst.count(i)>1 and self.__lst.index(i) == j) or self.__lst.count(i) == 1]

if __name__ == '__main__':
    a = Distincter([1,2,3,4,4,1,2])
    print(a.distinct1())
    print(a.distinct2())