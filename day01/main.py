# function for part 1
def getNumsO(s):
    g=''
    i=0
    while not s[i].isdigit():
        i += 1
    if s[i].isdigit():
        g+=s[i]
    i = len(s)-1
    while not s[i].isdigit(): i -= 1
    if s[i].isdigit():
        g+=s[i]
    return int(g)

# recursively parse part 2 into a string that can be used like part 1
def dig(s):
    words=['one','two','three','four','five','six','seven','eight','nine']
    print(s)
    if not any([w in s for w in words]): return s
    for i, a in enumerate(s):
        for j,w in enumerate(words):
            if w.startswith(a) and s[i:i+len(w)]==w:
                no = dig(s[0:i]+str(j+1)+w[1:]+s[i+len(w):])
                return no
    

                
with open('input.txt','r') as f:
    s = f.read().splitlines()
    x=0
    for e in s:
       # lots of debug variables
       r=dig(e)
       m=getNumsO(r)
       x+=m 
       with open('test.txt','a+') as ee:
           ee.write(e+" -->   "+r+"         " + str(m)+'\n')
    print(x)