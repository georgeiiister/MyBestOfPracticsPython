import sqlite3
import string
import random

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
    __table = 'Users'
    __create_table_sql = f'create table if not exists {__table} (id integer, username text, email text, age integer)'
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
        return self.__cursor.execute(User.__select_sql, (self.__id,)).fetchall()

    def __update(self):
       if self.__cursor is not None:
           self.__cursor.execute(
                                   User.__update_sql,
                                   (self.__username, self.__email, self.__age, self.__id)
                                 )
    def __insert(self):
        if self.__cursor is not None:
            self.__cursor.execute(
                                    User.__insert_sql,
                                    (self.__id, self.__username, self.__email, self.__age)
                                  )
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

connect = sqlite3.connect('users.db')
cur1 = connect.cursor()
User.create_table(cursor = cur1)

usr = [User(
             username = "".join(random.sample(string.ascii_letters, k=10)),
             email = f'{"".join(random.sample(string.ascii_letters, k=10))}@mail.ru',
             age = 43,
             cursor = cur1
           ) for i in range(10)
      ]

for j, i in enumerate(usr):
    i.save()
    if j%1000 == 0:
        connect.commit()
connect.commit()

usr1 = User(id=9,cursor = cur1)

print(usr1)

