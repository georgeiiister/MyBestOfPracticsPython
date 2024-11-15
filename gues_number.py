import random

class GuessNumber:
    min = 1
    max = 10

    def __init__(self):
        self.__min = GuessNumber.min
        self.__max = GuessNumber.max
        self.__input_values = []

        self.__guess_number = random.choices(range(self.__min,self.__max),k=1)[-1]

    @property
    def get_number(self):
        self.__input_values.append(int(input('Enter integer number ')))
        if self.__input_values[-1] == self.__guess_number:
            print(f'Congratulation! The number: {self.__input_values[-1]}')
            return True
        else:
            if self.__input_values[-1]<self.__guess_number:
                print('please, increase the number')
            else:
                print('please, reduce the number')
            return False

obj = GuessNumber()

while not obj.get_number:
    pass