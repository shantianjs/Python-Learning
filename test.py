import math


class Singleton():
    def __new__(cls, *args, **kw):
        if not hasattr(cls,'_instance'):
            print('already has instance')
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance

s = Singleton()
print("Object Created", s)

t = Singleton()
print("Object Created", t)

math.log(2434,10)