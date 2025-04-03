import copy
class BS:
    @staticmethod
    def sorted_b(obj):
        result = list(obj)
        for i in result[1:]:
            pass #ToDo buble!

        return type(obj)(result)


    @staticmethod
    def sorted(obj):
        result = []
        if obj:
            result.append(obj[0])
            for i in obj[1:]:
                for ind, j in enumerate(result):
                    if i <= j:
                        result.insert(ind, i)
                        break
                else:
                    result.append(i)
            return type(obj)(result)

    def __init__(self, obj):
        self.__obj = obj
        self.__obj_sorted = None

    def sort(self):
        self.__obj_sorted = self.__obj_sorted or BS.sorted(obj = self.__obj)
        return self.__obj_sorted

    def sort_b(self):
        self.__obj_sorted = self.__obj_sorted or BS.sorted_b(obj = self.__obj)
        return self.__obj_sorted

a = (1,2,3,-190,1000,0,900)
print(BS.sorted(a))


