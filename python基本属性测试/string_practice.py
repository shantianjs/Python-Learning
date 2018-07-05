from random import choice

#打印迷宫
for i in range(24):
    print(''.join(choice('\u2571\u2572')for i in range(50)))

print('\n'.join([''.join([('AaaaLove{:d}{:d}'.format(x,y)[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ') for x in range(-30,30)])for y in range(15,-15,-1)]))

#99乘法表
print('\n'.join([' '.join(['{0}*{1}={2}'.format(y,x,x*y) for y in range(1,x+1)] )for x in range(1,10)]))
