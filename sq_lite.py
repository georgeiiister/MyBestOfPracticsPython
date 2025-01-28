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
    __create_table_sql = (
                            f'create table if not exists {__table}'
                            f'('
                            f'id integer,'
                            f'fusername text,'
                            f'email text,'
                            f'age integer)'
                         )

    __insert_sql = f'insert into {__table} values(?,?,?,?)'
    __select_sql = f'select * from {__table} where id=?'
    __update_sql = f'update {__table} set username=?,email=?, age=? where id=?'
    __select_avg_age_sql = f'select cast(avg(age) as integer) as av from Users'
    __select_greatest_avg_age = f'select * from Users where age>?'

    __seq = Seq()

    @classmethod
    def avg_age(cls,cursor):
        return cursor.execute(User.__select_avg_age_sql).fetchone()[0]

    @classmethod
    def result_set_greates_avg_age(cls,cursor):
        result = cursor.execute(User.__select_greatest_avg_age,(User.avg_age(cursor = cursor),)).fetchall()
        return {rec[0]:{'id':rec[0],'username':rec[1], 'email':rec[2], 'age':rec[3]}
                for rec in result}

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
                                   (self.__username,
                                    self.__email,
                                    self.__age,
                                    self.__id)
                                 )
    def __insert(self):
        if self.__cursor is not None:
            self.__cursor.execute(
                                    User.__insert_sql,
                                    (self.__id,
                                     self.__username,
                                     self.__email,
                                     self.__age)
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

    @property
    def cursor(self):
        return self.__cursor

    @cursor.setter
    def cursor(self, other):
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
        return bool(self.cursor.execute('select "saccess"').fetchone())

    def execute_any_sql(self,sql,*args):
        self.cursor.execute(sql,args).fetchone()

    def commit(self):
        for i, cursor in self.__cursors:
            cursor.execute('commit')

class TestDataUsers:
    def __init__(self,*args:User):
        self.__users = args

    def generate(self, number:int, range_age = range(1,100), cursor = None):
        self.__users = tuple(User(
                                     username = "".join(random.sample(string.ascii_letters, k = 10)),
                                     email = f'{"".join(random.sample(string.ascii_letters, k = 10)).lower()}@mail.ru',
                                     age = random.randint(range_age[0],range_age[-1]),
                                     cursor = cursor
                                  ) for i in range(number)
                            )
    def cursor(self, cursor):
        for item in self.__users:
            item.cursor(other = cursor)

    def save(self):
        for item in self.__users:
            if item.cursor:
                item.save()
            else:
                raise ValueError
    def __getitem__(self,item):
        return self.__users[item]

if __name__ == '__main__':
    with SQEnv() as cn:
        cn.execute_any_sql(sql = 'delete from Users')
        tests_users = TestDataUsers()
        tests_users.generate(number=100, range_age=range(1, 100),cursor=cn.cursor)
        tests_users.save()
        cn.commit()
        print(User.avg_age(cursor=cn.cursor))
