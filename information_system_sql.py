import sqlite3
import string
import random
from typing import *

class InformationSystemError(Exception):
    pass

class LockObjectError(InformationSystemError):
    pass

class IsAlreadyBlocked(LockObjectError):
    pass

class CursorError(InformationSystemError):
    pass

class CursorNotFound(CursorError):
    pass

class Seq:
    def __init__(self, start:int = 1, stop:int = 100_000_000, step:int = 1):
        self.__start = start
        self.__stop = stop
        self.__step = step
        self.__current = self.__start

    def __iter__(self):
        return self

    def __next__(self):
        while self.__current <= self.__stop:
            result = self.__current
            self.__current += 1
            return result
        else:
            raise StopIteration

class User:
    class UserError(Exception):
        pass

    __table = 'Users'
    __create_table_sql = (
                            f'create table if not exists {__table}'
                            f'('
                            f'id integer,'
                            f'fusername text,'
                            f'email text,'
                            f'age integer'
                            f')'
                         )

    __insert_sql = f'insert into {__table} values(?,?,?,?)'
    __select_sql = f'select * from {__table} where id=?'
    __update_sql = f'update {__table} set username=?,email=?, age=? where id=?'

    __seq = Seq()

    @classmethod
    def create_table(cls,cursor):
        cursor.execute(User.__create_table_sql)

    @classmethod
    def table(cls, name):
        return User.__table

    @classmethod
    def set_table(cls, name):
        User.__table = name

    def __init__(self, id=None, username = None, email = None, age = None, cursor = None):
        if id is None:
            id = next(User.__seq)

        self.__cursor = cursor
        self.__id = id

        in_base = []
        if self.__cursor is not  None and self.__id is not None:
            in_base =  self.__select()

        if in_base:
            self.__id = in_base[0][0]
            self.__username = in_base[0][1]
            self.__email = in_base[0][2]
            self.__age = in_base[0][3]
        else:
            self.__username = username
            self.__email = email
            self.__age = age

        self.__lock = None

    @property
    def lock(self):
        return self.__lock

    @lock.setter
    def lock(self, other):
        self.__lock = other

    def __enter__(self):
        if not self.__lock:
            self.__lock = True
        else:
            raise IsAlreadyBlocked
        return self

    def __exit__(self, exc_type = None, exc_val = None, exc_tb = None):
        self.__lock = False

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, other):
        self.__username = other

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, other):
        self.__id = other

    def __select(self):
        if self.__cursor is not None:
            return self.__cursor.execute(User.__select_sql, (self.__id,)).fetchall()
        else:
            raise CursorNotFound

    def __update(self):
       if self.__cursor is not None:
           self.__cursor.execute(
                                   User.__update_sql,
                                   (self.__username,
                                    self.__email,
                                    self.__age,
                                    self.__id)
                                 )
       else:
           raise CursorNotFound

    def __insert(self):
        if self.__cursor is not None:
            self.__cursor.execute(
                                    User.__insert_sql,
                                    (self.__id,
                                     self.__username,
                                     self.__email,
                                     self.__age)
                                  )
        else:
            raise CursorNotFound
    @property
    def exists(self):
      result = None
      if self.__cursor is not None:
          result = bool(self.__cursor.execute(User.__select_sql, (self.__id,)).fetchall())
      return result

    def save(self):
        if self.exists:
            self.__update()
        else:
            self.__insert()

    def __str__(self):
        return (
                    f'id={self.__id}, '
                    f'username={self.__username}, '
                    f'email={self.__email}, '
                    f'age={self.__age}'
                )

    @property
    def cursor(self):
        return self.__cursor

    @cursor.setter
    def cursor(self, other):
        if self.__cursor is not other:
            self.__cursor = other

class SQEnv():
    __db = 'users.db'
    __seq_cursors = Seq()
    def __init__(self, db_name = __db):
        self.__db_name = db_name
        self.__connect = None
        self.__cursors = []

    def __enter__(self):
        self.__connect = sqlite3.connect(self.__db_name)
        self.__cursor()
        return self

    def __exit__(self, exc_type = None, exc_val = None, exc_tb = None):
        self.__cursors.clear()
        self.__connect.close()
        self.__connect = None

    def __cursor(self):
        cursor_id = next(SQEnv.__seq_cursors)
        cursor_object = self.__connect.cursor()
        self.__cursors.append((cursor_id, cursor_object))
        return (cursor_id, cursor_object)

    @property
    def cursor(self):
        if not self.__cursors:
            self.__cursors()
        return self.__cursors[0][1]    #simple get cursor - last (one) cursor

    @cursor.setter
    def cursor(self, other):
        self.__cursors[0][1] = other
    def test_conect(self):
        return bool(self.cursor.execute('select "successful"').fetchone())

    def execute_any_sql(self,sql,*args):
        return self.cursor.execute(sql,args).fetchall()

    def commit(self):
        for i, cursor in self.__cursors:
            cursor.execute('commit')

class CollectionOfUsers:
    def __add(self, other: User):
        try:
            self.__count += len(other)
        except TypeError:
            self.__count +=1
        self.__users.extend(other)

    def __init__(self,*args:User, cursor = None):
        self.__users = []
        self.__count = 0
        self.__add(other = args)
        self.__cursor = cursor

    @property
    def cursor(self):
        return self.__cursor

    @cursor.setter
    def cursor(self, other):
        self.__cursor = other
        self.__cursor_for_items()

    def __len__(self):
        return self.__count

    def add_users(self, *args:User):
        self.__add(*args)

    def __cursor_for_items(self):
        for user in self.__users:
            user.cursor = self.__cursor

    def save(self):
        for user in self.__users:
            with user as usr:
                usr.save()
    def __getitem__(self, item):
        return self.__users[item]

class TestDataUsers:
    def __init__(self, seq_id = None, number=100_000, range_age = range(1,100), cursor = None):
        self.__users = (User(
                                 id = seq_id if seq_id is not None else None,
                                 username = "".join(random.sample(string.ascii_letters, k = 10)),
                                 email = f'{"".join(random.sample(string.ascii_letters, k = 10)).lower()}@mail.ru',
                                 age = random.randint(range_age[0],range_age[-1]),
                                 cursor = cursor
                             ) for i in range(number)
                       )
    @property
    def users(self):
        return self.__users

if __name__ == '__main__':
    with SQEnv() as cn:
        cn.execute_any_sql(sql = 'delete from Users')
        col = CollectionOfUsers(*TestDataUsers().users)
        col.cursor = cn.cursor
        col.save()
        cnt = cn.execute_any_sql(sql = 'select count(*) from Users')
        print(cnt)
        cn.commit()