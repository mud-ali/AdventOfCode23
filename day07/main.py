class Card:

    def __init__(self, cards:str, score:int, val:int) -> None:
        self.cards = cards
        self.score = score
        self.val = val
    
    def __lt__(self, other: 'Card'):
        if self.val == other.val:
            return not getStronger(self,other) == self
        else: return self.val < other.val

    def __gt__(self, other:'Card'):
        return other < self
    
    def __str__(self):
        return self.cards + " val:"+str(self.val)+" score:"+str(self.score)

def getVal(hand:str) -> int:
    amts = {'A':0}
    for card in hand:
        if card not in amts.keys(): amts[card] = 1
        else: amts[card] += 1
    
    if 5 in amts.values(): return 7
    if 4 in amts.values(): return 6
    if 3 in amts.values():
        if 2 in amts.values(): return 5
        return 4
    if list(amts.values()).count(2) == 2: return 3
    if list(amts.values()).count(2) == 1: return 2
    return 1
    
def getStronger(hand1 : Card, hand2 : Card):
    cardvals = list("AKQJT98765432")
    for i,h in enumerate(hand1.cards):
        if h!=hand2.cards[i]:
            x1 = cardvals.index(h)
            x2 = cardvals.index(hand2.cards[i])
            return hand1 if x1 < x2 else hand2

with open('input.txt','r') as f:
    hands =[Card(r,int(g), getVal(r)) for (r,g) in [a.split() for a in f.read().split("\n")]]

    hands.sort()
    s=0
    for i,hand in enumerate(hands):
        r= hand.score * (i+1)
        print(hand,r)
        s+=r

    print(s)

