class Min3number:
    def __min(self):
        self.__min_val = min(self.__nums)

    def __init__(self):
        self.__nums = None
        self.__min_val = None
        while True:
            try:
                nums = tuple((int(input(f'input number {i+1} >> ')) for i in range(3)))
            except ValueError:
                print(f'you input not number!')
                continue
            self.__nums = nums
            break
        self.__min()

    def min(self):
        if  self.__min_val is None:
            self.__min()

        return self.__min_val

print(Min3number().min())



