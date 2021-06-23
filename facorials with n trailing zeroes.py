x,n,p = int(input()),0,0
while n!=x:
    p+=5
    s=p
    while s%5==0 and s>0:
        s/=5
        n+=1
print("\n".join([str(i)+"!" for i in range(p,p+5)]))
