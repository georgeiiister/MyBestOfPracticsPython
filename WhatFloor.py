class WhatFloor:
    @staticmethod
    def __what_floor(number_appartament:int, on_floor:int):
        return (number_appartament+3)//on_floor if number_appartament>=0 else -((-number_appartament+3)//on_floor)

    def __init__(self, number_appartament:int, on_floor:int):
        self.__number_appartament = number_appartament
        self.__on_floor = on_floor
        self.__what_floor = WhatFloor.__what_floor(number_appartament = number_appartament
                                       , on_floor = on_floor)

    @property
    def what_floor(self):
        return self.__what_floor

if __name__ == '__main__':
    print(WhatFloor(12,4).what_floor)
    print(WhatFloor(5, 4).what_floor)
    print(WhatFloor(-12, 4).what_floor)
    print(WhatFloor(-5, 4).what_floor)
