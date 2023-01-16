
import random
class card(object):
    def __init__(self,suite,face):
        self._suite=suite
        self._face=face
    @property
    def face(self):
        return self._face
    @property
    def suite(self):
        return self._suite
    def __str__(self):
        if self.face==1:
            face_str='A'
        elif self.face==11:
            face_str='J'
        elif self.face==12:
            face_str='Q'
        elif self.face==13:
            face_str='K'
        else:
            face_str=str(self._face)
        return '%s%s'%(self.suite,face_str)
    def __repr__(self):
        return self.__str__()
class poker(object):
    def __init__(self):
        self._cards=[card(suite,face)
                    for suite in ['♠','♣','♦','♥']
                    for face in range(1,14)]
        self._current=0
    @property
    def cards(self):
        return self._cards
    def wash(self):
        self._current=0
        random.shuffle(self._cards)
    @property
    def next(self):
        card=self._cards[self._current]
        self._current+=1
        return card
class player(object):
    def __init__(self,name):
        self._name=name
        self._currentCards=[]
    @property
    def name(self):
        return self._name
    def get(self,card):
        self._currentCards.append(card)
    @property
    def currentCards(self):
        return self._currentCards
    def arrange(self,card_key):
        self._currentCards.sort(key=card_key)
def get_key(card):
    return (card.suite,card.face)
def main():
    p=poker()
    p.wash()
    wdd=player('DescentDD')
    for _ in range(13):
        wdd.get(p.next)
    wdd.arrange(get_key)
    print(wdd.currentCards)
main()
