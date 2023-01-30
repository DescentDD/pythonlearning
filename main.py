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
"""
import tkinter
import tkinter.messagebox


def main():
    flag = True

    # ä¿®æ¹æ ç­¾ä¸çæå­
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # ç¡®è®¤éåº
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('æ¸©é¦¨æç¤º', 'ç¡®å®è¦éåºå?'):
            top.quit()

    # åå»ºé¡¶å±çªå£
    top = tkinter.Tk()
    # è®¾ç½®çªå£å¤§å°
    top.geometry('240x160')
    # è®¾ç½®çªå£æ é¢
    top.title('å°æ¸¸æ')
    # åå»ºæ ç­¾å¯¹è±¡å¹¶æ·»å å°é¡¶å±çªå£
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # åå»ºä¸ä¸ªè£æé®çå®¹å¨
    panel = tkinter.Frame(top)
    # åå»ºæé®å¯¹è±¡ æå®æ·»å å°åªä¸ªå®¹å¨ä¸­ éè¿commandåæ°ç»å®äºä»¶åè°å½æ°
    button1 = tkinter.Button(panel, text='ä¿®æ¹', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='éåº', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # å¼å¯ä¸»äºä»¶å¾ªç¯
    tkinter.mainloop()


if __name__ == '__main__':
    main()
"""
#day12
"""
from enum import Enum, unique
from math import sqrt
from random import randint

import pygame


@unique
class Color(Enum):


    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():

        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):


    def __init__(self, x, y, radius, sx, sy, color=Color.RED):

        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):

        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):

        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):

        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)
def main():
    # å®ä¹ç¨æ¥è£ææççå®¹å¨
    balls = []
    # åå§åå¯¼å¥çpygameä¸­çæ¨¡å
    pygame.init()
    # åå§åç¨äºæ¾ç¤ºççªå£å¹¶è®¾ç½®çªå£å°ºå¯¸
    screen = pygame.display.set_mode((800, 600))
    # è®¾ç½®å½åçªå£çæ é¢
    pygame.display.set_caption('å¤§çåå°ç')
    running = True
    # å¼å¯ä¸ä¸ªäºä»¶å¾ªç¯å¤çåççäºä»¶
    while running:
        # ä»æ¶æ¯éåä¸­è·åäºä»¶å¹¶å¯¹äºä»¶è¿è¡å¤ç
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # å¤çé¼ æ äºä»¶çä»£ç 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # è·å¾ç¹å»é¼ æ çä½ç½®
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                # å¨ç¹å»é¼ æ çä½ç½®åå»ºä¸ä¸ªç(å¤§å°ãéåº¦åé¢è²éæº)
                ball = Ball(x, y, radius, sx, sy, color)
                # å°çæ·»å å°åè¡¨å®¹å¨ä¸­
                balls.append(ball)
        screen.fill((255, 255, 255))
        # ååºå®¹å¨ä¸­çç å¦ææ²¡è¢«åæå°±ç»å¶ è¢«åæäºå°±ç§»é¤
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        # æ¯é50æ¯«ç§å°±æ¹åççä½ç½®åå·æ°çªå£
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            # æ£æ¥çææ²¡æåå°å¶ä»çç
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main()
"""
#day13
"""
éªè¯è¾å¥ç¨æ·ååQQå·æ¯å¦ææå¹¶ç»åºå¯¹åºçæç¤ºä¿¡æ¯

è¦æ±ï¼ç¨æ·åå¿é¡»ç±å­æ¯ãæ°å­æä¸åçº¿ææä¸é¿åº¦å¨6~20ä¸ªå­ç¬¦ä¹é´ï¼QQå·æ¯5~12çæ°å­ä¸é¦ä½ä¸è½ä¸º0
"""
"""
import re

    匹配用户名r’开头^0-9或者a-z或者A-Z或者下划线6到20位结尾$
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    匹配qq号：r‘1到9开头，数字4-11位’
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)

    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)  # 你丫是*吗? 我*你大爷的. * you.
    
        poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)  # ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']
"""
#day14
"""
from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()

from time import sleep
from threading import Thread, Lock


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续的代码
        self._lock.acquire()

        new_balance = self._balance + money
        sleep(0.01)
        self._balance = new_balance

        # 在finally中执行释放锁的操作保证正常异常锁都能释放
        self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()
"""
"""
import time
import tkinter
import tkinter.messagebox
from threading import Thread


def main():

    class DownloadTaskHandler(Thread):

        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('提示', '下载完成!')
            # 启用下载按钮
            button1.config(state=tkinter.NORMAL)

    def download():
        # 禁用下载按钮
        button1.config(state=tkinter.DISABLED)
        # 通过daemon参数将线程设置为守护线程(主程序退出就不再保留执行)
        # 在线程中处理耗时间的下载任务
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')

    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', 1)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()

from multiprocessing import Process, Queue
from random import randint
from time import time


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end - start), 's', sep='')
    


if __name__ == '__main__':
    main()
"""
#day18
from time import time
from threading import Thread

import requests


# 继承Thread类创建自定义的线程类
"""
class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/Users/Hao/' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    # 通过requests模块的get函数获取网络资源
    # 下面的代码中使用了天行数据接口提供的网络API
    # 要使用该数据接口需要在天行数据的网站上注册
    # 然后用自己的Key替换掉下面代码的中APIKey即可
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=APIKey&num=10')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        # 通过多线程的方式实现图片下载
        DownloadHanlder(url).start()


if __name__ == '__main__':
    main()

s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')

a, b = 5, 10
print(f'{a} * {b} = {a * b}')

file=open("123.txt",mode="a")
file.write("我是你爹")
file.close()
"""
