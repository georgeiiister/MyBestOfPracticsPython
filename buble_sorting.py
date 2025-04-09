import copy
class BS:
    @staticmethod
    def sorted_buble_(obj):
        result = list(obj)
        j = 1
        while j<len(result):
            k = len(result)-1
            while j <= k:
                if result[k-1] > result[k]:
                    result[k-1], result[k] = result[k], result[k-1]
                k-=1
            j+=1
        return type(obj)(result)

    @staticmethod
    def sorted_as_list_(obj):
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

    def sorted_as_list(self):
        self.__obj_sorted = self.__obj_sorted or BS.sorted_as_list_(obj = self.__obj)
        return self.__obj_sorted

    def sorted_buble(self):
        self.__obj_sorted = self.__obj_sorted or BS.sorted_buble_(obj = self.__obj)
        return self.__obj_sorted

a = (1,2,3,-190,1000,0,900)
print(BS(a).sorted_as_list())
print(BS(a).sorted_buble())


