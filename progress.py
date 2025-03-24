import time
class Progress:
    item_progress = chr(9646) #symbol for item progressbar

    def __init__(self, begin=0, end=100, step=1):
        self.__begin = begin
        self.__end = end
        self.__step = step
        self.__progress = ''

    def show(self):
        return self.__progress

    def next(self,value=1):
        self.__progress = f'{self.__progress}{value*Progress.item_progress}'

    def demo(self):
        for i in range(self.__begin, self.__end, self.__step):
            time.sleep(1)
            self.next()
            print('\b'*len(self.__progress),end='')
            print(self.show(),end='')

    def __init(self):
        raise NotImplemented

if __name__ == '__main__':
    progress_sample = Progress(1,20,1)
    progress_sample.demo()