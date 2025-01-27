import random
import binary_search

class GlassBallsGame:
    class GlassBallsGameError(Exception):
        pass

    class NumberOfLevel(GlassBallsGameError):
        pass

    class NumberOfLevelLessThanZero(NumberOfLevel):
        pass

    @staticmethod
    def check_number_of_level(value:int,raise_error=False)->bool:
        result = False
        try:
            if value <= 0:
                raise GlassBallsGame.NumberOfLevelLessThanZero
            else:
                result = True
        except Exception:
            if raise_error:
                raise
        return result



    def __init__(self, number_of_levels:int):
        GlassBallsGame.check_number_of_level(
                                              value = number_of_levels,
                                              raise_error = True
                                             )
        self.__number_of_levels = number_of_levels
        self.__number_glass_balls = None
        self.__number_of_level_for_broken_ball = random.randint(1,
                                                                self.__number_of_levels
                                                                )
    @property
    def number_of_levels(self):
        return self.__number_of_levels

    @property
    def number_glass_balls(self):
        bin_search = binary_search.BinSearch.bin_search
        if self.__number_glass_balls is None:
            collection = tuple(range(1,self.__number_of_levels+1))
            value = self.__number_of_level_for_broken_ball
            self.__number_glass_balls = bin_search(
                                                     collection=collection,
                                                     value = value,
                                                     sort = True,
                                                     return_hops = True,
                                                     print_hops = True
                                                  )[1]
        return self.__number_glass_balls

    @property
    def number_of_level_for_broken_ball(self):
        return self.__number_of_level_for_broken_ball


if __name__ =='__main__':
    level = 100
    print(f'level {level}')
    game1 = GlassBallsGame(level)
    print(game1.number_of_level_for_broken_ball,game1.number_glass_balls, sep='|')

