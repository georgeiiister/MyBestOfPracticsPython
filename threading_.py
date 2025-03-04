import threading
import datetime

a = (i for i in range(10))


class A(threading.Thread):
    def __init__(self, name, obj):
        super().__init__(name=name)
        self.__list = []
        self.__obj = obj

    def run(self):
        print(f'start {self.name} {datetime.datetime.now()}')
        while True:
            try:
                sum((i for i in range(1000_000_0)))
                self.__list.append(next(self.__obj))
            except StopIteration:
                break
        print(self.__list)

    @property
    def lst(self):
        return self.__list


if __name__ == '__main__':
    t1 = A('thread1', a)
    t2 = A('thread2', a)
    t1.start()
    t2.start()