class MS:
    def __init__(self, *args):
        self.__iter_objects = args
        self.__result_union_sorted = []

    def sorted_as_list(self):
        for item in self.__iter_objects:
            self.__result_union_sorted.extend(item)
        self.__result_union_sorted.sort()
        return self.__result_union_sorted


a = MS((1,2,3), [1,2,3],{3,4,5})
print(a.sorted_as_list())


