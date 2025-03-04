import threading
import random
import datetime

objects = (i for i in range(1000))

class Grabby(threading.Thread):
    def __init__(self,name, sort_out_objects):
        super().__init__(name = name)
        self.__sort_out_objects = sort_out_objects
        self.__objects = []

    def run(self):
        print(datetime.datetime.now())
        while True:
            try:
                [i for i in range(0,random.randint(1,1_000_000))]
                self.__objects.append(next(self.__sort_out_objects))
            except StopIteration:
                break
    @property
    def objects(self):
        return self.__objects

mrSmitty = Grabby(name='mrSmitty', sort_out_objects = objects)
msSmitty = Grabby(name='msSmitty', sort_out_objects = objects)

mrSmitty.run()
msSmitty.run()

for grabby in (mrSmitty, msSmitty):
    print(grabby.objects)
