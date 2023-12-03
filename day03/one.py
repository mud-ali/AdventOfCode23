import re
COUNT=0

def hasSymbol(s):
    if any([e!='.' and (not e.isdigit()) for e in s]):
        return True
    return False

def parse(this, other):
    res = re.finditer(r'\d+', this)
    for match in res:
        s, e = match.span()
        bef = 0 if s-1<0 else s-1
        aft = e if e+1>len(this) else e+1
        if hasSymbol(this[bef:aft]) or hasSymbol(other[bef:aft]):
            global COUNT
            COUNT += int(this[s:e])
        else:
            print(match.group())


with open('input.txt') as f:
    rows = f.read().split("\n")
    for i, row in enumerate(rows):
        if i == 0:
            parse(row, rows[i+1])
        elif i==len(rows)-1:
            parse(row, rows[i-1])
        else:
            n=''
            for j,e in enumerate(rows[i-1]):
                if hasSymbol(rows[i+1][j]) or hasSymbol(e):
                    n+='*'
                else:
                    n+='.'
            parse(row, n)
    print(COUNT)