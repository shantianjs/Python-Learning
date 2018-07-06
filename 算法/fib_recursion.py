demo=[]
def fib(n):
    if n==3:
        demo.append('2')
        return 2
    if n<=2:
        demo.append('1')
        return 1
    else:
        return fib(n-1)+fib(n-3)

print(fib(10))
a='+'.join(demo)
print(a,'\n1',a.count('1'),'2',a.count('2'),len(demo))
print(eval(a))