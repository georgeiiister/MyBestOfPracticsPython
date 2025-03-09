import threading
import datetime

class A(threading.Thread):
    def __init__(self, name, orders):
        super().__init__(name = name)
        self.__orders = orders
        self.__result = []

    def run(self):
        print(f'start {self.name} {datetime.datetime.now()}')
        while True:
            try:
                sum((i for i in range(10_000_000)))
                self.__result.append(next(self.__orders))
            except StopIteration:
                print(f'stop {self.name} {datetime.datetime.now()}')
                print(self.__result)
                break

if __name__ == '__main__':

    in_orders = (i for i in range(10))

    thread1 = A(name='thread1', orders = in_orders)
    thread2 = A(name='thread2', orders = in_orders)

    thread1.start()
    thread2.start()

