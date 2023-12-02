def power(rgb):
    return rgb[0]*rgb[1]*rgb[2]

def extract(game_str):
    header_split = game_str.split(":")
    ind = int(header_split[0][5:])
    vals = header_split[1][1:].split(";")
    rgbs = [[],[],[]]
    color_names = ["red","green","blue"]
    for set in vals:
        colors = set.split(",")
        for color in colors:
            spl = color.strip().split(" ")
            amt = int(spl[0])
            which = spl[1]
            rgbs[color_names.index(which)].append(amt)
    rgbmax= [0,0,0]
    for i,rgb in enumerate(rgbs):
        rgbmax[i] = max(rgb)
    return ind, rgbmax



with open('input.txt') as f:
    games = f.read().splitlines()
    sum_ids = 0
    for game in games:
        ind, maxvals = extract(game)
        powr = power(maxvals)
        sum_ids += powr
    print(sum_ids)