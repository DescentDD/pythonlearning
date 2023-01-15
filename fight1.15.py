from abc import ABCMeta,abstractmethod
from random import randint,randrange
class fighter(object,metaclass=ABCMeta):
    __slots__ = ('_name','_hp')
    def __init__(self,name,hp):
        self._name=name
        self._hp=hp
    @property
    def name(self):
        return self._name
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self,hp):
        self._hp=hp if hp>0 else 0
    @property
    def alive(self):
        return self._hp>0
    @abstractmethod
    def attack(self,other):
        pass
class DescentDD(fighter):
    __slots__ = ('_name','_hp','_mp')
    def __init__(self,name,hp,mp):
        super().__init__(name,hp)#这里到时候调试一下fighter和descentdd有什么不一样
        self._mp=mp
    @property
    def mp(self):
        return self._mp
    @mp.setter
    def mp(self,mp):
        self._mp=mp
    def attack(self,other):
        a=['打你脸','打你肚子','踹你下面','扇你耳光']
        print(a[randint(0,4)])
        other.hp-=randint(10000000,11456789)
    def superattack(self,other):
        if self.mp>=50:
            print('对他使用赐予死亡吧')
            other.hp-=randint(27396495,36583945)
            self.mp-=50
            return True
        else:
            print('傻逼你没蓝啦')
            return False
    def __str__(self):
        return "%s的血量:%s\n蓝条:%s"%(self.name,self.hp,self.mp)
    def resume(self):
        deltamp=randint(10,21)
        self.mp+=deltamp
        return deltamp
class Monster(fighter):
    __slots__ = ('_name','_hp')
    def attack(self,other):
        other.hp-=randint(100,200)
    def __str__(self):
        return "%s的血量：%s"%(self.name,self.hp)
def displayInfo(DescentDD,Monster):
    print(DescentDD)
    print((Monster))
def main():
    u=DescentDD('DescentDD',1000,50)
    m=Monster('狗狗',100000000)
    fight_round=1
    while(u.alive>0 and m.alive>0):
        print('=======第%2d回合======='%fight_round)
        skill=randint(0,6)
        if skill>4:
            print('必杀！')
            u.superattack(m)
        else:
            print('殴打你')
            u.attack(m)
        if m.alive>0:
            print('你打我我告老师')
            m.attack(u)
        displayInfo(u,m)
        fight_round+=1
    print('\n=======战斗结束=======\n')
    if u.alive>0:
        print("爷赢辣")
    else:
        print("爷死啦")
main()

