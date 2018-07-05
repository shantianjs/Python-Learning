class timerr():
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance=super(timerr,cls).__new__(cls,*args,**kwargs)
        else:
            print('already has instance')
        return cls._instance


class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Test(metaclass=MetaSingleton):
    pass

class Metaclass(type):
    def __new__(cls, name, bases, dct):
        print('HAHAHA')
        dct['a'] = 1
        return type.__new__(cls, name, bases, dct)

print('before Create OBJ')
class OBJ(metaclass=Metaclass):
    pass
print('after Create OBJ')

if __name__ == '__main__':
    print(OBJ.a)
    type