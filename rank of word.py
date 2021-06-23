# NO MODULES/LIBRARIES CAN BE USED
# Challenge link in comment section!

def findDup(x):
    d = {}
    for i in x:
        if i not in d: d[i]=1
        else: d[i]+=1
    return d.values()

def fact(x):
    if x>1: return x*fact(x-1)
    else: return x

a = x = input() or "misunderstanding"
word = ""
y = sorted(list(set(x)))

rank = 1
for k in range(len(x)-1):
    if word+"".join(sorted(x)) != a:
        #print(word+"".join(sorted(x)))
        for i in range(0,y.index(x[0])):
            n = fact(len(x)-1)/(eval("*".join([str(fact(i)) for i in findDup(x.replace(y[i],"",1))])))
            rank+=n
            #print(rank,x)
    else: break
    word+=x[0]
    x = x[1:]
    y = sorted(list(set(x)))
print(f"rank of '{a}' is {int(rank)}")
