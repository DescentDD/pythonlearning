#import this
#day1
"""
这是注释
"""
#这也是注释
"""
a,b=input().split()
a=int(a)
print(f'{a:.2f}')
"""
#scan 1 2;print 1.00
#day3
"""
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')
"""
"""
print('*')
print('*')
print('*',end='')
print('*')
"""
#day4
"""
def foo():
    print('hello, world!')
def foo():
    print('goodbye, world!')
foo()
import module1 as m1
import module2 as m2

m1.foo()
m2.foo()
from module1 import foo
"""
"""
def foo():
    global a
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 200
    #global覆盖
    """