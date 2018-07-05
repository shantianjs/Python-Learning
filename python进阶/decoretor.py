from functools import wraps
import time
import random
def time_couter(func):
    'decorator without param'
    @wraps(func)
    def wrap(*args,**kwargs):
        '''function of decoractor'''
        start = time.perf_counter()
        print(func.__name__,'is called.')
        func(*args,**kwargs)
        print('time:',time.perf_counter()-start,' s')
    return wrap


