with open('input.txt','r') as f:
    cards = [c.split(":")[1].strip().split('|') for c in f.read().split("\n")]
    card_scores = []
    for i, (wins, hases) in enumerate(cards):
        has = list(map(int, hases.split()))
        win = list(map(int, wins.split()))
        c_count = 0
        for h in has:
            if h in win: c_count += 1
        card_scores.append(list(range(i+2, i+2+c_count)))

    new_cards=[s+1 for s in list(range(len(cards)))]

    print(new_cards)
    idx = 0
    while idx < len(new_cards):
        r = card_scores[new_cards[idx]-1]
        new_cards += r
        idx += 1
    print(len(new_cards))