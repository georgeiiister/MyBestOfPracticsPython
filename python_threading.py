import threading
import random
import datetime

orders = (i for i in range(10))

class Grabby(threading.Thread):
    def __init__(self,name, link_on_orders):
        super().__init__(name = name)
        self.__orders = link_on_orders
        self.__result = []

    def run(self):
        print(datetime.datetime.now())
        while True:
            try:
                sum(i for i in range(0,random.randint(1,10_000_000)))
                result = next(self.__orders)
                self.__result.append(result)
            except StopIteration:
                print(self.__result)
                break


if __name__ == '__main__':
    Grabby1 = Grabby(name='Grabby1', link_on_orders=orders)
    Grabby2 = Grabby(name='Grabby1', link_on_orders=orders)

    Grabby1.start()
    Grabby2.start()
