class WhatFloor:
    @staticmethod
    def __what_floor(number_appartament:int, on_floor:int):
        what_floor = (abs(number_appartament)+3)//on_floor
        return what_floor if number_appartament>=0 else -what_floor

    def __init__(self, number_appartament:int, on_floor:int):
        self.__number_appartament = number_appartament
        self.__on_floor = on_floor
        self.__what_floor = WhatFloor.__what_floor(number_appartament = number_appartament
                                       , on_floor = on_floor)

    @property
    def what_floor(self):
        return self.__what_floor

if __name__ == '__main__':
    test = ((12,4),(5,4),(-12,4),(-5,4),(0,4), (1,4), (-1,4))
    for i,j in sorted(test,key=lambda l:abs(l[0])):
        print(f'Номер квартиры {i},  число квартир на этаже {j}, этаж {WhatFloor(i,j).what_floor}')
