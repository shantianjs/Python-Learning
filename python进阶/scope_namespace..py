import time

def output():
    a=1
    c=2
    def inner():
        print('a',a)
        c=4
        def in_inner():
            nonlocal c
            c=5
            print(c)
        return in_inner()
    inner()
    print('c',c)

#output()

class A(object):
    a=3
    def inner(self):
        a=3
        def in_inner():
            b = list(a + i for i in range(10))
            return b
        print(in_inner())
    print('a',a)

# A().inner()

#生成器形成了一个局部作用域
class B(object):
    aa = 3
    bb = (lambda  aa: (aa + i for i in range(10)))(1)
    def inner(self):
        bb=list(B.aa+i for i in range(10))
        print('bb', bb)
    print('bb',list(bb))

#B().inner()
B()

# class C():
#     cc = 4
#     def inner(cc):
#         print(cc)
#     inner()

# C()
#                  buildin            scope is bone
#                      |              namespace as node
#                  global             class can access only by itself
#                      |
#                /           |          \     \
#             enclosing     enclosing   local
#             |               |
#            function      local
#            |
#            function
#            |
#            local




