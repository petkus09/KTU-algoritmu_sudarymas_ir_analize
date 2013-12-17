#!/usr/bin/env python
import random
import time
from random import randint

def  prnt_statns(l ,le ,n):
    global const
    i=le
    const += 2
    for j in range(n-1, 0, -1):
        i=l[j][i-1]
        const += 2

def fast_way(a, t, e, x, n):
    global const
    f1 = [None] * n
    f2 = [None] * n
    l = [[None, None]] * n
    fe = None
    le = None
    f1[0]=e[0]+a[0][0]
    f2[0]=e[1]+a[0][1]
    const += 7
    for j in range(1, n):
        if( (f1[j-1]+a[j][0]) <= (f2[j-1]+t[j-1][1]+a[j][0]) ):
            f1[j]=f1[j-1]+a[j][0]
            l[j][0]=1
            const += 2
        else:
                 f1[j]=f2[j-1]+t[j-1][1]+a[j][0]
                 l[j][0]=2
                 const += 2
        if( (f2[j-1]+a[j][1]) <= (f1[j-1]+t[j-1][0]+a[j][1]) ):
            f2[j]=f2[j-1]+a[j][1]
            l[j][1]=2
            const += 2
        else:
             f2[j]=f1[j-1]+t[j-1][0]+a[j][1]
             l[j][1]=1
             const += 2
    if( (f1[n-1]+x[0]) <= (f2[n-1]+x[1]) ):
        fe=f1[n-1]+x[0]
        le=1
        const += 2
    else:
         fe=f2[n-1]+x[1]
         le=2
         const += 2
    prnt_statns(l,le,n)

def main(n):
    global const
    i=0
    const = 0;
    time1 = time.time()
    print "Konvejeriu skaicius: " + str(n) + "\n"
    a = [[None, None]] * n
    t = [[None, None]] * (n-1)
    e = [None] * 2
    x = [None] * 2
    e[0]=2
    e[1]=4
    x[0]=3
    x[1]=2
    const += 10
    for i in range(0, n):
        a[i][0] = int(randint(1, 1000))
        const += 1
    for i in range(0, n):
        a[i][1] = int(randint(1, 1000))
        const += 1
    for i in range(0, n-1):
        t[i][0] = int(randint(1, 1000))
        const += 1
    for i in range(0, n-1):
        t[i][1] = int(randint(1, 1000))
        const += 1
    fast_way(a,t,e,x,n)
    time2 = time.time()
    skirtumas = time2 - time1
    print "Bendras uztruktas laikas sekundemis: %(time)s" %{'time': skirtumas}
    const += 3
    print "Eiluciu kiekis: %(const)s" %{'const': const}

if __name__ == '__main__':
   main(20)
   main(100)
   main(200)
   main(500)
   main(1000)
   main(2000)
   main(5000)
   main(10000)
   main(20000)
   main(50000)
   main(100000)
   main(1000000)