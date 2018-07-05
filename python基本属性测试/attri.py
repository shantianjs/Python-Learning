class foo:
    a = 10
    def __getattr__(self, item):
        print('__getattr__ is called')
        return item + 'from getattr'
    def __getattribute__(self, item):
        print('getattribute is called')
        return object.__getattribute__(self,item)
    # def __get__(self, instance, owner):
    #     print('get is called',instance,owner)
    #     return self
    def ding(self):
        print('process is run')
    def __call__(self, *args, **kwargs):
        print('__call__ is called')
        print('name is ',args)
# class c2():
#     #a=foo()
#     pass

if __name__=='__main__':
    a=foo()
    print(a.b)
