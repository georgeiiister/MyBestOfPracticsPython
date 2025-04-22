import uuid
import pickle
from typing import Optional
class Queue:
    class QueueError(Exception):
        pass

    class QueueIsFullError(QueueError):
        pass

    class QueueIsEmptyError(QueueError):
        pass

    class QueueIsLockError(QueueError):
        pass

    __error_if_lock = False

    @classmethod
    def _status_lock(cls):
        return cls.__error_if_lock

    def __init__(self, size:int, error_if_lock:Optional[bool] = None):
        self.__size = size
        self.__queue = []
        self.__lock = error_if_lock or self.__class__._status_lock()
        self.__error_if_lock = error_if_lock

    def get(self):
        return self.__get()

    def put(self, obj):
        self.__put(obj = obj)

    @property
    def size(self):
        return self.__size

    def dump(self, path = None):
        if path is None:
            path = str(uuid.uuid1())

        with open(path,'wb+') as _file:
            pickle.dump(self, _file)

    def status_lock(self):
        result = self.__lock

        if result and self.__error_if_lock:
            raise Queue.QueueIsLockError

        return result

    def __get(self):
        if not self.__queue:
            raise Queue.QueueIsEmptyError

        if not self.__lock:
            return self.__queue.pop(0)

    def __put(self, obj):
        if len(self.__queue) == self.__size:
            raise QueueIsFullError

        if not self.__lock:
            self.__queue.append(obj)

    def __lock(self):
        self.__queue = True

    def __unlock(self):
        self.__lock = False

    def __enter__(self):
        self.__lock()

    def __exit__(self, exc_type = None, exc_val  = None, exc_tb = None):
        self.__unlock()

    def __len__(self):
        return len(self.__queue)

if __name__ == '__main__':
    """create Queue"""

    queue = Queue(size = 100_000_0)

    import random
    import string

    for i in range(queue.size):
        queue.put(''.join(random.choices(string.ascii_letters,k = 10)))

    print(queue.get())
    print(queue.get())