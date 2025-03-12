import time
class Progress:
    item_progress = chr(9646)

    def __init__(self, begin=0, end=100, step=1):
        self.__begin = begin
        self.__end = end
        self.__step = step
        self.__progress = ''

    @property
    def progress(self):
        return self.__progress

    @progress.setter
    def progress(self,value=None):
        if value is None:
            value = 1
        self.__progress = f'{self.__progress}{value*Progress.item_progress}'

    def demo(self):
        for i in range(self.__begin, self.__end, self.__step):
            time.sleep(1)
            self.progress=None
            print(self.progress, end = '')

if __name__ == '__main__':
    progress_sample = Progress(1,10,1)
    progress_sample.demo()

