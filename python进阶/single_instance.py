import math
import threading


class Singleton():
    single_lock = threading.Lock()

    def __new__(cls, *args, **kw):
        with Singleton.single_lock:
            if not hasattr(cls, '_instance'):
                print('already has instance')
                cls._instance = super().__new__(cls, *args, **kw)




s = Singleton()
print("Object Created", s)

t = Singleton()
print("Object Created", t)


