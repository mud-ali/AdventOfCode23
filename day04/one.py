def parseCard(card):
    print(card)
    winners, haves = card.split("|")
    wins = list(map(int, winners.split()))
    has = list(map(int, haves.split()))
    point_val = 0
    for lot in has:
        if lot in wins:
            if point_val==0: point_val=1
            else: point_val*=2
    return point_val

with open('input.txt','r') as f:
    cards = [c.split(":")[1].strip() for c in f.read().split("\n")]
    sumn = 0
    for card in cards:
        sumn += parseCard(card)
    print(sumn)