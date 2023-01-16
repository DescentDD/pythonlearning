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
"""
s1 = 'hello, world!'
s2 = "hello, world!"
print(s1, s2, end='')

set1 = {1, 2, 3, 3, 3, 2}
print(set1)#1，2，3
print('Length =', len(set1))

import os
import time



content = 'åäº¬æ¬¢è¿ä½ ä¸ºä½ å¼å¤©è¾å°â¦â¦â¦â¦'
while True:
    # æ¸çå±å¹ä¸çè¾åº
    os.system('cls')  # os.system('clear')
    print(content)
    # ä¼ç 200æ¯«ç§
    time.sleep(0.2)
    content = content[1:] + content[0]
from random import randint,sample

def display(balls):
"""

"""
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
"""
"""
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('abcd: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()
"""
#day8
"""
class Test:

    def __init__(self, foo):
        self.__foo = foo

    def bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    test.bar()
    # AttributeError: 'Test' object has no attribute '__foo'



if __name__ == "__main__":
    main()

from time import sleep


class Clock(object):


    def __init__(self, hour=0, minute=0, second=0):
  
        
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
      
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        
        return '%02d:%02d:%02d' % 
               (self._hour, self._minute, self._second)


def main():
    clock = Clock()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
"""
#day9
"""
class Person(object):

    __slots__ = ('_name','_agew','_gender','fuck')
    def __init__(self, name, agee):
        self._name = name
        self._agew = agee


    @property
    def name(self):
        return self._name
    @property
    def ageo(self):
        return self._agew


    @ageo.setter
    def ages(self, fuck):
        self._agew = fuck

    def play(self):
        if self._agew <= 16:
            print('%sqwjd' % self._name)
        else:
            print('%sqwer' % self._name)


def main():
    person = Person('0086', 12)
    person.play()
    person._gender='male'
    person.fuck='lll'
    print(person.name)
    print(person._agew)
    print(person._gender)
    print(person.fuck)
    person.ages = 22
    person.play()


if __name__ == '__main__':
    main()


from time import localtime,time
ctime=localtime()
print(ctime.tm_hour)
"""
#day10,fight1.15.py
#day11,card.py
