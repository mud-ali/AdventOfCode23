def getVal(hand):
    key_max = []
    keymax2 = []
    amts = {'A':0}
    for card in hand:
        if card not in amts.keys(): amts[card] = 1
        else: amts[card] += 1
    max_val = max(list(amts.values()))
    next_max_val = max([a if a!=max_val else 0 for a in list(amts.values())])
    for n in amts.keys():
        if amts[n] == max_val:
            key_max.append(n)
        if amts[n] == next_max_val:
            keymax2 = n
    print(max_val, next_max_val)
    


with open('test.txt','r') as f:
    hands =[(r,int(g)) for (r,g) in [a.split() for a in f.read().split("\n")]]
    print(hands)
